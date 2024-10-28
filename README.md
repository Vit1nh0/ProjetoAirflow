# ProjetoAirflow

Projeto utilizando Airflow e MongoDB

# Meu Projeto de ETL com Airflow e MongoDB

Este projeto configura um ambiente Docker para o Apache Airflow e insere dados em um MongoDB usando uma DAG.

## Estrutura do Projeto

- `dags/`: Contém os arquivos de DAG do Airflow.
- `data/`: Contém arquivos de entrada, como CSV.
- `logs/`: Armazena os logs gerados pelo Airflow.
- `Dockerfile`: Arquivo para construir a imagem do Docker.
- `docker-compose.yml`: Arquivo para orquestrar os serviços com Docker.
- `requirements.txt`: Lista de dependências do projeto.
- `MongoDB`: Foi utilizado localmente na máquina

## Como Executar o Projeto

1. Clone o repositório
 ```
git clone https://github.com/Vit1nh0/ProjetoAirflow
```
2. Navegue até o diretório do projeto.
3. Execute o seguinte comando para iniciar os serviços.
 ```
docker-compose up
```
4. Acesse o Airflow na URL `http://localhost:8080`.

## Dependências

- Apache Airflow
- Pandas
- PyMongo
- Psycopg2-binary

## Observação

**Caso já possua o Mongo instalado e deseja rodar os códigos na sua máquina é necessario verificar o arquivo mongod.conf e trocar a bindIp: 0.0.0.0, pois a conexão com o mongo ao ser feita de forma local pode dar erro de acesso negado se não estiver alterada**
 
