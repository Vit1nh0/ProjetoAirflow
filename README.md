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
 
3. Faça as devidas alterações nos caminhos dos arquivos nos arquivos docker-compose e na dag. Na dag é necessário substituir o espaço informado pelo IP do seu computador pois a conexão com o mongo é feita de forma local. E no Comopose e necessário verificar se o caminho para o CSV esta configurado

4. Após todas as alterações execute o seguinte comando para iniciar os serviços.
 ```
docker-compose up
```
5. Acesse o Airflow na URL `http://localhost:8080`. Se tudo estiver certo o site estara em Pé, se for solicitado senha e usuario utilize Airflow e Airflow respectivamente.

6. Neste passo é necessário instalar o mongoDB o Mongo Compass e o MongoDB shell

7. Após instalação execute como admin o CMD e utilize os seguintes comandos (navegue até a pasta onde foi instalado o mongo e vá até a pasta bin).
```
mongod
```
Vá ate a pasta onde foi instalado o mongosh vá até a bin e execute
```
mongosh
```
8. Para criação do banco execute
```
use "Coloque o nome do seu banco de dados"
```
9. Verifique se foi criado. Se aparecer o seu banco de dados tudo correu bem.
```
db
```
10. Faça a inserção de dados para que de fato seja criado
```
db.Nome_da_sua_coleção.insertOne({ nome: "exemplo", valor: 123 })
```
11. Altere o nome da coleção na Dag para que tudo ocorra certo.
   
12. Utilize a Dag no Airflow
   
13. Verifique se foi inserido no Compass 

## Dependências

- Apache Airflow
- Pandas
- PyMongo
- Psycopg2-binary

## Observação

**Caso já possua o Mongo instalado e deseja rodar os códigos na sua máquina é necessario verificar o arquivo mongod.conf e trocar a bindIp: 0.0.0.0, pois a conexão com o mongo ao ser feita de forma local pode dar erro de acesso negado se não estiver alterada**
 
