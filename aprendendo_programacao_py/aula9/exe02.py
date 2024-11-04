import flet as ft

def main(page: ft.Page):
    # Inicializa o valor do contador
    counter = ft.TextField("0",width=100, text_align=ft.TextAlign.RIGHT)

    # Função para incrementar
    def increment(e):
        counter.value = int(counter.value)
        counter.value += 1
        counter.value = str(counter.value)
        page.update()

    # Função para decrementar
    def decrement(e):
        counter.value = int(counter.value)
        counter.value -= 1
        counter.value = str(counter.value)
        page.update()
    # Criação dos componentes da interface
    
    increment_button = ft.ElevatedButton(text="+", on_click=increment)
    decrement_button = ft.ElevatedButton(text="-", on_click=decrement)

    # Adiciona os componentes ao layout da página
    page.add(counter, ft.Row([increment_button, decrement_button], alignment=ft.MainAxisAlignment.CENTER))

# Executa a aplicação
ft.app(target=main)