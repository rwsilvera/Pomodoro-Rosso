import flet as ft

class DialogoConfirmacion:
    def __init__(self, page: ft.Page):
        self.page = page
        self.dialogo = None

    def mostrar(self, mensaje: str, on_confirmar, on_cancelar=None):
        print("🧪 Mostrando diálogo de confirmación...")

        self.dialogo = ft.AlertDialog(
            modal=True,
            title=ft.Text("Confirmación"),
            content=ft.Text(mensaje),
            actions=[
                ft.TextButton("Cancelar", on_click=lambda e: self.cancelar(on_cancelar)),
                ft.ElevatedButton("Eliminar", bgcolor=ft.colors.RED, on_click=lambda e: self.confirmar(on_confirmar)),
            ],
            actions_alignment="end",
            shape=ft.RoundedRectangleBorder(radius=10)
        )

        # Para versiones sin page.dialog
        if self.dialogo not in self.page.overlay:
            self.page.overlay.append(self.dialogo)

        self.dialogo.open = True
        self.page.update()

    def confirmar(self, on_confirmar):
        self.dialogo.open = False
        self.page.update()
        if on_confirmar:
            on_confirmar()

    def cancelar(self, on_cancelar):
        self.dialogo.open = False
        self.page.update()
        if on_cancelar:
            on_cancelar()
