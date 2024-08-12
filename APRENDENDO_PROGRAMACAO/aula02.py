'''competicao = [
    ('Equipe 1', [70, 85, 98, 89]),
    ('Equipe 2', [75, 78, 75, 95]),
    ('Equipe 3', [90, 75, 99, 84])
]

# Converte a lista de tuplas em um dicionário
competicao_dict = dict(competicao)

# Calcula a média dos pontos para cada equipe
medias = [(nome, sum(pontos)/ len(pontos))for nome, pontos in competicao_dict.items()]


# Ordena a lista de médias em ordem decrescente
# O método sort() modifica a lista no local e retorna None
# Portanto, você precisa usar a função sorted() se quiser criar uma nova lista ordenada
oredem_das_medias = sorted(medias, key=lambda x: x[1], reverse=True)

# Exibe a lista ordenada
print(oredem_das_medias)

#adicionar novos itens
lista_de_compras = {"açucar", "café", "arroz", "feijão"}
lista_de_compras.add("carnes")
print(lista_de_compras)

#Essa função retira todas as vogais!
set1 = {letra for letra in 'programaçao' if letra not in 'aeiou'}
print(set1)

ids = {10, 12, 14, 16}
novos_ids = {11, 13, 15, 16}
#Adiciona items
ids.update(novos_ids)
print(ids)

#Remove itens de um set
convidados = {"Alex", "Artur", "Monalisa", "Pedro"}
convidados.remove("Alex")
print(convidados)

#Atualizar um dos sets
convidados_2 = {"Alex", "Artur", "Monalisa", "Pedro"}
convidados_3 = {"Alex", "Alice"}
convidados_2.intersection_update(convidados_3)
print(convidados_2)

#Sets não permite elementos duplicados e não mantém a ordem de inserção dos elementos.
frutas = set()
#Adiciona items
frutas.add("maçã")
frutas.add("banana")
frutas.add("uva")
frutas.add("laranja")
frutas.add("morango")
print(frutas)

#Verifica se o item está presente no conjunto
if "banana" in frutas:
    print('A banana está presente no conjunto de frutas.')
else:
    print('A banana não está presente no conjunto de frutas.')
    
frutas_vermelhas = set()

lista_frutas = ["morango", "cereja", "framboesa"]
#Adiciona items a um set
frutas_vermelhas.update(lista_frutas)
print(frutas_vermelhas)

#Remove itens de um set
frutas_vermelhas.remove("cereja")
print(frutas_vermelhas)

carros_1 = {"corola", "uno", "palio"}
carros_2 = {"corsa", "hb20", "uno"}

print(carros_1.union(carros_2))

#função para atualizar um dos sets com interseção entre eles
def intersection(a,b):
    print(a.intersection(b))

intersection(carros_1, carros_2)


def cadastrar_alunos():
    alunos = []
    
    while True:
        # Coleta de dados do aluno
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        matematica = float(input("Digite a nota de Matemática: "))
        ciencias = float(input("Digite a nota de Ciências: "))
        historia = float(input("Digite a nota de História: "))
        
        # Armazena os dados do aluno em um dicionário
        aluno = {
            'nome': nome,
            'idade': idade,
            'notas': (matematica, ciencias, historia)
        }
        
        # Adiciona o aluno à lista de alunos
        alunos.append(aluno)
        
        # Pergunta ao usuário se deseja adicionar mais alunos
        continuar = input("Deseja cadastrar outro aluno? (s/n): ")
        if continuar.lower() != 's':
            break
    
    return alunos

def visualizar_alunos(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    
    melhor_aluno = None
    maior_media = 0
    
    print("\n--- Lista de Alunos ---")
    for aluno in alunos:
        nome = aluno['nome']
        idade = aluno['idade']
        notas = aluno['notas']
        media = sum(notas) / len(notas)
        
        # Exibe as informações do aluno
        print(f"Nome: {nome}")
        print(f"Idade: {idade}")
        print(f"Notas: Matemática={notas[0]}, Ciências={notas[1]}, História={notas[2]}")
        print(f"Média: {media:.2f}\n")
        
        # Verifica se este aluno tem a melhor média
        if media > maior_media:
            maior_media = media
            melhor_aluno = aluno
    
    if melhor_aluno:
        print("--- Aluno com Melhor Média ---")
        print(f"Nome: {melhor_aluno['nome']}")
        print(f"Idade: {melhor_aluno['idade']}")
        print(f"Notas: Matemática={melhor_aluno['notas'][0]}, Ciências={melhor_aluno['notas'][1]}, História={melhor_aluno['notas'][2]}")
        print(f"Média: {maior_media:.2f}")

# Função principal para executar o sistema
def main():
    alunos = cadastrar_alunos()
    visualizar_alunos(alunos)

if __name__ == "__main__":
    main()'''