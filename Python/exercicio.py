
"""
# Questão 1
x = int(input('Digite um numero inteiro: '))

if x < 0:
    resp1 = 'negativo'
else:
    resp1 = 'Positivo'

if x % 2 == 0:
    resp2 = 'par'
else:
    resp2 = 'impar'

print('O numero {} é {} e {}.'. format(x, resp1, resp2))

"""

# Questão 2
cont = 0
resultado = 0
n = 1000

while cont != n:
    resultado = resultado + 1/(2**cont)
    cont = cont + 1

print(resultado)

# Questão 3

#for _ in range(10):
#    print('Ola mundo!')

for _ in [10]:
    print("Ola mundo")
