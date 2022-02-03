FROM apache/airflow:2.2.3-python3.7

# Install Java
USER root
RUN mkdir -p /usr/share/man/man1
RUN apt-get update && apt-get install -y default-jdk && apt-get install -y git && apt-get clean
USER airflow

COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt