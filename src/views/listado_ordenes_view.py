import flet as ft

def ListadoOrdenesView():
    return ft.Column([
        ft.Text("Listado de órdenes", size=30, weight=ft.FontWeight.BOLD),
        ft.Text("📦 Próximamente verás aquí todas las órdenes generadas.", size=18, italic=True),
    ])