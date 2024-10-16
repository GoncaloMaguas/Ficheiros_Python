# Solicita ao usuário o número total de vértices
n = int(input("Digite o número total de vértices do grafo: "))

# Cria uma matriz de adjacência vazia
matriz_adj = []

# Preenche a matriz de adjacência com os elementos fornecidos pelo usuário
for i in range(n):
    linha = []
    for j in range(n):
        valor = int(input(f"Digite o valor da posição ({i},{j}): "))
        linha.append(valor)
    matriz_adj.append(linha)

# Exibe a matriz de adjacência
print("Matriz de adjacência:")
for linha in matriz_adj:
    print(linha)
