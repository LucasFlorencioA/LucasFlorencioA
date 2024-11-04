import flet as ft

def main(page: ft.Page):

    #Inicializa lista de cadastros
    cadastros = []

    #Definir os campos de cadastro de cada usuário
    nome = ft.TextField(label='Nome', width=300, max_length=50)
    sobrenome = ft.TextField(label='Sobrenome', width=300, max_length=70)
    cpf = ft.TextField(label='CPF', width=300, max_length=13)
    email = ft.TextField(label='E-mail', width=300, max_length=100)
    telefone = ft.TextField(label='Telefone', width=300, max_length=20)
    data_nascimento = ft.TextField(label='Data de Nascimento', width=300, max_length=15)

    print(nome)

    # Função que irá armazenar o cadastro do usuário ao se clicar no botão "Enviar"
    def enviar_formulario(e):
        if nome.value.strip() and sobrenome.value.strip() and email.value.strip():
            #Adicionando cadastro à lista
            cadastros.append(
                {
                    'nome': nome.value,
                    'sobrenome': sobrenome.value,
                    'email': email.value,
                    'cpf': cpf.value,
                    'telefone': telefone.value,
                    'data_nascimento': data_nascimento.value
                }
            )

            nome.value = ''
            sobrenome.value = ''
            email.value = ''
            telefone.value = ''
            data_nascimento.value = ''
            cpf.value = ''
            page.update()

    # Consulta cadastros realizados
    def consultar_cadastros(e):
        if not cadastros:

            page.dialog = ft.AlertDialog(
                title= ft.Text('Nenhum cadastro encontrado.'),
                content= ft.Text('Não há cadastros para exibir.')
            )
        else:
            #Exibir cadastros
            registros = "\n\n".join(f"Nome: {c['nome']}\nSobrenome: {c['sobrenome']}\nE-mail: {c['email']}\nTelefone: {c['telefone']}\nCPF: {c['cpf']}\n Data de Nascimento: {c['data_nascimento']}" for c in cadastros)
            page.dialog = ft.AlertDialog(
                title = ft.Text('Cadastros Realizados'),
                content = ft.Text(registros)
            )
        page.dialog.open = True
        page.update()

        #criar botões de interação
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_formulario)
    botao_consultar = ft.ElevatedButton('Consultar Cadastros', on_click=consultar_cadastros)

    #Definindo Layout da aplicação
    page.add(
        ft.Column(
            [
                nome,
                sobrenome,
                telefone,
                data_nascimento,
                email,
                cpf,
                botao_enviar,
                botao_consultar
            ],
            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER
        )
)


#Executando aplicação
ft.app(target=main)