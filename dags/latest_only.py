import datetime as dt

import airflow
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.latest_only_operator import LatestOnlyOperator

dag = DAG(
    dag_id='latest_only',
    schedule_interval=dt.timedelta(hours=4),
    start_date=airflow.utils.dates.days_ago(2),
)

latest_only = LatestOnlyOperator(task_id='latest_only', dag=dag)
task1 = DummyOperator(task_id='task1', dag=dag)

latest_only >> task1
