import flet as ft
from dao.ingrediente_dao import IngredienteDAO
from models.ingrediente import Ingrediente
from components.dialogo_confirmacion_component import DialogoConfirmacion

def IngredientesView(page: ft.Page):
    input_nombre = ft.TextField(label="Nombre del ingrediente", expand=True)
    input_unidad = ft.TextField(label="Unidad de medida", expand=True)
    boton_agregar = ft.ElevatedButton("Agregar", on_click=lambda e: agregar_o_modificar_ingrediente())
    boton_cancelar = ft.ElevatedButton("Cancelar", visible=False, on_click=lambda e: cancelar_edicion())

    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Unidad de Medida")),
            ft.DataColumn(ft.Text("Acciones")),
        ],
        rows=[],
        expand=True,
    )

    tabla_scroll = ft.Container(
        content=ft.Column([
            ft.Container(
                content=tabla,
                expand=True,
            )
        ], scroll=ft.ScrollMode.ADAPTIVE),
        expand=True,
        padding=ft.padding.only(top=10),
        alignment=ft.alignment.center,
    )

    snack = ft.SnackBar(content=ft.Text(""), open=False)
    page.snack_bar = snack

    dialogo = DialogoConfirmacion(page)
    ingrediente_en_edicion = {"id": None}  # Para rastrear si estamos editando

    def cargar_ingredientes():
        tabla.rows.clear()
        for ing in IngredienteDAO.listar_todos():
            tabla.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(ing.nombre)),
                        ft.DataCell(
                            ft.Text(
                                ing.unidad_medida,
                                text_align=ft.TextAlign.CENTER,
                            )
                        ),
                        ft.DataCell(
                            ft.Row(
                                [
                                    ft.IconButton(
                                        icon=ft.icons.CREATE,
                                        tooltip="Editar",
                                        icon_color=ft.colors.BLUE_300,
                                        on_click=lambda e, i=ing: editar_ingrediente(i),
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.DELETE,
                                        tooltip="Eliminar",
                                        icon_color=ft.colors.RED_400,
                                        on_click=lambda e, i=ing: preguntar_eliminar(i),
                                    ),
                                ]
                            )
                        ),
                    ]
                )
            )

    def editar_ingrediente(ingrediente: Ingrediente):
        input_nombre.value = ingrediente.nombre
        input_unidad.value = ingrediente.unidad_medida
        ingrediente_en_edicion["id"] = ingrediente.id_ingrediente
        boton_agregar.text = "Guardar cambios"
        boton_cancelar.visible = True
        page.update()

    def cancelar_edicion():
        input_nombre.value = ""
        input_unidad.value = ""
        ingrediente_en_edicion["id"] = None
        boton_agregar.text = "Agregar"
        boton_cancelar.visible = False
        page.update()

    def preguntar_eliminar(ingrediente: Ingrediente):
        dialogo.mostrar(
            mensaje=f"¿Deseás eliminar el ingrediente '{ingrediente.nombre}'?",
            on_confirmar=lambda: confirmar_eliminar(ingrediente.id_ingrediente, ingrediente.nombre)
        )

    def confirmar_eliminar(id_ingrediente: int, nombre: str):
        IngredienteDAO.eliminar(id_ingrediente)
        cargar_ingredientes()
        snack.content = ft.Text(f"🗑️ Ingrediente eliminado: {nombre}")
        snack.open = True
        page.snack_bar = snack
        page.update()

    def agregar_o_modificar_ingrediente():
        nombre = input_nombre.value.strip()
        unidad = input_unidad.value.strip()
        if not nombre or not unidad:
            return

        if ingrediente_en_edicion["id"] is None:
            IngredienteDAO.insertar(Ingrediente(nombre=nombre, unidad_medida=unidad))
            snack.content = ft.Text(f"✅ Ingrediente agregado: {nombre}")
        else:
            IngredienteDAO.modificar(
                Ingrediente(
                    id_ingrediente=ingrediente_en_edicion["id"],
                    nombre=nombre,
                    unidad_medida=unidad
                )
            )
            snack.content = ft.Text(f"✏️ Ingrediente modificado: {nombre}")
            boton_agregar.text = "Agregar"
            ingrediente_en_edicion["id"] = None
            boton_cancelar.visible = False

        input_nombre.value = ""
        input_unidad.value = ""
        cargar_ingredientes()
        snack.open = True
        page.snack_bar = snack
        page.update()

    layout = ft.Column(
        [
            ft.Text("Listado de Ingredientes", size=30, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
            ft.Divider(),
            ft.Row([
                input_nombre,
                input_unidad,
                boton_agregar,
                boton_cancelar,
            ], alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(),
            tabla_scroll,
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER
    )

    cargar_ingredientes()
    return layout