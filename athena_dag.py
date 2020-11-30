import boto3
from botocore.exceptions import ClientError
import json
import configparser

from airflow.contrib.hooks.aws_hook import AwsHook
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.amazon.aws.operators.glue import AwsGlueJobOperator

s3 = None
iam = None

def fetch_aws(*args, **kwargs):
    self.aws_conn_id = AwsHook("aws_credentials")

# def create_athena():
#     glue = boto3.client('glue',
#                     region_name="us-east-2",
#                     aws_access_key_id=KEY,
#                     aws_secret_access_key=SECRET,
#                     )

#     try:
#         response = client.create_crawler(
#             Name='string',
#             Role='string',
#             DatabaseName='string',
#             Description='string',
#             Targets={
#                 'S3Targets': [
#                     {
#                         'Path': 'string',
#                         'Exclusions': [
#                             'string',
#                         ],
#                         'ConnectionName': 'string'
#                     },
#                 ],
#                 'JdbcTargets': [
#                     {
#                         'ConnectionName': 'string',
#                         'Path': 'string',
#                         'Exclusions': [
#                             'string',
#                         ]
#                     },
#                 ],
#                 'MongoDBTargets': [
#                     {
#                         'ConnectionName': 'string',
#                         'Path': 'string',
#                         'ScanAll': True|False
#                     },
#                 ],
#                 'DynamoDBTargets': [
#                     {
#                         'Path': 'string',
#                         'scanAll': True|False,
#                         'scanRate': 123.0
#                     },
#                 ],
#                 'CatalogTargets': [
#                     {
#                         'DatabaseName': 'string',
#                         'Tables': [
#                             'string',
#                         ]
#                     },
#                 ]
#             },
#             Schedule='string',
#             Classifiers=[
#                 'string',
#             ],
#             TablePrefix='string',
#             SchemaChangePolicy={
#                 'UpdateBehavior': 'LOG'|'UPDATE_IN_DATABASE',
#                 'DeleteBehavior': 'LOG'|'DELETE_FROM_DATABASE'|'DEPRECATE_IN_DATABASE'
#             },
#             RecrawlPolicy={
#                 'RecrawlBehavior': 'CRAWL_EVERYTHING'|'CRAWL_NEW_FOLDERS_ONLY'
#             },
#             LineageConfiguration={
#                 'CrawlerLineageSettings': 'ENABLE'|'DISABLE'
#             },
#             Configuration='string',
#             CrawlerSecurityConfiguration='string',
#             Tags={
#                 'string': 'string'
#             }
#         )   
#     except Exception as e:
#         print(e)

default_args = {
    'owner': 'Idelfonso',
    'depends_on_past': False,
    'email': ['idelfonsog2@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'catchup': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2018, 11, 1)
}

dag = DAG('immigration_dag',
          default_args=default_args,
          description='ETL for immigration events in the US',
          schedule_interval='@daily')

# create_iam_role_task = PythonOperator(
#     task_id='create_iam_role',
#     dag=dag,
#     python_callable=create_iam_role
# )

load_and_analyze_task = AwsGlueJobOperator(
    task_id='load_and_analyze',
    dag=dag,
    job_name = 'glue_job',
    job_desc=None,
    script_location=spark_job.py,
    concurrent_run_limit=1,
    script_args=None,
    retry_limit=2,
    num_of_dpus=2,
    aws_conn_id=self.aws_conn_id,
    region_name='us-east-2',
    s3_bucket=self.s3_bucket,
    iam_role_name=DWH_IAM_ROLE_NAME
)

create_iam_role_task >> load_and_analyze_task