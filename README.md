# CORAL: Community in Oncology for RApid Learning

## Introduction

UM/MUMC+/Maastro Clinical Data Science (CDS) did a study in 2018 internally 
called the 20k challenge [1]. In this challenge we successfully applied 
privacy-preserving, federated learning / Personal Health Train principles 
to learn and validate a prediction model for 2 year overall survival for 
lung cancer patients using more than 20.000 patients from 8 sites. 

The CDS vision is to responsibly learn from all data of all people in the world 
to improve health, therefore we would like to continuously extend our 
network of hospitals which share this vision. The current state of the network 
with past, present and prospective partners is shown in the figure below. 

 ![CORAL network](./figures/coral_network.png)

To onboard new partners and maintain this network, we need to have an 
easy-to-implement, continuous learning project. The 20k challenge seems a 
good choice for this as it only concerns a limited number of data elements 
which are all often well captured in clinical routine practice.

## Requirements

## Environment variables

## How to run

### Setting up the infrastructure

Before running the infrastructure, a few things have to be set up.
First of all, copy the sample `.env` file (and make any changes to passwords):

```bash
cp .env.example .env
```

Do the same for the `r2rml.properties` file under `airflow/r2rml`:

```bash
cp airflow/r2rml/r2rml.properties.example airflow/r2rml/r2rml.properties
```

Next upload a mapping file `mapping.ttl` to the `airflow/r2rml` directory, 
which will be used to map tabular data to triples.

### Running the infrastructure

After everything has been set up, the infrastructure can be run using the
following command:

```bash
docker compose up
```

To upload data, put a zip with your CSV files in the `input` directory. Within
a few seconds the data should be picked up and processed to triples, which
can be found in the `output` directory.

## References

[1] T. M. Deist et al., “Distributed learning on 20 000+ lung cancer patients – 
The Personal Health Train,” Radiother. Oncol., vol. 144, pp. 189–200, Mar. 2020, 
doi: 10.1016/j.radonc.2019.11.019.