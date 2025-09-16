import psycopg2
import os
from dotenv import load_dotenv
from contextlib import contextmanager

load_dotenv()

@contextmanager
def connection_db():
    """Context manager for database connections"""
    conn = None
    try:
        conn = psycopg2.connect(
            host=os.getenv("BD_HOST2"),
            port=os.getenv("BD_PORT2"),
            database=os.getenv("BD_NAME2"),
            user=os.getenv("BD_USER2"),
            password=os.getenv("BD_PASSWORD2")
        )
        yield conn
    except Exception as e:
        if conn:
            conn.rollback()
        raise e
    finally:
        if conn:
            conn.close()