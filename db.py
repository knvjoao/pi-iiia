import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()


def connect_to_db():
   conn = psycopg2.connect(
      dbname = "projeto_integrador3",
      user = os.getenv("db_user"),
      password = os.getenv("db_password"),
      host = os.getenv("db_host"),
      port = os.getenv("db_port")
   )
   return conn


def insert_post(title, post_link, categoria, conn):
    try:
        cur = conn.cursor()
        query = "INSERT INTO posts(title, post_link, categoria) VALUES (%s, %s, %s)"
        cur.execute(query, (title, post_link, categoria))
        print(f"'{title}' adicionado. (Pendente)")
    except psycopg2.Error as psyerror:
        print("Erro: ", psyerror)


def insert_filmes(title, category, conn):
    try:
        cur = conn.cursor()
        query = "INSERT INTO filmes(title, category) VALUES (%s, %s)"
        cur.execute(query, (title, category))
        print(f"Filme '{title}' inserido no banco de dados. (Pendente)")
    except psycopg2.Error as psyerror:
        print("Erro: ", psyerror)


def insert_series(title, category, conn):
    try:
        cur = conn.cursor()
        query = "INSERT INTO series(title, category) VALUES (%s, %s)"
        cur.execute(query, (title, category))
        print(f"Série '{title}' inserida no banco de dados. (Pendente)")
    except psycopg2.Error as psyerror:
        print("Erro: ", psyerror)


def confirmation(conn):
    answer = input("Deseja inserir os dados no banco de dados? s ou S para confirmar, qualquer outro input para revogar.").strip().lower()
    if answer == 's':
        conn.commit()
        print("Alterações confirmadas no banco de dados.")
    else:
        conn.rollback()
        print("Alterações desfeitas.")