import os
from dotenv import load_dotenv
import cx_Oracle

load_dotenv()

class Conexion:
    @staticmethod
    def get_connection():
        user = os.getenv("DB_USER")
        pwd  = os.getenv("DB_PASSWORD")
        dsn  = os.getenv("DB_DSN")
        print(user,pwd,dsn)

        try:
            conn = cx_Oracle.connect(user, pwd, dsn)
            print("🔗 Conexión a Oracle establecida.")
            return conn
        except cx_Oracle.Error as e:
            raise RuntimeError(f"Error conectando a Oracle: {e}")