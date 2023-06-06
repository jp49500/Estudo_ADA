# > Dicionario

# Criando dicionarios

dicionario = {} # dicionario vazio
dicionario = dict() # função para criar dicionario vazio

dicionario = { 'nome': 'Joao Paulo', 'idade': 25, 'altura': 1.65}

print(dicionario['nome'])

# Adicionar elementos em um dicionario

dicionario['programador'] = True

print(dicionario)

dicionario['altura'] = 3 # subiscreve a informação

print(dicionario['altura'])

# Iterando sobre um dicionario

for chave in dicionario:
    print(chave, dicionario[chave]) # variavel chave percore as chaves do dicionario e dicionario[chave] percore a descrição da chave

# Testando a existencia de uma chave

print('Existe a palava "peso" no dicionario?')
print('peso' in dicionario)
print('Existe a palava "altura" no dicionario?')
print('altura' in dicionario)

