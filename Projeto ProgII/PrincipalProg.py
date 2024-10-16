import pandas as pd
from anytree import Node, RenderTree

# Funções do programa importado

import Funcoes_E_ConexoesAoFicheiroXLSX


root=Funcoes_E_ConexoesAoFicheiroXLSX.ler_excel()



# Menu principal
while True:
    print("\n\n\n---- Menu ----")
    print("1. Verificar se um navio está na árvore")
    print("2. Mostrar todos os navios de um dado tipo")
    print("3. Mostrar todos os navios de um dado tipo e ano de construção")
    print("4. Mostrar todos os navios de um dado ano de construção")
    print("5. Exibir a árvore")
    print("0. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        navio = input("Digite o nome do navio: ")
        tipo = input("Digite o tipo do navio (Passageiros, Carga, Rebocadores ou Tanque):")
        if Funcoes_E_ConexoesAoFicheiroXLSX.verificar_navio(navio, tipo, root):
            print("O navio está na árvore.")
        else:
            print("O navio não está na árvore.\nPara uma visão mais ampla dos navios pertencentes á árvore escolha a opção 5")
    elif opcao == '2':
        tipo = input("Digite o tipo do navio (Passageiros, Carga, Rebocadores ou Tanque):")
        Funcoes_E_ConexoesAoFicheiroXLSX.mostrar_navios_tipo(tipo, root)
    elif opcao == '3':
        tipo = input("Digite o tipo do navio (Passageiros, Carga, Rebocadores ou Tanque):")
        ano = input("Digite o ano de construção(formato do ano AAAA): ")
        Funcoes_E_ConexoesAoFicheiroXLSX.mostrar_navios_tipo_ano(tipo, ano, root)
    elif opcao == '4':
        ano = input("Digite o ano de construção(formato do ano AAAA): ")
        Funcoes_E_ConexoesAoFicheiroXLSX.mostrar_navios_ano(ano, root)
    elif opcao == '5':
        Funcoes_E_ConexoesAoFicheiroXLSX.exibir_arvore(root)
    elif opcao == '0':
        print("\nPrograma terminado")
        break
    else:
        print("Opção inválida. Tente novamente.\n")
