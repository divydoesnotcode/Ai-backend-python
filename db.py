import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="ai_python",
        user="postgres",
        password="asdfghjkl"
    )
    return conn

    