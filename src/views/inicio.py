import flet as ft

from views.ingrediente_view import IngredientesView
from views.listado_ordenes_view import ListadoOrdenesView
from views.orden_view import OrdenView
from views.producto_view import ProductosView

def inicio(page: ft.Page):
    page.title = "Pomodoro Rosso"
    page.window.width = 1200
    page.window.height = 800
    
    orden_view = OrdenView()
    listado_ordenes_view = ListadoOrdenesView()
    producto_view = ProductosView()
    ingrediente_view = IngredientesView(page)

    tabs = ft.Tabs(
        selected_index = 0,
        animation_duration = 300,
        tabs = [
            ft.Tab(text="Orden", content= orden_view),
            ft.Tab(text="Listado de órdenes", content= listado_ordenes_view),
            ft.Tab(text="Productos", content= producto_view),
            ft.Tab(text="Ingrediente", content=ingrediente_view)

        ],
        expand=True
    )

    page.add(tabs)


