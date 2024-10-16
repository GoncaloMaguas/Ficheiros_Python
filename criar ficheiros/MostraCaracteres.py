def obter_primeiros_caracteres_arquivo(nome_arquivo, x):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        primeiros_caracteres = conteudo[:x]
    return primeiros_caracteres

nome_arquivo = input("Digite o nome do arquivo: ")
x = int(input("Digite o número de caracteres a serem retornados: "))

try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        if x > len(conteudo):
            print("O valor inserido é maior do que a quantidade de caracteres no arquivo.")
        else:
            primeiros_caracteres = obter_primeiros_caracteres_arquivo(nome_arquivo, x)
            print("Primeiros", x, "caracteres:")
            print(primeiros_caracteres)
except FileNotFoundError:
    print("Arquivo não encontrado.")
