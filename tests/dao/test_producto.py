import pytest
from src.models.producto import Producto
from src.dao.producto_dao import ProductoDAO

def test_insertar_producto():
    producto = Producto(nombre="Pascualina",precio=200)

    try:
        ProductoDAO.insertar(producto)
        productos = ProductoDAO.listar_todos()
        nombres = [p.nombre for p in productos]

        assert "Pascualina" in nombres

        for pro in productos:
            if pro.nombre == "Pascualina":
                ProductoDAO.eliminar(pro.id_producto)
    except Exception as e:
        pytest.fail(f"Fallo al insertar producto: {e}")
def test_eliminar_producto():
    producto = Producto(nombre="EliminarTest",precio=100)
    ProductoDAO.insertar(producto)

    productos = ProductoDAO.listar_todos()
    producto_insertado = next((p for p in productos if p.nombre == "EliminarTest"), None)

    assert producto_insertado is not None,"No se insertó el producto para eliminar"
    ProductoDAO.eliminar(producto_insertado.id_producto)

    producto_buscado = ProductoDAO.listar_por_id(producto_insertado.id_producto)
    assert producto_buscado is None, "El producto no fue eliminado correctamente"
def test_modificar_ingrediente():
    producto = Producto(nombre="ModificarTest", precio= 100)
    ProductoDAO.insertar(producto)

    productos = ProductoDAO.listar_todos()
    producto_original = next((p for p in productos if p.nombre == "ModificarTest"),None)
    assert producto_original is not None,"No se encontró el ingrediente para modificar"

    producto_original.nombre = "Modificado"
    producto_original.precio = 200
    ProductoDAO.modificar(producto_original)

    producto_modificado = ProductoDAO.listar_por_id(producto_original.id_producto)
    assert producto_modificado is not None
    assert producto_modificado.nombre == "Modificado"
    assert producto_modificado.precio == 200
    ProductoDAO.eliminar(producto_original.id_producto)


