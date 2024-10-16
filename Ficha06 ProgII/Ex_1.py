import shutil


origem = input("Digite o nome do arquivo de origem: ")
destino = input("Digite o nome do arquivo de destino: ")


shutil.copy(origem, destino)


print("Arquivo copiado com sucesso!")
