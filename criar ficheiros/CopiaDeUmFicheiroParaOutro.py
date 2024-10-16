def copia_arquivo(arquivo_origem, arquivo_destino):
    try:
        with open(arquivo_origem, 'rb') as origem:
            with open(arquivo_destino, 'wb') as destino:
                destino.write(origem.read())
        print(f"Cópia do arquivo {arquivo_origem} criada com sucesso no arquivo {arquivo_destino}.")
    except FileNotFoundError:
        print("Arquivo de origem não encontrado.")

def main():
    arquivo_origem = input("Digite o nome do arquivo de origem: ")
    arquivo_destino = input("Digite o nome do arquivo de destino: ")

    copia_arquivo(arquivo_origem, arquivo_destino)

main()
