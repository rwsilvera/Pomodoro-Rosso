import flet as ft

def ProductosView():
    return ft.Column([
        ft.Text("Gestión de Productos", size=30, weight=ft.FontWeight.BOLD),
        ft.Text("🍕 Próximamente podrás gestionar tus productos aquí.", size=18, italic=True),
    ])
