from src.database.conexion import Conexion

def test_conexion_exitosa():
    conn = None
    try:
        conn = Conexion.get_connection()          # abre conexión real
        assert isinstance(conn.version, str)      # verifica que es una conexión válida
    except Exception as e:
        assert False, f"Falló la conexión: {e}"
    finally:
        if conn:
            conn.close()
            print("🔒 Conexión cerrada correctamente.")
