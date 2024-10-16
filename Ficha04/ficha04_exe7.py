def is_cycle(path):
    # Verifica se o caminho tem pelo menos dois vértices
    if len(path) < 2:
        return False
    
    # Verifica se o primeiro e o último vértices são iguais
    if path[0] != path[-1]:
        return False
    
    # Cria um conjunto vazio para armazenar os vértices visitados
    visited = set()
    
    # Verifica se cada vértice do caminho já foi visitado
    for vertex in path:
        if vertex in visited:
            return False
        visited.add(vertex)
    
    # Se chegou aqui, o caminho é um ciclo
    return True
    
caminho = [1, 2, 3, 4, 1]
if is_cycle(caminho):
    print("O caminho é um ciclo.")
else:
    print("O caminho não é um ciclo.")