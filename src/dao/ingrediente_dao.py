from database.conexion import Conexion
from models.ingrediente import Ingrediente
from typing import Optional

class IngredienteDAO:   
    @staticmethod
    def insertar(ingrediente: Ingrediente):
        conn = Conexion.get_connection()
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO INGREDIENTE VALUES (INGREDIENTE_SEQ.NEXTVAL, :1, :2)"
            valores = (ingrediente.nombre, ingrediente.unidad_medida)
            cursor.execute(sql, valores)
            conn.commit()
        except Exception as e:
            print(f"❌ No se pudo insertar el ingrediente: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    @staticmethod    
    def listar_todos() -> list[Ingrediente]:
        conn = Conexion.get_connection()
        try:
            cursor = conn.cursor()
            sql = "SELECT ID_INGREDIENTE, NOMBRE, UNIDAD_MEDIDA FROM INGREDIENTE"
            cursor.execute(sql)
            rows = cursor.fetchall()
            return [
                Ingrediente(id_ingrediente=row[0], nombre=row[1], unidad_medida=row[2])
                for row in rows
            ]
        except Exception as e:
            print(f"❌ Error al listar ingredientes: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def listar_por_id(id_ingrediente: int) -> Optional[Ingrediente]:
        conn = Conexion.get_connection()
        try:
            cursor = conn.cursor()
            sql = "SELECT ID_INGREDIENTE, NOMBRE, UNIDAD_MEDIDA FROM INGREDIENTE WHERE ID_INGREDIENTE = :1"
            cursor.execute(sql, (id_ingrediente,))
            row = cursor.fetchone()
            if row:
                return Ingrediente(id_ingrediente=row[0], nombre=row[1], unidad_medida=row[2])
            return None
        except Exception as e:
            print(f"❌ Error al buscar ingrediente por ID: {e}")
            return None
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def modificar(ingrediente: Ingrediente):
        conn = Conexion.get_connection()
        try:
            cursor = conn.cursor()
            sql = "UPDATE INGREDIENTE SET NOMBRE = :1, UNIDAD_MEDIDA = :2 WHERE ID_INGREDIENTE = :3"
            valores = (ingrediente.nombre, ingrediente.unidad_medida, ingrediente.id_ingrediente)
            cursor.execute(sql, valores)
            conn.commit()
        except Exception as e:
            print(f"❌ Error al modificar el ingrediente: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def eliminar(id_ingrediente: int):
        conn = Conexion.get_connection()
        try:
            cursor = conn.cursor()
            sql = "DELETE FROM INGREDIENTE WHERE ID_INGREDIENTE = :1"
            cursor.execute(sql, (id_ingrediente,))
            conn.commit()
        except Exception as e:
            print(f"❌ Error al eliminar el ingrediente: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
