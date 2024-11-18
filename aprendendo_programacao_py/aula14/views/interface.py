import flet as ft
from models.gerenciador import GerenciadorDeReservas
from models.quarto import Quarto
from models.cliente import Cliente

def tela_cliente(page: ft.Page, gerenciador: GerenciadorDeReservas):
    page.title = "Sistema de Reservas de Hotel - Cliente"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 20

    lista_quartos = ft.Column()
    formulario = ft.Column(visible=False)
    mensagem_confirmacao = ft.Text("", visible=False, color="green")

    def mostrar_quartos_disponiveis(e):
        """Função para exibir os quartos disponíveis."""
        lista_quartos.controls.clear()
        quartos_disponiveis = gerenciador.verificar_disponibilidade(None, None)
        
        if not quartos_disponiveis:
            lista_quartos.controls.append(ft.Text("Nenhum quarto disponível no momento.", color="red"))
        else:
            for quarto in quartos_disponiveis:
                quarto_texto = f"Quarto {quarto.numero} - Tipo: {quarto.tipo} - Preço: {quarto.preco}"
                botao_reserva = ft.ElevatedButton(
                    text="Reservar",
                    on_click=lambda e, q=quarto: mostrar_formulario_reserva(q)
                )
                lista_quartos.controls.append(ft.Row([ft.Text(quarto_texto), botao_reserva]))
        
        lista_quartos.update()

    def mostrar_formulario_reserva(quarto):
        """Exibe o formulário de reserva para o quarto selecionado."""
        formulario.controls.clear()
        
        nome_input = ft.TextField(hint_text="Nome", width=300)
        email_input = ft.TextField(hint_text="Email", width=300)
        telefone_input = ft.TextField(hint_text="Telefone", width=300)
        date_checkin_input = ft.TextField(hint_text="Check In", width=300)
        date_checkout_input = ft.TextField(hint_text="Check Out", width=300)
    
        
        def confirmar_reserva(e):
            """Confirma a reserva para o cliente e exibe uma mensagem de confirmação."""
            cliente = Cliente(nome_input.value, email_input.value, telefone_input.value)
            reserva = gerenciador.criar_reserva(
                cliente, 
                quarto, 
                date_checkin_input.value,
                date_checkout_input.value
            )
            
            if reserva:
                mensagem_confirmacao.value = "Reserva confirmada!"
                mensagem_confirmacao.visible = True
                formulario.visible = False
                lista_quartos.controls.clear()
                mostrar_quartos_disponiveis(None)
            else:
                mensagem_confirmacao.value = "Erro ao confirmar a reserva. Verifique os dados e tente novamente."
                mensagem_confirmacao.color = "red"
                mensagem_confirmacao.visible = True

            mensagem_confirmacao.update()
            formulario.update()

        # Adiciona os campos ao formulário
        formulario.controls.extend([
            ft.Text(f"Reserva para Quarto {quarto.numero} - {quarto.tipo}"),
            nome_input,
            email_input,
            telefone_input,
            date_checkin_input,
            date_checkout_input,
            ft.ElevatedButton(text="Confirmar Reserva", on_click=confirmar_reserva)
        ])
        formulario.visible = True
        formulario.update()

    # Carregar a lista de quartos disponíveis na inicialização
    page.add(
        ft.Text("Quartos Disponíveis para Reserva", size=20, weight="bold"),
        lista_quartos,
        ft.ElevatedButton(text="Verificar Quartos Disponíveis", on_click=mostrar_quartos_disponiveis),
        ft.Divider(),
        formulario,
        mensagem_confirmacao
    )

    mostrar_quartos_disponiveis(None)  # Exibe os quartos disponíveis ao carregar a interface
