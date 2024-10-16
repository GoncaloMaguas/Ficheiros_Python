num_vertices = int(input("Digite o número total de vértices do grafo: "))

adj_matrix = []


for i in range(num_vertices):
    
    conexoes = []
    for j in range(num_vertices):
    
        elem = int(input(f"Digite o elemento ({i}, {j}): "))

        conexoes.append(elem)
    adj_matrix.append(conexoes)

print("Matriz de adjacência:")
for linha in adj_matrix:
    print(linha)
