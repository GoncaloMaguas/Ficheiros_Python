def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print("Arquivo não encontrado.")

def main():
    nome_arquivo = input("Digite o nome do arquivo: ")
    ler_arquivo(nome_arquivo)

main()
