import flet as ft

def main(page: ft.Page):

    numero = ft.TextField("Digite um número: ",max_length=2)

    def adicionar_numero(e):
        numero.value = int(numero.value)+1
        numero.value = str(numero.value)
        page.update()

    def subtrair_numero(e):
        numero.value = int(numero.value)-1
        numero.value = str(numero.value)
        page.update()  

      
    botao_somar = ft.ElevatedButton("+", on_click=adicionar_numero)
    botao_subtrair =ft.ElevatedButton("-", on_click=subtrair_numero)

    page.add(
        ft.Row(
            [
            numero,
            botao_somar,
            botao_subtrair,
            ],
            alignment= ft.MainAxisAlignment.CENTER
            
        ))


ft.app(target=main)           