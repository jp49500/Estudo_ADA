# Lista

# Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com Lista
notas = [7.9, 9.7, 8.2]

# Criando Lista
print('-- Criando Lista --')
lista = []  #lista vazia
lista = list() #criando uma lista vazia com função que converte estrutura para lista
lista = [25, 'Joao Paulo', 3.14159, False]
lista_de_listas = [10, [1, 2, 3]]

# Indexação e Slices (fatiamento)

lista = [10, 'Joao Paulo', 3.14159, True]

#Indexãção
print('-- Indexação(acessando por indice) --')
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print(lista[-1]) # acessa o ultimo elemento da lista
print(lista[-2]) # acessa o antepenúltimo e assim por diante

# Slices
print('-- Slices(fatiamento) --')
lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3]) # começa no indice 0 e vai até o 3
print(lista[3:6])
print(lista[3:]) # começa aparti do terceiro elemento e vai até o final
print(lista[2:6:2]) # os dois primeiros definem o intervalo e o ultimo define a alternancia(pulos)
# Utilizando os próprios da lista
# 1 Utilizando os próprios elementos da lista

for elemento in lista: # acada elemento encontrado ele vai imprimindo
    print(elemento)

# 2 Utilizando os Índices
print('-- Acessando o indice pela função len --')
print('Comprimento da lista: ', len(lista)) # *len* sempre tais a quantidade de elementos dentro da lista

for i in range(len(lista)):
    print(lista[i])

# > Metodos de listas
print('-- Metodos de listas --')

lista = [1, 3, 12, 8, 2]

# apeend (acrecentando)

print('Antes do append: ', lista)
lista.append(3) # estou inserindo um elemento no final da lista
print('Depois do append: ', lista)

# insert (inserir)

lista.insert(2, 10) # estou dizendo onde quero inserir o elemento
print('Depois do insert: ', lista)

# extend 
# utilizado para juntar listas

lista2 = [1, 2, 3]

lista.extend(lista2)
print('Depois do extend: ', lista)

# pop (remove)

lista.pop()

print('Lista após o pop: ', lista)

lista.pop(0) # removendo elemento pela posição do indice
print('Lista após o pop: ', lista)

# remove

lista.remove(3) # remove o elemento pelo proprio valor
# a função vai procurar o numero 3 e o primeiro que encontrar sera removido obs: só remove
print('Depois do remove', lista)

# count

print('Quantidade de 2 na lista: ', lista.count(2)) # quantidade de elemento pelo valor que tem na lista

# index

print('Indice do elemento 12: ', lista.index(12)) # mostar o index de onde esta o elemento

# sort

lista.sort() # organiza a lista de forma crescente
print('Lista de maneira crescente',lista)
lista.sort(reverse=True) # organizando de forma decrescente
print('Lista de maneira descresente: ', lista)

# Funções para lista

# len

print('Quantos elementos tem na lista: ', len(lista)) # quantos elementos tem na lista

# sum

print('Soma de todos os elementos: ',sum(lista)) # soma todos os elementos da lista]

# max

print('Maior elemento da lista: ', max(lista)) # retorna o maior valor da lista

# min

print('Menor elemento da lista: ', min(lista))
