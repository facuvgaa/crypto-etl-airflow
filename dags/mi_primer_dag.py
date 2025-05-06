
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import os

default_args = {
     'owner': 'airflow',
     'depends_on_past': False,
     'start_date' : datetime(2024, 1, 1),
     'retries': 1,
     'retry_delay': timedelta(minutes=5),
}

dag = DAG(
     dag_id ='crypto_pipeline',
     default_args=default_args,
     description= 'Pipeline ETL (api de coingecko) + Estimación de criptomonedas',
     schedule_interval='@daily',
     catchup=False,
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'scripts'))

ETL_PATH = os.path.join(SCRIPTS_DIR, 'etl.py')
PREDICT_PATH = os.path.join(SCRIPTS_DIR, 'main.py')

etl_task = BashOperator(
     task_id = 'run_etl',
     bash_command= f'python {ETL_PATH}',
     dag =dag,
)

predict_task = BashOperator(
     task_id = 'run_prediction',
     bash_command=f'python {PREDICT_PATH}',
     dag=dag,
)

etl_task >> predict_task