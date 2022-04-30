# https://confluence.atlassian.com/bitbucketserverkb/fatal-ident-authentication-failed-for-user-unable-to-connect-to-postgresql-779171564.html
# CREATE USER vladlink WITH PASSWORD 'vladlink' CREATEDB;
from rich import print
import psycopg2


def connect():
    conn = psycopg2.connect(database="vladlink", user="vladlink",
                            password="vladlink1", host="127.0.0.1", port=5432)
    return conn


def create_table():
    conn = connect()
    query = " ".join([
        "CREATE TABLE menu",
        "(id  BIGSERIAL NOT NULL PRIMARY KEY,",
        "parent SMALLINT NOT NULL,",
        "alias VARCHAR(64) NOT NULL,",
        "name VARCHAR(64) NOT NULL,",
        "level SMALLINT NOT NULL",
        ");"
    ])
    with conn:
        with conn.cursor() as cur:
            cur.execute(query)
    conn.commit()
    print(f'[orchid]{query}[/orchid]')


def drop_table():
    conn = connect()
    query = "DROP TABLE IF EXISTS menu"
    with conn:
        with conn.cursor() as cur:
            cur.execute(query)
    conn.commit()
    print(f'[orchid]{query}[/orchid]')


def insert_items(items):
    conn = connect()
    query = " ".join([
        "INSERT INTO menu",
        "(id, parent, alias, name, level)",
        "VALUES (%s, %s, %s, %s, %s)"
    ])
    with conn:
        with conn.cursor() as cur:
            for item in items:
                cur.execute(query, item)
    conn.commit()
    print(f'[orchid]{query}[/orchid]')


def select_items(deep=100):
    if deep<1:
        print("[red1]deep can't be less than 1[/red1]")
        return
    conn = connect()
    query = f"SELECT id, parent, alias, name, level  FROM menu WHERE level<={deep}"
    with conn:
        with conn.cursor() as cur:
            cur.execute(query)
            data = cur.fetchall()
    conn.commit()
    print(f'[orchid]{query}[/orchid]')
    return data
