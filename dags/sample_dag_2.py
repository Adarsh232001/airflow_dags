from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def print_and_log_message():
    message = "It's working"
    print(message)
    # Logging the message
    # You can replace the print statement with appropriate logging configuration based on your requirements

dag = DAG(
    'simple_dag',
    description='A simple DAG that prints and logs a message',
    start_date=datetime(2023, 7, 4),
    schedule_interval=None,
)

print_and_log_task = PythonOperator(
    task_id='print_and_log_task',
    python_callable=print_and_log_message,
    dag=dag,
)

print_and_log_task
