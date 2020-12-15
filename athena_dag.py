import boto3
from botocore.exceptions import ClientError
import json
import configparser
import datetime

from airflow.contrib.hooks.aws_hook import AwsHook
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.amazon.aws.operators.glue import AwsGlueJobOperator

def fetch_aws(*args, **kwargs):
    self.aws_conn_id = AwsHook("aws_credentials")

default_args = {
    'owner': 'Idelfonso',
    'depends_on_past': False,
    'email': ['idelfonsog2@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'catchup': False,
    'retries': 3,
    'retry_delay': datetime.timedelta(minutes=5),
    'start_date': datetime.datetime(2018, 11, 1)
}

dag = DAG('immigration_dag',
          default_args=default_args,
          description='ETL for immigration events in the US',
          schedule_interval='@daily')
          