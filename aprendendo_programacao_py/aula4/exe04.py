import streamlit as st




def soma(lista):
    return sum(lista)

def subtracao(lista):
    return [lista[i] - lista[i+1] for i in range(len(lista) - 1)]

def divisao(lista):
    for elementos in lista:
        if elementos == 0:
            return f'Não é possível dividir por 0.'
    return [lista[i] / lista[i+1] for i in range(len(lista) - 1)]

def multiplicacao(lista):
    return [lista[i] * lista[i+1] for i in range(len(lista) - 1)]

# Título da aplicação
st.title("Calculadora Matemática")

# Seleção da operação
operacao = st.selectbox(
    "Escolha sua operação",
    ["Adição", "Subtração", "Multiplicação", "Divisão", "Integral Indefinida", "Integral Definida", "Derivada"]
)

# Executa a operação escolhida
if operacao in ["Adição", "Subtração", "Multiplicação", "Divisão"]:
    #num1 = st.number_input("Digite o primeiro número:", value=0.0, step=1.0)
    #num2 = st.number_input("Digite o segundo número:", value=0.0, step=1.0)
    
    lista = [1]
    for numeros in lista:
        numeros = st.number_input("Digite o primeiro número: ")
        lista.append(numeros)


    if operacao == "Adição":
        resultado = soma(lista)
    elif operacao == "Subtração":
        resultado = subtracao(lista)

    elif operacao == "Multiplicação":
        resultado = multiplicacao(lista)

    elif operacao == "Divisão":
        resultado = divisao(lista)
    
    if resultado is not None:
        st.write(f"O resultado da sua {operacao.lower()} é: {resultado}")