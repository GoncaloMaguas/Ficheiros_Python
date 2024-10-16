import pandas as pd
from anytree import Node, RenderTree

# Função para verificar se um navio está na árvore
def verificar_navio(navio, tipo, root):
    for node in root.children:
        if node.name == tipo:
            for subnode in node.children:
                if navio in subnode.name:
                    return True
    return False

# Função para mostrar todos os navios de um dado tipo
def mostrar_navios_tipo(tipo, root):
    for node in root.children:
        if node.name == tipo:
            for subnode in node.children:
                print(subnode.name)

# Função para mostrar todos os navios de um dado tipo e ano de construção
def mostrar_navios_tipo_ano(tipo, ano, root):
    for node in root.children:
        if node.name == tipo:
            for subnode in node.children:
                if str(ano) in subnode.name:
                    print(subnode.name)

# Função para mostrar todos os navios de um dado ano de construção
def mostrar_navios_ano(ano, root):
    for node in root.children:
        for subnode in node.children:
            if str(ano) in subnode.name:
                print(subnode.name)

# Função para exibir a árvore
def exibir_arvore(root):
    for pre, _, node in RenderTree(root):
        print(f'{pre}{node.name}')
        


def ler_excel():
    pag1_df = pd.read_excel("navios.xlsx", sheet_name="navios_passageiros")
    pag2_df = pd.read_excel("navios.xlsx", sheet_name="navios_de_carga")
    pag3_df = pd.read_excel("navios.xlsx", sheet_name="navios_rebocadores")
    pag4_df = pd.read_excel("navios.xlsx", sheet_name="navios_tanque")

    root = Node('Navios Mercantes')

    passageiros_node = Node('Passageiros', parent=root)
    for _, row in pag1_df.iterrows():
        nome = row['nome']
        ano_construcao = row['anoConstrucao']
        total_passageiros = row['totalPassageiros']
        node = Node(f'{nome} (Ano de Contrução:{ano_construcao},    Passageiros:{total_passageiros})', parent=passageiros_node)

    carga_node = Node('Carga', parent=root)
    for _, row in pag2_df.iterrows():
        nome = row['nome']
        classe = row['classe']
        ano_construcao = row['anoConstrucao']
        potencia = row['potência']
        node = Node(f'{nome} (Classe:{classe},    Ano de Contrucao:{ano_construcao},    Potencia:{potencia})', parent=carga_node)

    rebocadores_node = Node('Rebocadores', parent=root)
    for _, row in pag3_df.iterrows():
        nome = row['nome']
        ano_construcao = row['anoConstrucao']
        potencia = row['potencia']
        Vmax = row['velocidadeMaxima']
        node = Node(f'{nome} (Ano de Contrucao:{ano_construcao},    Potencia:{potencia},    Velocidade Maxima:{Vmax})', parent=rebocadores_node)

    tanque_node = Node('Tanque', parent=root)
    for _, row in pag4_df.iterrows():
        nome = row['nome']
        ano_construcao = row['anoConstrucao']
        potencia = row['potencia']
        Vnorm = row['velocidadeNormal']
        tripulantes = row['tripulantes']
        node = Node(f'{nome} (Ano de Contrucao:{ano_construcao},    Potencia:{potencia},    Velocidade Normal:{Vnorm},     Tripulantes:{tripulantes})', parent=tanque_node)

    # Retorna a raiz da árvore
    return root


