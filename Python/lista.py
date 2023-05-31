# Lista

# Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com Lista
notas = [7.9, 9.7, 8.2]

# Criando Lista
lista = []  #lista vazia
lista = list() #criando uma lista vazia com função que converte estrutura para lista
lista = [25, 'Joao Paulo', 3.14159, False]
lista_de_listas = [10, [1, 2, 3]]

# Indexação e Slices (fatiamento)

lista = [10, 'Joao Paulo', 3.14159, True]

#Indexãção

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print(lista[-1]) # acessa o ultimo elemento da lista
print(lista[-2]) # acessa o antepenúltimo e assim por diante

# Slices

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3]) # começa no indice 0 e vai até o 3
print(lista[3:6])
print(lista[3:]) # começa aparti do terceiro elemento e vai até o final
print(lista[2:6:2]) # os dois primeiro define o intervalo e o ultimo os pulos
# Utilizando os próprios da lista
# 1 Utilizando os próprios elementos

for elemento in lista: # acada elemento encontrado ele vai imprimindo
    print(elemento)

# 2 Utilizando os Índices
print('Comprimento da lista: ', len(lista)) # *len* sempre tais a quantidade de elementos dentro da lista

for i in range(len(lista)):
    print(lista[i])