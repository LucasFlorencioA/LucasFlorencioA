import flet as ft




def main(page: ft.Page):

    style = ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE | ft.TextDecoration.OVERLINE)
    
    page.title = 'Minha Aplicação'
    
    texto_1 = ft.Text(
        'Água mole, pedra dura, tanto bate até que fura.',
        color='blue',
        size=30,
        weight=ft.FontWeight.BOLD
    )

    texto_2 = ft.Text(
        'O rato roeu a roupa do rei de roma.',
        color='red',
        size=20,
        weight=ft.TextDecoration.UNDERLINE
    )

    texto_3 = ft.Text(
        color='orange',
        size=20,
        weight=ft.FontWeight.BOLD,
        spans= [ft.TextSpan(
                    'Vi vovó atrás do trem.',
                    ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
    
                )
        ]
    )
    

    page.add(
        texto_1, texto_2, texto_3
    )


ft.app(target=main)