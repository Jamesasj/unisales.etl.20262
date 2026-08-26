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
insert into dw.d_filmes (titulo, ano_lancamento, source_id, imdb_rating, imdb_url)
select  titulo, ano_lancamento, 'rent#'||id_filme, imdb_rating, url
from stage.rent_filmes rf
left join stage.imdb_ratings ir on trim(upper(rf.titulo)) = trim(upper(ir.titulo))
""")

conn.commit()
cur.close()
conn.close()