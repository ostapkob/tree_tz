# https://confluence.atlassian.com/bitbucketserverkb/fatal-ident-authentication-failed-for-user-unable-to-connect-to-postgresql-779171564.html
# CREATE USER vladlink WITH PASSWORD 'vladlink' CREATEDB;

import psycopg2

def create_db():
    conn = psycopg2.connect(database="vladlink", user="vladlink",
                            password="vladlink1", host="127.0.0.1", port=5432)

    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, login, password FROM users")
            data = cur.fetchall()

    for row in data:
        print(row)


    conn.commit()
