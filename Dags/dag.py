from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
# from aiflow.utils.date import days_ago
from airflow.operators.python_operator import PythonOperator
from etl import transform_load_data

default_args = {
    'owner':  'airflow',
    'depends_on_past' : False,
    'start_date' : datetime(2024, 8, 24),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG('weather_data_pipeline',
          default_args = default_args,
          description= 'ETL Pipeline for weather data',
          catchup = False,
          schedule_interval='@daily')

run_etl = PythonOperator(
                         task_id = 'run_etl',
                         python_callable = transform_load_data,
                         dag =dag
)

run_etl


   