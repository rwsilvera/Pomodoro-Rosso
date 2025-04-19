import pytest
from src.models.ingrediente import Ingrediente
from src.dao.ingrediente_dao import IngredienteDAO

def test_insertar_ingrediente():
    ingrediente = Ingrediente(nombre="Masa",unidad_medida="Kilogramos")

    try:
        IngredienteDAO.insertar(ingrediente)
        ingredientes = IngredienteDAO.listar_todos()
        nombres = [i.nombre for i in ingredientes]

        assert "Masa" in nombres
        
        for ing in ingredientes:
            if ing.nombre == "Masa":
                IngredienteDAO.eliminar(ing.id_ingrediente)

    except Exception as e:
        pytest.fail(f"Fallo al insertar ingrediente: {e}")

def test_eliminar_ingrediente():

    ingrediente = Ingrediente(nombre="EliminarTest", unidad_medida="Litros")
    IngredienteDAO.insertar(ingrediente)


    ingredientes = IngredienteDAO.listar_todos()
    ingrediente_insertado = next((i for i in ingredientes if i.nombre == "EliminarTest"), None)

    assert ingrediente_insertado is not None, "No se insertó el ingrediente para eliminar"


    IngredienteDAO.eliminar(ingrediente_insertado.id_ingrediente)


    ingrediente_buscado = IngredienteDAO.listar_por_id(ingrediente_insertado.id_ingrediente)
    assert ingrediente_buscado is None, "El ingrediente no fue eliminado correctamente"
def test_modificar_ingrediente():
    # Paso 1: Insertar un ingrediente de prueba
    ingrediente = Ingrediente(nombre="ModificarTest", unidad_medida="Gramos")
    IngredienteDAO.insertar(ingrediente)

    # Paso 2: Obtener el ingrediente recién insertado
    ingredientes = IngredienteDAO.listar_todos()
    ingrediente_original = next((i for i in ingredientes if i.nombre == "ModificarTest"), None)

    assert ingrediente_original is not None, "No se encontró el ingrediente para modificar"

    # Paso 3: Modificar el ingrediente
    ingrediente_original.nombre = "Modificado"
    ingrediente_original.unidad_medida = "Kilos"
    IngredienteDAO.modificar(ingrediente_original)

    # Paso 4: Verificar que los cambios se aplicaron
    ingrediente_modificado = IngredienteDAO.listar_por_id(ingrediente_original.id_ingrediente)

    assert ingrediente_modificado is not None
    assert ingrediente_modificado.nombre == "Modificado"
    assert ingrediente_modificado.unidad_medida == "Kilos"

    # Paso 5: Eliminar el ingrediente para limpiar la base
    IngredienteDAO.eliminar(ingrediente_original.id_ingrediente)   