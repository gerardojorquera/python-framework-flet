import os
import flet as ft  # prueba con flet basado en flutter para python 123


# Forzar a Flutter a usar renderizado por software si es necesario
os.environ["FLUTTER_RENDERER"] = "software" 

async def main(page: ft.Page):
    page.title = "Flet (GUI)"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txtName = ft.TextField(label="Ingrese su nombre:", width=200)
    lblGreeting = ft.Text()

    def greet(e):
        lblGreeting.value = f"Hola, {txtName.value}!"
        page.update()

    page.add(
        txtName,
        ft.ElevatedButton("Saludar!", on_click=greet),
        lblGreeting
    )

if __name__ == "__main__":    
    ft.app(target=main)