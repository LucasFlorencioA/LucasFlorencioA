import flet as ft

def main(page: ft.Page):
    page.title = 'Conversor de Temperatura'

    tema = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary= ft.colors.INDIGO,
            secondary=ft.colors.RED,
            background=ft.colors.WHITE,
            on_background=ft.colors.BLACK,
            on_primary=ft.colors.WHITE, 
        )
    )

    page.theme = tema
    page.bgcolor = page.theme.color_scheme.background
    page.padding = 20


    campo_entrada = ft.TextField(
       label = 'Digite a Temperatura: ',
       border_color=page.theme.color_scheme.primary,
       text_style=ft.TextStyle(size=18),
       width = 400,
       color=page.theme.color_scheme.secondary
    )

    campo_select_box = ft.Dropdown(
       label='Converter para...',
       options=[
            ft.dropdown.Option('Celsius -> Farenheit'),
            ft.dropdown.Option('Farenheit -> Celsius')
       ],
       width=400,
       color=page.theme.color_scheme.secondary
    )

    resultado_texto = ft.Text(
        "",
        color=page.theme.color_scheme.on_background,
        size = 22,
        weight="bold"
    )


    def converter_temperatura(e):
        temperatura = float(campo_entrada.value)
        unidade = campo_select_box.value

        if unidade == 'Celsius -> Farenheit':
            resultado = (temperatura * 9/5) + 32
            resultado_texto.value = f'{temperatura} C = {round(resultado,2)} F'
        elif unidade == 'Farenheit -> Celsius':
            resultado = (temperatura - 32) * 5/9
            resultado_texto.value = f'{temperatura} F = {round(resultado,2)} C'
        else:
            resultado_texto.value = 'Por favor, selecione uma conversão.'

        page.update()

    botao = ft.ElevatedButton(
        text='Converter',
        color=page.theme.color_scheme.on_primary,
        bgcolor= page.theme.color_scheme.primary,
        style=ft.ButtonStyle(
            text_style=ft.TextStyle(size=18)
        ),
        on_click=converter_temperatura
    )

    page.add(campo_entrada, campo_select_box, botao ,resultado_texto)

ft.app(target=main)