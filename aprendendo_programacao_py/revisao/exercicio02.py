'''Crie um dicionário chamado notas_alunos onde as chaves são os nomes dos alunos e os valores são listas de notas (números entre 0 e 10). Adicione os seguintes alunos e suas respectivas notas:

"Italo": [8, 7.5, 9]
"Bruno": [2, 4, 10]
"Carlos": [9, 8.5, 10]
"Gabriel": [7, 7, 8]

1.Adicione as notas de um novo aluno chamado "Eduardo", que tirou 7, 8 e 9 nas três avaliações.

2.Calcule a média de notas para cada aluno e armazene as médias em um novo dicionário chamado medias_alunos.

3.Identifique o aluno com a maior média na turma.

4.Conte quantos alunos tiveram média maior ou igual a 7 e quantos tiveram média menor que 7.

5.Exiba um relatório final que mostre o nome de cada aluno, suas notas, sua média e se ele foi aprovado (média >= 7) ou reprovado.
'''


notas_alunos = {
"Italo": [8, 7.5, 9],
"Bruno": [2, 4, 10],
"Carlos": [9, 8.5, 10],
"Gabriel": [7, 7, 8],
}

#1 
notas_alunos['Eduardo'] = [7,8,9]

#2
nomes_alunos_lista = []
medias_alunos_lista = []
for chave,valor in notas_alunos.items():
  medias = round(sum(valor)/len(valor),2)
  nomes_alunos_lista.append(chave)
  medias_alunos_lista.append(medias)

dicionario_medias = dict(zip(nomes_alunos_lista,medias_alunos_lista))

print(dicionario_medias)

maior_media = max(medias_alunos_lista)
print(maior_media)

cont_acima = 0
cont_abaixo = 0
for chave, valor in dicionario_medias.items():
  if valor >= 7:
    print(f'O Aluno {chave} obteve média {valor} que é acima de 7.')
    cont_acima += 1

  else:
    print(f'O Aluno {chave} obteve média {valor} que é abaixo de 7.')
    cont_abaixo += 1

print(f'# de Alunos que foram aprovados: {cont_acima}')

print(f'# de Alunos que foram reprovados: {cont_abaixo}')

print('RELATÓRIO FINAL')
print('#NOTAS#')
for chave,valor in notas_alunos.items():
  print(f'Aluno: {chave} - Notas: {valor}')
print('#MÉDIAS#')
for chave,valor in dicionario_medias.items():
  if valor >= 7:
    print(f'O Aluno {chave} obteve média {valor} e foi aprovado.')
  else:
    print(f'O Aluno {chave} obteve média {valor} e foi reprovado.')
