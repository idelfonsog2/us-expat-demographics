# Project Goal

The goal of this project is to create an ELT job using the following datasets: _, _, _, _. As a result, clients will have an everyday update database that will allow them to find answers to questions based on _ (inmigrations events)


# Initial Thoughts

Some questions/queries I formulate myself that draw me to work with these datasets were:

- 
- 
- 

# Explore and Assess the Data

Many of the data comes in a raw format and in different kinds of format. Not all data is tabular.

- List Data sources
- 
- 
- 

# Define the Data Model
Why did you choose the model you chose?


# Run ETL to Model the Data

- data_dictionary.txt is the file that contains the descriptions of the columns 

# Technologies Used
- Apache Spark
- Amazon Athena
- Apache Airflow
    - Python
    - Boto3
    - AWS Glue (Spark jobs)
    - AWS S3

1. The main use for **Apache Airflow** is that the analysis included in the original query file need to run on a daily bases job at 07:00
3. Additionally **Apache Airflow** let us setup the infrastructure like what resources should be created or run after a particular step in the process has been completed or fail
2. The reason to pick **AWS Athena** is because its cost-saving as a result the main disadvantage is a bit a performance given when reading or writing either from the data source or its result respectively.
3. **Boto3** is a Python API for AWS services that we will be using in **Apache Airflow** steps
4. How would Spark or Airflow be incorporated? 

# *Insert Airflow DAG Graph*


# What if...

- If the data was increased by 100x. **How would you do it?**
- If the pipelines were run on a daily basis by 7am. **How would you do it?**
- If the database needed to be accessed by 100+ people. **How would you do it?**



# REmove
facts consists of the measurement, metrics. They are usually ints or numbers
dimensions table are people, product, places, and time, information that are not use for aggregation