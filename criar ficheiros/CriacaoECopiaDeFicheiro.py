def copia_arquivo(arquivo_origem, arquivo_destino):
    try:
        with open(arquivo_origem, 'r') as origem:
            with open(arquivo_destino, 'w') as destino:
                conteudo = origem.read()
                destino.write(conteudo)
        print(f"Cópia do arquivo {arquivo_origem} criada com sucesso no arquivo {arquivo_destino}.")
    except FileNotFoundError:
        print("Arquivo de origem não encontrado.")

def main():
    arquivo_origem = input("Digite o nome do arquivo de origem: ")
    arquivo_destino = input("Digite o nome do arquivo de destino: ")
    conteudo_origem = input("Digite o conteúdo do arquivo de origem: ")

    with open(arquivo_origem, 'w') as origem:
        origem.write(conteudo_origem)

    copia_arquivo(arquivo_origem, arquivo_destino)

main()
