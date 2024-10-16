num = 100
categoria = 'A'
funcionarios = []
n=int(input("Digite o numero de pessoas: "))
for i in range(n):
    nome = input('Digite o nome do funcionário: ')
    funcionario = (num, nome, categoria)
    funcionarios.append(funcionario)
    num += 10
    categoria = chr(ord(categoria) + 1)
    

print(funcionarios)
