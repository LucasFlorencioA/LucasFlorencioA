import flet as ft

def main(page: ft.Page):

    theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.BLUE,
            secondary=ft.colors.GREEN,
            background=ft.colors.WHITE,
            surface=ft.colors.GREY,
        )
    )


    page.title = 'Meu App'
    page.theme = theme
    page.add(
        ft.Text("Texto da aplicação", color='black'),
        ft.ElevatedButton("Meu botão", bgcolor='blue', color='white')
    )

ft.app(target=main)