import psycopg2
import os
from dotenv import load_dotenv


load_dotenv()

def connection():
    return psycopg2.connect(
        host=os.getenv("BD_HOST2"),
        port=os.getenv("BD_PORT2"),
        database=os.getenv("BD_NAME2"),
        user=os.getenv("BD_USER2"),
        password=os.getenv("BD_PASSWORD2")
    )

