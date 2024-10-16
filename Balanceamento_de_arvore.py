class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    else:
        return max(height(node.left), height(node.right)) + 1

def balance_factor(node):
    if node is None:
        return 0
    else:
        return height(node.left) - height(node.right)

def rotate_left(node):
    new_root = node.right
    node.right = new_root.left
    new_root.left = node
    return new_root

def rotate_right(node):
    new_root = node.left
    node.left = new_root.right
    new_root.right = node
    return new_root

def balance_tree(node):
    if node is None:
        return None

    # Calcula o fator de balanceamento do nó atual
    bf = balance_factor(node)

    # Caso esteja desbalanceado à direita
    if bf < -1:
        # Caso o filho à direita esteja desbalanceado à esquerda
        if balance_factor(node.right) > 0:
            node.right = rotate_right(node.right)
        # Realiza a rotação simples à esquerda
        return rotate_left(node)

    # Caso esteja desbalanceado à esquerda
    elif bf > 1:
        # Caso o filho à esquerda esteja desbalanceado à direita
        if balance_factor(node.left) < 0:
            node.left = rotate_left(node.left)
        # Realiza a rotação simples à direita
        return rotate_right(node)

    # Caso já esteja balanceado
    else:
        return node

def print_tree(node):
    if node is not None:
        print_tree(node.left)
        print(node.value)
        print_tree(node.right)


# Cria a árvore
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(20)

# Balanceia a árvore
root = balance_tree(root)

# Mostra o resultado final
print_tree(root)
