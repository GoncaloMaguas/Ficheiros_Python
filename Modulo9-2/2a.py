import os
import pickle
from alunos import Aluno, cadastrar_aluno, listar_alunos, buscar_aluno, remover_aluno

# define o nome do arquivo de dados
arquivo = 'alunos.dat'

# limpa o arquivo de dados antes dos testes
with open(arquivo, 'wb') as f:
    pickle.dump([], f)

# cadastra dois alunos
cadastrar_aluno('João Silva', 'joao.silva@email.com', 'Engenharia Civil')
cadastrar_aluno('Maria Santos', 'maria.santos@email.com', 'Psicologia')

# lista os alunos cadastrados
listar_alunos()

# busca um aluno pelo nome
aluno = buscar_aluno('João Silva')
print(f'Aluno encontrado: {aluno.nome}, {aluno.email}, {aluno.curso}')

# remove um aluno pelo nome
remover_aluno('João Silva')

# lista os alunos cadastrados novamente
listar_alunos()

# verifica se o arquivo de dados foi atualizado corretamente
with open(arquivo, 'rb') as f:
    alunos = pickle.load(f)
assert len(alunos) == 1
assert alunos[0].nome == 'Maria Santos'

# remove o arquivo de dados após os testes
os.remove(arquivo)
