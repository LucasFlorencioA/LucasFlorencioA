import flet as ft
from models.gerenciador import GerenciadorDeReservas
from models.quarto import Quarto
from views.tela_cliente import tela_cliente

def main(page: ft.Page):
    page.title = "Sistema de Reservas de Hotel"
    gerenciador = GerenciadorDeReservas()


    # Adiciona alguns quartos para exemplo
    gerenciador.adicionar_quarto(Quarto(101, "Standard", 100))
    gerenciador.adicionar_quarto(Quarto(102, "Deluxe", 150))
    gerenciador.adicionar_quarto(Quarto(103, "Deluxe", 200))
    gerenciador.adicionar_quarto(Quarto(104, "Deluxe", 250))
    gerenciador.adicionar_quarto(Quarto(105, "Deluxe", 300))
    gerenciador.adicionar_quarto(Quarto(106, "Deluxe", 350))

    
    # Exibe a tela principal
    tela_cliente(page, gerenciador)

ft.app(target=main) 