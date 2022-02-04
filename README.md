# FAIRifier 2.0

The goal of the FAIRifier is to FAIRify tabular data. 
This tooling focuses on the I and R of FAIR, and achieves this by turning tabular data into RDF data.

The tool is based on a few pipelines defined in python files (under `airflow/dags`), which are responsible for different parts of the transformation.
These pipelines include one to upload data to a LibreClinica instance.

## Configuration

Configuration is mostly done through environment variables, which are loaded into the Airflow workers.
`.env.example` has a list of all the necessary configuration options. 
Note that all of these can also be defined in Airflow itself, under `Variables`.