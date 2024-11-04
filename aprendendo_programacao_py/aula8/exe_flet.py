import flet as ft


def main(page: ft.Page):
    page.Title = 'Minha primeira aplicação em Flet'
    page.add(
        ft.Text("Bem-vindo ao Flet!"),
        ft.ElevatedButton("Clique Aqui!",
                          on_click=lambda _: page.add(ft.Text('Botão Clicado!'))
        )
    )

ft.app(target=main)