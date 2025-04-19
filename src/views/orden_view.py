import flet as ft

def OrdenView():
    return ft.Column([
        ft.Text("Gestión de Órdenes", size=30, weight=ft.FontWeight.BOLD),
        ft.Text("📝 Próximamente podrás registrar y administrar órdenes aquí.", size=18, italic=True),
    ])
    