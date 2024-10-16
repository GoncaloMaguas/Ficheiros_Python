def is_cyclic(graph):
    visited = set()
    for node in graph.keys():
        if node not in visited:
            if is_cyclic_util(graph, node, visited, -1):
                return True
    return False

def is_cyclic_util(graph, node, visited, parent):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            if is_cyclic_util(graph, neighbor, visited, node):
                return True
        elif neighbor != parent:
            return True
    return False

graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
if is_cyclic(graph):
    print("O grafo é cíclico.")
else:
    print("O grafo é acíclico.")
