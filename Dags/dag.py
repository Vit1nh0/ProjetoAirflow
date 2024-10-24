from airflow import DAG
from airflow.operators.python import PythonOperator
from pymongo import MongoClient, errors
import pandas as pd
from datetime import datetime, timedelta

def remove_duplicates(collection):
    
    all_docs = list(collection.find())
    
    seen = set()
    duplicates = []
    
    for doc in all_docs:
        
        key = (doc['nome'], doc['email'], doc['telefone'], doc['data_nascimento'])
        if key in seen:
            duplicates.append(doc['_id']) 
        else:
            seen.add(key)
    
    
    if duplicates:
        collection.delete_many({'_id': {'$in': duplicates}})

def extracao(**kwargs):
    data_path = "/opt/airflow/estudos/Checkpoint5e6profTiago.csv"

    df = pd.read_csv(data_path)
    Cliente = MongoClient("mongodb://Coloque o Ip da sua máquina:27017") 
    db = Cliente["MeuBancoDeDados"]
    Colecao = db["pessoas"]

    
    remove_duplicates(Colecao)

    
    Colecao.create_index([('nome', 1), ('email', 1), ('telefone', 1), ('data_nascimento', 1)], unique=True)

    for record in df.to_dict(orient='records'):
        try:
            Colecao.insert_one(record)  
        except errors.DuplicateKeyError:
            print(f"Registro {record} já existe no banco de dados.")
    
    print("Processo de inserção concluído.")

default_args = {
    'owner': 'Victor',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 23),
    'email': ['example@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'Extracao', 
    default_args=default_args,  
    description='Extrai dados e envia para o Mongo',  
    schedule_interval=timedelta(days=1), 
    catchup=False,
) as dag:

    task1 = PythonOperator(
        task_id='executa_funcao', 
        python_callable=extracao,  
        provide_context=True 
    )

    task1
