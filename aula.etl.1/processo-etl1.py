import requests

# Data acquisition (APIS)
res = requests.get('https://jsonplaceholder.typicode.com/users')
users = res.json()

# SQLs

# ARQUIVOS (CSV, JSON, XML, TXT)

# WebScrapping

## TRANFORM - removendo os dados desnecessários e deixando apenas os dados que serão utilizados
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