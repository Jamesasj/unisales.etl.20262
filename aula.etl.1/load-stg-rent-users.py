import requests

# Data acquisition (APIS)
res = requests.get('https://jsonplaceholder.typicode.com/users')
users = res.json()

# SQLs

# ARQUIVOS (CSV, JSON, XML, TXT)

# WebScrapping

## EXTRACT
lista = []
for obj in users:
    lista.append({
        'name': obj['name'],
        'email': obj['email'],
        'city': obj['address']['city'],
        'company': obj['company']['name']
    })

## LOAD - carregando os dados no arquivo csv
file = open('users.csv', 'w')
for obj in lista:
    file.write(f"{obj['name']}, {obj['email']}, {obj['city']}, {obj['company']}\n")

file.close()


## LOAD STAGE - carregando no banco de dados DADO EM RAW
## database: dw, schema: stage, table: rent_usuarios
## postgreSQL connection and insertion
import psycopg2

conn = psycopg2.connect(
    dbname="dw",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()
i=0

for obj in lista:
    i += 1
    cur.execute(
        "INSERT INTO stage.rent_usuarios (id,nome, email, senha, data_cadastro) VALUES (%s, %s, %s, %s, %s)",
        (i, obj['name'], obj['email'], 'default_password', '2024-01-01')
    )

conn.commit()
cur.close()
conn.close()

# PARQUET