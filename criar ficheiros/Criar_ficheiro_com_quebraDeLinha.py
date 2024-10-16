conteudo = "Acabei de criar o meu primeiro ficheiro em Python"
quebrar_linhas = input("Deseja quebrar linhas no conteúdo? (S/N): ")

if quebrar_linhas.upper() == "S":
    linhas = input("Informe as posições onde deseja quebrar as linhas (separadas por vírgula): ")
    posicoes = [int(posicao.strip()) for posicao in linhas.split(",")]
    
    conteudo_quebrado = ""
    inicio = 0
    for posicao in posicoes:
        conteudo_quebrado += conteudo[inicio:posicao] + "\n"
        inicio = posicao
    conteudo_quebrado += conteudo[inicio:]
    
    conteudo = conteudo_quebrado

with open("primeiro.txt", "w") as arquivo:
    arquivo.write(conteudo)
