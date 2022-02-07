from datetime import timedelta, datetime
from pathlib import Path
import os
import logging
import xml.etree.ElementTree as et

from airflow import DAG
from airflow.utils.decorators import apply_defaults
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from airflow.models import Variable
from airflow import settings

import pandas as pd
import rdflib as rdf
import requests
import yaml
from zeep import Client
import lxml
from bs4 import BeautifulSoup

from sparql.query_engine import QueryEngine


def get_lc_ss_oid(lc_endpoint, lc_user, lc_password, study_identifier, ss_label, ss_gender, ss_birthdate=None, ss_birthyear=None, rerun=False):
    LOGGER = logging.getLogger("airflow.task")
    LOGGER.info(f'Trying to get SS_OID for {ss_label}')

    client = Client(lc_endpoint + 'studySubject/v1/studySubjectWsdl.wsdl')

    header = f'''
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v1="http://openclinica.org/ws/studySubject/v1" xmlns:bean="http://openclinica.org/ws/beans">
        <soapenv:Header>
            <wsse:Security soapenv:mustUnderstand="1" xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
            <wsse:UsernameToken wsu:Id="UsernameToken-27777511" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
                <wsse:Username>{lc_user}</wsse:Username>
                <wsse:Password type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">{lc_password}</wsse:Password>
            </wsse:UsernameToken>
            </wsse:Security>
        </soapenv:Header>
    </soapenv:Envelope>
    '''
    header = lxml.etree.fromstring(header)[0][0]

    # Check if subject exists
    subject = {
        'label': ss_label,
        'enrollmentDate': '1900-01-01',#This is ignored by LC but because bad soap implementation we have to supply it
        'subject': {},
        'studyRef': {
            'identifier': study_identifier
        }
    }

    with client.settings(strict=False):
        ret = client.service.isStudySubject(subject, _soapheaders=[header])

    if ret['result'] == 'Success':
        # if yes return
        oid = ret['_raw_elements'].pop().text
        LOGGER.info(f'Found SS OID {oid}')
        return oid
    elif not rerun:
        # Else create the SS
        LOGGER.info("Couldn't find an OID, creating a new SS")
        subject = {
            'label': ss_label,
            'enrollmentDate': '2021-08-31',
            'subject': {
                'uniqueIdentifier': ss_label,
                'gender': ss_gender,
            },
            'studyRef': {
                'identifier': study_identifier
            }
        }

        if ss_birthyear:
            subject['subject']['yearOfBirth'] = ss_birthyear
        elif ss_birthdate:
            subject['subject']['dateOfBirth'] = ss_birthdate
        else:
            raise ValueError('Need a year or date of birth to create SS')

        with client.settings(strict=False):
            ret = client.service.create(subject, _soapheaders=[header])

        if ret['result'] == 'Success':
            # Rerun this method because LC doesn't actaully give us back the OID
            LOGGER.info('All went well, rerunning to fetch OID')
            return get_lc_ss_oid(lc_endpoint, lc_user, lc_password, study_identifier, ss_label, True)
        else:
            # Couldn't create user
            LOGGER.warning(f'Could not create user: {ret["error"]}')
            return None
    else:
        # we created a new user but it's still not here, great
        return None


