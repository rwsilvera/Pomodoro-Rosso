from src.database.conexion import Conexion
from src.models.producto import Producto
from typing import Optional

class ProductoDAO:
    @staticmethod
    def insertar(producto:Producto):
        conn = Conexion.get_connection()
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO PRODUCTO VALUES(PRODUCTO_SEQ.NEXTVAL, :1, :2)"
            valores = (producto.nombre,producto.precio)
            cursor.execute(sql,valores)
            conn.commit()
        except Exception as e:
             print(f"❌ No se pudo insertar el producto: {e}")
             conn.rollback()
        finally:
            cursor.close()
            conn.close()     

    @staticmethod
    def listar_todos() -> list[Producto]:
        conn = Conexion.get_connection()
        try:
            cursor = conn.cursor()
            sql = "SELECT ID_PRODUCTO, NOMBRE, PRECIO FROM PRODUCTO"
            cursor.execute(sql)
            rows = cursor.fetchall()
            return [
                Producto(id_producto=row[0],nombre=row[1],precio=row[2])
                for row in rows
            ]
        except Exception as e:
            print(f"❌ Error al listar productos: {e}")
            return[]
        finally:
            cursor.close()
            conn.close()
    @staticmethod
    def listar_por_id(id_producto : int) -> Optional[Producto]:
        conn = Conexion.get_connection()
        try:
            cursor = conn.cursor()
            sql = "SELECT ID_PRODUCTO,NOMBRE,PRECIO FROM PRODUCTO WHERE ID_PRODUCTO = :1"
            cursor.execute(sql,(id_producto,))
            row = cursor.fetchone()
            if row:
                return Producto(id_producto=row[0],nombre=row[1],precio=row[2])
            return None
        except Exception as e:
           print(f"❌ Error al buscar producto por ID: {e}")
           return None
        finally:
            cursor.close()
            conn.close()
    @staticmethod
    def modificar(producto:Producto):
        conn = Conexion.get_connection()
        try:
            cursor = conn.cursor()
            sql = "UPDATE PRODUCTO SET NOMBRE = :1,PRECIO = :2 WHERE ID_PRODUCTO = :3"
            valores = (producto.nombre,producto.precio,producto.id_producto,)
            cursor.execute(sql,valores)
            conn.commit()
        except Exception as e:
               print(f"❌ Error al modificar el producto: {e}") 
               conn.rollback()
        finally:
            cursor.close()
            conn.close()
    @staticmethod
    def eliminar(id_producto: int):
        conn = Conexion.get_connection()
        try:
            cursor = conn.cursor()
            sql = "DELETE FROM PRODUCTO WHERE ID_PRODUCTO = :1"
            cursor.execute(sql,(id_producto,))
            conn.commit()
        except Exception as e:
            print(f"❌ Error al eliminar el producto: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
    
