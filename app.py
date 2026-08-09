import flet as ft  # prueba con flet basado en flutter para python 123

SIMULAR_MOVIL = True  # Cambia a False para probar en escritorio

async def main(page: ft.Page):
    page.title = "Flet (GUI)"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # --- AGREGA ESTAS LÍNEAS PARA SIMULAR UN MÓVIL ---
    if SIMULAR_MOVIL:
        page.window.width = 390   # Ancho promedio de un celular
        page.window.height = 844  # Alto promedio de un celular
        page.window.resizable = False # Evita que se deforme la prueba
    # -------------------------------------------------

    txtName = ft.TextField(label="Ingrese su nombre:", width=200, autofocus=True)
    lblGreeting = ft.Text()

    """
    def greet(e):
        if not txtName.value:
            lblGreeting.value = "Por favor, ingrese su nombre."
        else:
            lblGreeting.value = f"Hola, {txtName.value}!"
        page.update()
    """

    def greet(e):
        # Eliminamos espacios en blanco invisibles al inicio o final
        if not txtName.value.strip():
            txtName.error_text = "¡Este campo es obligatorio!" # Muestra alerta visual
            lblGreeting.value = "" # Limpia el saludo anterior si existía
            txtName.focus()        # <--- DEVUELVE EL FOCO AL TEXTO
            page.update()
            return # Detiene la ejecución aquí si está vacío

        # Si el texto es válido, limpia el error y saluda
        txtName.error_text = None 
        lblGreeting.value = f"Hola, {txtName.value}!"
        page.update()

    page.add(
        txtName,
        ft.ElevatedButton("Saludar!", on_click=greet),
        lblGreeting
    )

if __name__ == "__main__":    
    ft.app(target=main) # Escritorio
    # ft.app(target=main, view=ft.AppView.WEB_BROWSER)