class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def exibir(self):
        print(f'Nome: {self.nome}\nCargo:{self.cargo}\nSalário: R${round(self.salario, 2)}')

    
class Empresa:
    def __init__(self, nome_empresa):
        self.nome_empresa = nome_empresa
        self.funcionarios = []


    def add_funcionarios(self, funcionario):
        self.funcionarios.append(funcionario)
        print(f'O funcionário {funcionario.nome} foi contratado.')

    def remover_funcionarios(self, nome):
        for funcionario in self.funcionarios:
            if funcionario.nome == nome:
                self.funcionarios.remove(funcionario)
                print(f'Funcionario {nome} removido com sucesso.')
                return
        
        
    def listar_funcionarios(self):
        if not self.funcionarios:
            print('Não há funcionários cadastrados.')
        else:
            print(f'Lista de Funcionários da empresa {self.nome_empresa}')
            for funcionario in self.funcionarios:
                for chave, valor in vars(funcionario).items():
                    print(f'{chave} - {valor}')


empresa_xpto = Empresa('XPTO LTDA')

bruno = Funcionario('Bruno','Desenvolvedor', 18000)
fabricio = Funcionario('Fabrício','Auxiliar de serviços gerais', 1400)
cassia = Funcionario('Cassia','Product Owner', 24000)

empresa_xpto.add_funcionarios(bruno)
empresa_xpto.add_funcionarios(fabricio)
empresa_xpto.add_funcionarios(cassia)


empresa_xpto.listar_funcionarios()

empresa_xpto.remover_funcionarios('Fabrício')

empresa_xpto.listar_funcionarios()