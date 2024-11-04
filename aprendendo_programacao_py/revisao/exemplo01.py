'''Exercício: Gerenciando um Inventário de Loja

Você foi contratado para desenvolver um sistema simples de gerenciamento de inventário para uma loja.
A loja vende diferentes produtos, e você precisa criar um dicionário para armazenar o nome do produto como chave e a quantidade disponível em estoque como valor.

Tarefas:
Crie um dicionário chamado inventario com os seguintes itens:

"Maçã": 50
"Banana": 20
"Laranja": 30
"Uva": 100

1. Adicione um novo produto ao dicionário com o nome "Morango" e a quantidade de 40.

2. Remova um produto do dicionário. Vamos dizer que a loja parou de vender bananas, então remova "Banana" do dicionário.

3. Atualize a quantidade de um dos produtos. A loja vendeu 10 maçãs, então subtraia 10 da quantidade atual de "Maçã".

4.Verifique a existência de um produto no dicionário. Verifique se "Laranja" está no inventário e exiba uma mensagem apropriada.-
'''

#SOLUÇÃO

# Criando inventário
inventario = {
    "Maçã": 50,
    "Banana": 20,
    "Laranja": 30,
    "Uva": 100
}

# 1 - Adicionar novo produto
inventario['Morango'] = 40

# 2
del inventario['Banana'] 


# 3
inventario['Maçã'] -= 10

# 4
existe_laranja = False
if "Laranja" in inventario:
  existe_laranja = True
  print('Existe estoque de laranja no inventário.')
else:
  print('Não há estoque de laranja no inventário.')
