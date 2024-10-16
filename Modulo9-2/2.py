import pickle

# cria a classe Aluno para armazenar os dados
class Aluno:
    def __init__(self, nome, email, curso):
        self.nome = nome
        self.email = email
        self.curso = curso

# define o nome do arquivo de dados
arquivo = 'alunos.dat'

# verifica se o arquivo já existe e carrega os dados
try:
    with open(arquivo, 'rb') as f:
        alunos = pickle.load(f)
except FileNotFoundError:
    alunos = []

# função para cadastrar um novo aluno
def cadastrar_aluno():
    nome = input('Nome do aluno: ')
    email = input('Email do aluno: ')
    curso = input('Curso do aluno: ')
    aluno = Aluno(nome, email, curso)
    alunos.append(aluno)
    with open(arquivo, 'wb') as f:
        pickle.dump(alunos, f)
    print('Aluno cadastrado com sucesso!')

# função para listar os alunos cadastrados
def listar_alunos():
    print('--- Lista de Alunos ---')
    for i, aluno in enumerate(alunos):
        print(f'{i+1} - Nome: {aluno.nome}, Email: {aluno.email}, Curso: {aluno.curso}')

# função para buscar um aluno pelo nome
def buscar_aluno():
    nome = input('Digite o nome do aluno: ')
    for aluno in alunos:
        if aluno.nome == nome:
            print(f'Nome: {aluno.nome}, Email: {aluno.email}, Curso: {aluno.curso}')
            break
    else:
        print('Aluno não encontrado.')

# função para remover um aluno pelo nome
def remover_aluno():
    nome = input('Digite o nome do aluno: ')
    for aluno in alunos:
        if aluno.nome == nome:
            alunos.remove(aluno)
            with open(arquivo, 'wb') as f:
                pickle.dump(alunos, f)
            print('Aluno removido com sucesso!')
            break
    else:
        print('Aluno não encontrado.')

# loop do menu
while True:
    print('--- Menu ---')
    print('1. Cadastrar novo aluno')
    print('2. Listar alunos')
    print('3. Buscar aluno')
    print('4. Remover aluno')
    print('0. Sair')
    opcao = input('Digite a opção desejada: ')
    if opcao == '1':
        cadastrar_aluno()
    elif opcao == '2':
        listar_alunos()
    elif opcao == '3':
        buscar_aluno()
    elif opcao == '4':
        remover_aluno()
    elif opcao == '0':
        break
    else:
        print('Opção inválida. Tente novamente.')
