# Project Goal

ELT data pipeline based on the following datasets: _, _, _, _. As a result, clients will have an everyday update database that will allow them to find answers to questions based on _ (expats in the U.S.)


# Initial Thoughts

Some questions/queries I formulate myself that draw me to work with these datasets were:

- 
- 
- 

# Explore and Assess the Data

Many of the data comes in a raw format and in different kinds of format. Not all data is tabular.

- I94 Immigration Data: This data comes from the US National Tourism and Trade Office. ![here](https://travel.trade.gov/research/reports/i94/historical/2016.html)
<!-- A data dictionary is included in the workspace.  -->
- World Temperature Data: This dataset came from Kaggle. You can read more about it ![here](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data).
- U.S. City Demographic Data: This data comes from OpenSoft. You can read more about it ![here](https://public.opendatasoft.com/explore/dataset/us-cities-demographics/export/).
- Airport Code Table: This is a simple table of airport codes and corresponding cities. It comes from ![here](https://datahub.io/core/airport-codes#data).

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