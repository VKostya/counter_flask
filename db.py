import psycopg2


def get_db_connection():
    conn = psycopg2.connect(
        host="db", database="counterdb", user="flask", password="flask"
    )
    return conn


def init_table_in_db():
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "CREATE TABLE IF NOT EXISTS counter (id serial PRIMARY KEY, date varchar, user_agent varchar);"
        )
        print("table inited")
        conn.commit()
    except:
        print("table init error")
    cur.close()
    conn.close()
