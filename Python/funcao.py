# Função

# 1. O que são funções e porque utiliza-las?
# Funções que já utilizamos anteriome

"""
print() 
input()
len()
max()
"""
# 2. Criação de funções

# Função Inicial

def saudacao():
    print('Seja Bem-vindo(o)!')
    print('É um prazer ter você fazendo parte desse curso!')

saudacao()

# Função com parametros

def saudacao(nome, curso):
    print(f'Seja Bem-vindo(o), {nome}!')
    print(f'É um prazer ter você fazendo parte do curso de {curso}!')

saudacao('João Paulo', 'Python')
saudacao('Marcos', 'Java')

# Função com parametros default(por Padrão)

def saudacao(nome, curso='Python'):
    print(f'Seja Bem-vindo(o), {nome}!')
    print(f'É um prazer ter você fazendo parte do curso de {curso}!')

saudacao('João Paulo', 'C++') 

# Funções com retorno

def soma(num1, num2):
    return num1 + num2 # depois do return nada mais é execultado

resultado = soma(5,7)

print('O resultado da soma é: ', resultado)

def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        return num1 / num2



resultado = calculadora(10, 20, '/')

print(resultado)