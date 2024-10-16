L = []
LU = []

# Recebe as listas do usuário
while True:
    lista = input("Digite uma lista de números (ou 'fim' para encerrar): ")
    if lista == 'fim':
        break
    lista = lista.split() # transforma a string em uma lista de strings
    lista = [int(elemento) for elemento in lista] # transforma cada string em um número inteiro
    L.append(lista)

# Cria a lista única com todos os elementos
for lista in L:
    for elemento in lista:
        LU.append(elemento)

print(LU)
