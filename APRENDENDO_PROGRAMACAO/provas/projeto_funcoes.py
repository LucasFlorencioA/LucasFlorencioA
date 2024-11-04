# Definindo estrutura de dados
lista_tarefas = []

def adicionar_tarefa(nome, descricao, prioridade, categoria):
    # Adicionar uma nova tarefa
    tarefa = {
        'nome': nome,
        'descricao': descricao,
        'prioridade': prioridade,
        'categoria': categoria,
        'concluida': False
    }
    lista_tarefas.append(tarefa)
    print(f"Tarefa '{nome}' adicionada com sucesso!")

def listar_tarefas(filtro_prioridade = None, filtro_categoria= None):
    # Lista tarefas cadastradas
    tarefas_filtradas = lista_tarefas
    if filtro_prioridade:
        tarefas_filtradas = [tarefa for tarefa in lista_tarefas if tarefa['prioridade'] == filtro_prioridade]
    if filtro_categoria:
        tarefas_filtradas = [tarefa for tarefa in lista_tarefas if tarefa['categoria'] == filtro_categoria]
    
    if len(tarefas_filtradas) > 0:
        for i, tarefa in enumerate(tarefas_filtradas, start=1):
            status = 'Concluída' if tarefa['concluida'] else 'Pendente'
            print(f"{i}. {tarefa['nome']}, Prioridade: {tarefa['prioridade']}, Categoria: {tarefa['categoria']}, Descrição: {tarefa['descricao']}")
    else:
        print('Nenhuma tarefa cadastrada.')

def marcar_concluida(indice):
    tarefa = lista_tarefas[indice -1]
    tarefa['concluida'] = True
    print(f"Tarefa {tarefa['nome']} marcada como concluída!")

def exibir_menu():
    print("\n Gerenciador de Tarefas - Menu de Comandos")
    print('1. Adicionar Tarefa')
    print('2. Listar Tarefas')
    print('3. Marcar tarefa como concluída')
    print('4. Listar tarefas por categoria')
    print('5. Listar tarefas por prioridade')
    print('6. Sair')

def executar_comandos(comando):
    if comando == '1':
        nome = input('Nome da Tarefa: ')
        descricao = input('Descrição da Tarefa: ')
        prioridade = input('Prioridade da Tarefa [Alta - A | Média - M | Baixa - B]')
        categoria = input('Categoria da Tarefa: ')
        adicionar_tarefa(nome,descricao,prioridade,categoria)
    elif comando == '2':
        listar_tarefas()
    elif comando == '3':
        indice = int(input('Digite o número da tarefa a ser concluída: '))
        marcar_concluida(indice)
    elif comando == '4':
        categoria = input('Informe a categoria: ')
        listar_tarefas(filtro_categoria=categoria)
    elif comando == '5':
        prioridade = input('Informe a prioridade [Alta - A | Média - M | Baixa - B]: ')
        listar_tarefas(filtro_prioridade=prioridade)
    elif comando == '6':
        print('Saindo do programa...')
        exit()
    else:
        print('Comando inválido. Tente novamente.')

def main():
    while True:
        exibir_menu()
        comando = input('Digite o número do comando desejado.')
        executar_comandos(comando)

if __name__ == "__main__":
    main()