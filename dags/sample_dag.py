from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 7, 24),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Instantiate the DAG
dag = DAG(
    'simple_dag_example',
    default_args=default_args,
    description='A simple example DAG',
    schedule_interval=timedelta(days=1),
)

# Define tasks for the DAG
task_1 = DummyOperator(task_id='task_1', dag=dag)

def print_hello():
    print("Hello, Airflow!")

task_2 = PythonOperator(
    task_id='task_2',
    python_callable=print_hello,
    dag=dag,
)

task_3 = DummyOperator(task_id='task_3', dag=dag)
task_4 = DummyOperator(task_id='task_4', dag=dag)

# Set the task dependencies
task_1 >> task_2
task_1 >> task_3
task_2 >> task_4
task_3 >> task_4