def upload_to_lc(
        sparql_endpoint, query,
        lc_endpoint,
        lc_user,
        lc_password,
        study_oid,
        study_identifier,
        event_oid,
        form_oid,
        item_group_oid,
        identifier_colname,
        birthdate_colname,
        birthdate_isyear,
        gender_colname,
        item_prefix,
        alternative_item_oids={},
        **kwargs):
    LOGGER = logging.getLogger("airflow.task")
    LOGGER.info(f'Retrieving triples from {sparql_endpoint}')
    sparql = QueryEngine(sparql_endpoint)
    df: pd.DataFrame = sparql.get_sparql_dataframe(query)
    LOGGER.info(f'Received {len(df)} rows of data')

    df = df.rename(columns=alternative_item_oids)

    LOGGER.info(f'Have columns {df.columns}')

    header = f'''
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v1="http://openclinica.org/ws/studySubject/v1" xmlns:bean="http://openclinica.org/ws/beans">
        <soapenv:Header>
            <wsse:Security soapenv:mustUnderstand="1" xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
            <wsse:UsernameToken wsu:Id="UsernameToken-27777511" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
                <wsse:Username>{lc_user}</wsse:Username>
                <wsse:Password type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">{lc_password}</wsse:Password>
            </wsse:UsernameToken>
            </wsse:Security>
        </soapenv:Header>
    </soapenv:Envelope>
    '''
    header = lxml.etree.fromstring(header)[0][0]

    failed_subjects = []

    for _, row in df.iterrows():
        ss_label = row[identifier_colname]
        LOGGER.debug(f'Adding subject {id}')

        # Get SS OID
        ss_oid = get_lc_ss_oid(
            lc_endpoint,
            lc_user,
            lc_password,
            study_identifier,
            ss_label,
            row[gender_colname],
            row[birthdate_colname] if not birthdate_isyear else None,
            row[birthdate_colname] if birthdate_isyear else None,
        )

        LOGGER.debug(f'Got SS_OID {ss_label}')

        event = {
            'studySubjectRef': {
                'label': ss_label
            },
            'studyRef': {
                'identifier': study_identifier
            },
            'eventDefinitionOID': event_oid,
            'startDate': '2000-01-01'
        }

        # Make sure the event is scheduled
        client = Client(lc_endpoint + 'event/v1/eventWsdl.wsdl')
        with client.settings(strict=False):
            ret = client.service.schedule(event, _soapheaders=[header])

        LOGGER.debug(f'Got return code {ret["result"]} for scheduling the event')

        items = ''
        for name in df.columns:
            if name != identifier_colname:
                if row[name] is not None:
                    items += f'<ItemData ItemOID="{item_prefix}{name}" Value="{row[name]}"/>\n'

        subject = f'''
            <SubjectData SubjectKey="{ss_oid}">
                <StudyEventData StudyEventOID="{event_oid}" StudyEventRepeatKey="1">
                    <FormData FormOID="{form_oid}" OpenClinica:Status="initial data entry">
                        <ItemGroupData ItemGroupOID="{item_group_oid}" ItemGroupRepeatKey="1" TransactionType="Insert">
                            {items}
                        </ItemGroupData>
                    </FormData>
                </StudyEventData>
            </SubjectData>
        '''

        LOGGER.info(f'Starting upload for {ss_label}')

        submit_data = f'''
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v1="http://openclinica.org/ws/data/v1" xmlns:OpenClinica="http://www.openclinica.org/ns/odm_ext_v130/v3.1">
            <soapenv:Header>
                <wsse:Security soapenv:mustUnderstand="1" xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
                    <wsse:UsernameToken wsu:Id="UsernameToken-27777511" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
                        <wsse:Username>{lc_user}</wsse:Username>
                        <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">{lc_password}</wsse:Password>
                    </wsse:UsernameToken>
                </wsse:Security>
            </soapenv:Header>

            <soapenv:Body>
            <v1:importRequest>
            <odm>
            <ODM>
            <ClinicalData StudyOID="{study_oid}" MetaDataVersionOID="v1.0.0">
                <UpsertOn NotStarted="true" DataEntryStarted="true" DataEntryComplete="true"/>
                {subject}
            </ClinicalData>
            </ODM>
            </odm>
            </v1:importRequest>  
            </soapenv:Body>
            </soapenv:Envelope>
        '''

        ret = requests.post(lc_endpoint + 'data/v1/dataWsdl.wsdl', data=submit_data, headers={'SOAPAction': '""', 'Content-Type': 'text/xml; charset=utf-8'})
        LOGGER.debug(f'Got return code {ret.status_code} for upload')
        ret = BeautifulSoup(ret.text)
        ret_code = ret.find_all('result')[0].text
        if 'Success' in ret_code:
            LOGGER.info('Succeeded in upload:')
            LOGGER.info(f'{ret_code}')
        else:
            error = ret.find_all("error")[0].text
            LOGGER.warning(f'Got a non-success code back from LC: {error}')
            failed_subjects.append({'subject': ss_label, 'error': error})

    if failed_subjects:
        LOGGER.warning(f'Failed to upload these study subjects: \n{failed_subjects}')


def create_dag(dag_id,
               schedule,
               default_args,
               upload_kwargs):

    dag = DAG(
        dag_id,
        default_args=default_args,
        schedule_interval=schedule,
        start_date=days_ago(0),
        catchup=False,
        max_active_runs=1
    )

    op_kwargs = upload_kwargs
    op_kwargs['sparql_endpoint'] = Variable.get('SPARQL_ENDPOINT')
    op_kwargs['lc_endpoint'] = Variable.get('LC_ENDPOINT')
    op_kwargs['lc_user'] = Variable.get('LC_USER')
    op_kwargs['lc_password'] = Variable.get('LC_PASSWORD')

    with dag:
        t1 = PythonOperator(
            task_id='push_lc',
            python_callable=upload_to_lc,
            op_kwargs=upload_kwargs)

    return dag

filename = Variable.get('LC_UPLOAD_CONFIG')
with open(filename) as f:
    upload_config = yaml.load(f)

for key, val in upload_config.items():
    dag_id = f'lc_upload_list_{key}'

    default_args = {
        'owner': 'airflow',
        'depends_on_past': False,
        'retries': 0,
    }

    globals()[dag_id] = create_dag(dag_id=dag_id,
                                schedule=None,
                                default_args=default_args,
                                upload_kwargs=val)