import flet as ft


def main(page: ft.Page):

    cadastros = []


    nome = ft.TextField(label='Nome', width=300, color='blue', max_length=50)
    email = ft.TextField(label='E-mail', width=300, color='red', max_length=100)

    def enviar_formulario(e):
        if nome.value.strip() and email.value.strip():
            cadastros.append(
                {
                    'nome': nome.value,
                    'email': email.value,
                }

            )
        
        page.dialog = ft.AlertDialog(
            title = ft.Text('Cadastro Realizado!', color='green'),
            content= ft.Text('Cadastro Realizado!', color='green')
        )

        nome.value = ''
        email.value = ''
        page.update()

    def consultar_cadastro(e):
        if not cadastros:

            page.dialog = ft.AlertDialog(
                title = ft.Text('Nenhum cadastro encontrado.', color='red', weight=ft.FontWeight.BOLD),
                content= ft.Text('Não há cadastros para exibir.',color='red')
            )
        else:
            registros = '\n\n'.join(f'Nome: {c["nome"]}\nE-mail: {c["email"]}' for c in cadastros)
            page.dialog = ft.AlertDialog(
                title = ft.Text('Cadastros Realizados'),
                content = ft.Text(registros)
            )
        
        page.dialog.open = True
        page.update()


    enviar = ft.ElevatedButton('Enviar', on_click=enviar_formulario, bgcolor='green', color='white')
    consultar = ft.ElevatedButton('Consultar', on_click=consultar_cadastro, bgcolor='blue', color='white')


    page.add(

        ft.Column(
            [  
                nome,
                email,
                enviar,
                consultar
            ],
            alignment= ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER
        )

    )

ft.app(target=main)