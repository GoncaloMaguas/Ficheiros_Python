import lista

lista0 = []  # cria uma lista vazia
lista1= []
while True:
    valor = int(input("Digite um valor para a primeira lista (ou '-1' para sair): "))
    if valor == -1:
        break  # sai do loop se o usuário digitar "fim"
    lista0.append(valor)  # adiciona o valor à lista


while True:
    valor = int(input("Digite um valor para a segnda lista (ou '-1' para sair): "))
    if valor == -1:
        break  # sai do loop se o usuário digitar "fim"
    lista1.append(valor)  # adiciona o valor à lista

print("A primeira lista que criou foi:", lista0)
print("A segunda lista que criou foi:", lista1)

elemento = int(input("Insira o valor para verificar se pertence á lista: "))

print("O valor",elemento,"existe na primeira lista? ",lista.verifica_membro(elemento, lista0))
print("Quantos",elemento,"existem na primeira lista? ", lista.contaRepetido(elemento, lista0))
print("Quais os numeros repetidos na primeira lista? ",lista.repetidos(lista0))
print("Quais dos numeros sao comuns nas duas listas?",lista.elementos_comuns(lista0, lista1))
print("O maior valor da primeira lista é: ",lista.maior_elemento(lista0))
