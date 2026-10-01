from airflow.sdk import dag, task
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from datetime import datetime

@dag(
    dag_id="etl_ingest_postgres",
    schedule="@daily",
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["exemplo2", "etl", "postgres"],
)
def etl_ingest_postgres():

    create_pet_table = SQLExecuteQueryOperator(
        task_id="create_pet_table",
        conn_id="sample_postgres",
        sql="sql/pet_schema.sql",
    )

    create_pet_table()

etl_ingest_postgres()
