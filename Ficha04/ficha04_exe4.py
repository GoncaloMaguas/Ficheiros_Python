def get_adjacent_nodes(adj_matrix, node):
    adj_nodes = []
    for i in range(len(adj_matrix[node])):
        if adj_matrix[node][i] == 1:
            adj_nodes.append(i)
    return adj_nodes