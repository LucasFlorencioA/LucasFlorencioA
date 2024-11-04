class Tarefa:
    def __init__(self, titulo, descricao, concluida=False):
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = concluida

    def concluir_tarefa(self):
        self.concluida = True
        print(f'Tarefa {self.titulo} concluída com sucesso.')

    def __str__(self):
        status = 'Concluída' if self.concluida else 'Pendente'
        return f'Título: {self.titulo} | Descrição: {self.descricao} | Status: {status}'
    

class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def add_tarefas(self, tarefa):
        if isinstance(tarefa, Tarefa):
            self.tarefas.append(tarefa)
            print(f'Tarefa {tarefa.titulo} adicionada ao projeto {self.nome}')
        else:
            print('Apenas objetos da classe tarefa podem ser adicionados ao projeto.')

    def listar_tarefas(self):
        if not self.tarefas:
            print('Não há nenhuma tarefa cadastrada no projeto.')
        else:
            print('Tarefas cadastradas: ')
            for tarefa in self.tarefas:
                print(f'{tarefa.titulo}')

    def __str__(self):
        return f'Projeto: {self.nome} | Nº de Tarefas: {len(self.tarefas)}'
    

projeto = Projeto('Prédio da Infinity.')

tarefa_1 = Tarefa('Terraplanagem','Deixar o terreno plano e nivelado para construção do prédio.')
tarefa_2 = Tarefa('Marcação dos pilares','Seleciona os locais onde serão construídos os pilares.')
tarefa_3 = Tarefa('Escavação','Escavação dos pilares')
tarefa_4 = Tarefa('Construir Estrutura', 'Levantar concreto dos andares do prédio.')
tarefa_5 = 'Pontos eletricos.'


projeto.add_tarefas(tarefa_1)
projeto.add_tarefas(tarefa_2)
projeto.add_tarefas(tarefa_3)
projeto.add_tarefas(tarefa_4)
projeto.add_tarefas(tarefa_5)


tarefa_1.concluir_tarefa()

projeto.listar_tarefas()
