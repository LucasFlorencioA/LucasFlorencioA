import streamlit as st
import sympy as sp
# Definir símbolos
x, y, z = sp.symbols('x y z')

def calcular_integral_indefinida(expr, var):
    integral = sp.integrate(expr, var)
    return integral

def calcular_integral_definida(expr, var, a, b):
    integral_indefinida = sp.integrate(expr, var)
    integral_definida = integral_indefinida.subs(var, b) - integral_indefinida.subs(var, a)
    return integral_definida

def calcular_derivada(expr, var):
    derivada = sp.diff(expr, var)
    return derivada

# Título da aplicação
st.title("Calculadora Matemática")

# Seleção da operação
operacao = st.selectbox(
    "Escolha sua operação",
    ["Adição", "Subtração", "Multiplicação", "Divisão", "Integral Indefinida", "Integral Definida", "Derivada"]
)

# Executa a operação escolhida
if operacao in ["Adição", "Subtração", "Multiplicação", "Divisão"]:
    num1 = st.number_input("Digite o primeiro número:", value=0.0, step=1.0)
    num2 = st.number_input("Digite o segundo número:", value=0.0, step=1.0)
    
    if operacao == "Adição":
        resultado = num1 + num2
    elif operacao == "Subtração":
        resultado = num1 - num2
    elif operacao == "Multiplicação":
        resultado = num1 * num2
    elif operacao == "Divisão":
        if num2 != 0:
            resultado = num1 / num2
        else:
            st.error("Erro! Divisão por zero.")
            resultado = None
    if resultado is not None:
        st.write(f"O resultado da sua {operacao.lower()} é: {resultado}")

elif operacao in ["Integral Indefinida", "Integral Definida", "Derivada"]:
    funcao = st.text_input("Escreva sua função:")
    letra = st.selectbox("Escolha a variável", ["x", "y", "z"])
    var = sp.symbols(letra)
    
    if funcao:
        expr = sp.sympify(funcao)
        
        if operacao == "Integral Indefinida":
            resultado = calcular_integral_indefinida(expr, var)
            st.write(f"A integral indefinida de {funcao} em relação a {letra} é:")
            st.latex(sp.latex(resultado) + " + C")
        
        elif operacao == "Integral Definida":
            a = st.number_input("Digite o limite inferior da integral:", value=0.0)
            b = st.number_input("Digite o limite superior da integral:", value=1.0)
            resultado = calcular_integral_definida(expr, var, a, b)
            st.write(f"A integral definida de {funcao} de {a} a {b} é:")
            st.latex(sp.latex(resultado))
        
        elif operacao == "Derivada":
            resultado = calcular_derivada(expr, var)
            st.write(f"A derivada de {funcao} em relação a {letra} é:")
            st.latex(sp.latex(resultado))