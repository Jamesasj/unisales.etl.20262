## LOAD stage.rent_usuarios > dw.d_user
import psycopg2

conn = psycopg2.connect(
    dbname="dw",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

cur.execute("""
INSERT INTO dw.d_user (nome, email, source_id, tp_user)
SELECT nome, email, 'rent#'||id, 'rent'
FROM stage.rent_usuarios
union
SELECT nome, email, 'sold#'||id, 'sold'
FROM stage.sold_usuarios
""")

conn.commit()
cur.close()
conn.close()
