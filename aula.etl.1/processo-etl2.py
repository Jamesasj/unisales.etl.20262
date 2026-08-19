import psycopg2
import os

# fazendo extract em banco de dados PostgreSQL

conexao = psycopg2.connect(
	host=os.getenv("PGHOST", "localhost"),
	port=os.getenv("PGPORT", "5432"),
	database=os.getenv("PGDATABASE", "postgres"),
	user=os.getenv("PGUSER", "postgres"),
	password=os.getenv("PGPASSWORD", "postgres"),
)

cursor = conexao.cursor()
cursor.execute("SELECT * FROM usuarios where data_cadastro >= '2026-06-1'")
resultado = cursor.fetchall()

print("Resultado da consulta:")
for linha in resultado:
    print(linha)


conexao.close()
