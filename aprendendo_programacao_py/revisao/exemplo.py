# CONDICIONAIS

# Recebe o valor da idade do usuário
idade = int(input('Digite sua idade: '))

# Receber os antecedentes criminais
criminoso = input('O usuário cometeu algum crime? [s/n]')

if criminoso == 's':
  criminoso = True
elif criminoso == 'n':
  criminoso = False
else:
  print('Opção inválida.')
# Classificando usuário

if idade <= 12 and criminoso == True:
  print('O usuário é um menor infrator.')
elif 12 < idade <= 17 and criminoso == True:
  print('O usuário é um menor infrator.')
elif 17 < idade <= 60 and criminoso == True:
  print('O usuário é um infrator.')
elif idade <= 12 and criminoso == False:
  print('O usuário NÃO é um menor infrator, e é criança.')
elif 12 < idade <= 17 and criminoso == False:
  print('O usuário NÃO é um menor infrator, e é adolescente.')
elif 17 < idade <= 60 and criminoso == False:
  print('O usuário NÃO é um infrator.')
else:
  print('O usuário é aposentado e não é infrator.')


#WHILE


from time import sleep


contador = int(input('Digite o valor do contador: '))

while True:
  print(f'Valor do contador:{contador}')
  contador += 1
  continuar = input('Deseja continuar? [s/n]: ')
  if continuar == 's':
    continue
  elif continuar == 'n':
    break
  sleep(2)


#FOR


# Verifica o número de usuários
usuarios = int(input('Digite o número de usuários: '))

# Variável que receberá a soma das idades dos usuários analisados
soma_idades = 0


# Verifica e soma as idades de cada usuário
lista_idades = []
for usuario in range(usuarios):
  idade = int(input(f'Digite a idade do usuário #{usuario + 1}: '))
  lista_idades.append(idade)
  soma_idades += idade

# Calcula a media de idades
media_idades = soma_idades / usuarios

# Calcula a maior idade entre os usuários
usuario_mais_velho = max(lista_idades)

# Calcula a menor idade entre os usuários
usuario_mais_novo = min(lista_idades)

# Classificar usuários de acordo com a média
if media_idades <= 18:
  classificacao = 'jovem'
elif 18 < media_idades <= 60:
  classificacao = 'adulta'
else:
  classificacao = 'idosa'

print(f'A média de idades é {round(media_idades,2)}, portanto os usuários são considerados classe {classificacao}. O usuário mais velho tem {usuario_mais_velho} e o usuário mais novo tem {usuario_mais_novo}.')



#LISTAS

# Listaque que conterá o faturamento por produto.
lista_faturamento = []

# Verificar quantos produtos foram vendidos
qtd_de_produtos = int(input('Digite a quantidade de produtos vendidos: '))

for produto in range(qtd_de_produtos):
  preco_de_venda = float(input(f'Digite o valor de venda do produto #{produto + 1}.'))
  lista_faturamento.append(preco_de_venda)

# Calcula o faturamento total diário
faturamento_diario = round(sum(lista_faturamento), 2)

# Calcula o faturamento médio diáio
faturamento_medio = round(sum(lista_faturamento)/len(lista_faturamento),2)

# Calcular o preço do produto mais caro
produto_mais_caro = round(max(lista_faturamento),2)

# Calcular o preço do produto mais barato
produto_mais_barato = round(min(lista_faturamento),2)

print(f'Quantidade de produtos vendidos: {qtd_de_produtos}.')
print(f'Faturamento Total Diário: R${faturamento_diario}.')
print(f'Faturamento Médio Diário: R${faturamento_medio}.')
print(f'Produto mais caro: R${produto_mais_caro}.')
print(f'Produto mais barato: R${produto_mais_barato}.')