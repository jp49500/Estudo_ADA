
"""for variavel in range(10):  
    print(variavel)"""

"""for variavel in range(1, 10):  # repeticao de 1 a 9 
    print(variavel)"""

"""for variavel in range(1, 12, 3): # os dois primeiro é o inicio e final e o terceiro paramentro é quantas casa quero pular.
    print(variavel)     # 1,4 , 7, 10"""
soma = 0

for i in range(1, 4):
    nota = float(input(f'Informe sua nota{i}: '))

    soma = soma + nota # contado para somar as notas

print(soma / 3) # media das treis notas