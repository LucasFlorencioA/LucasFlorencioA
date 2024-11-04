# Menu do Usuário

from conexao import *

while True:
    print('''

=============== MENU ===================
          1 - CADASTRAR USUÁRIO
          2 - LISTAR USUÁRIOS
          3 - ATUALIZAR USUÁRIOS
          4 - DELETAR USUÁRIOS
          5 - SAIR      

''')
    opcao = input('Digite a Opção Desejada: ')

    if opcao == '1':
        nome = input('Digite seu nome: ')
        email = input('Digite seu e-mail: ')
        cadastrarUsuario(nome, email)

    elif opcao == '2':
        tabela = input('Digite o nome da tabela que deseja visualizar: ')
        print(listarUsuarios(tabela))

    elif opcao == '5':
        print('Saindo da aplicação...')
        break



# Conexão com SQLITE3

import sqlite3

conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

def cadastrarUsuario(nome, email):

    try:
        #Criando a tabela no banco de dados
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT NOT NULL,
                       email TEXT NOT NULL
                       )''')
        
        # Criando um usuário
        cursor.execute('''INSERT INTO usuarios(nome, email) VALUES(?, ?)''', (nome, email))

        # Salvando as alterações e criações
        conn.commit()
        print(f'Usuário {nome} cadastrado com sucesso!')

    except sqlite3.Error as e:
        print(f'Erro so inserir usuário {e}')
    
    finally:
        conn.close()

def listarUsuarios(tabela):

    try:
        cursor.execute(f'SELECT nome, email FROM {tabela}')
        nomes = cursor.fetchall()
        return [{'nome': nome[0], 'email':nome[1]} for nome in nomes]

    except sqlite3.Error as e:
        print(f'Erro ao buscar usuários {e}')
        return []

    finally:
        conn.close()