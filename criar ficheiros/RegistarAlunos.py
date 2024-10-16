def registrar_aluno():
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o email do aluno: ")
    curso = input("Digite o curso do aluno: ")
    
    with open("alunos.txt", "a") as arquivo:
        arquivo.write(f"{nome},{email},{curso}\n")
    
    print("Aluno registrado com sucesso!")

def listar_alunos():
    try:
        with open("alunos.txt", "r") as arquivo:
            alunos = arquivo.readlines()
        
        if not alunos:
            print("Nenhum aluno registrado.")
        else:
            print("Alunos registrados:")
            for aluno in alunos:
                nome, email, curso = aluno.strip().split(",")
                print(f"Nome: {nome}\nEmail: {email}\nCurso: {curso}\n")
    except FileNotFoundError:
        print("Nenhum aluno registrado.")

def buscar_aluno():
    nome_busca = input("Digite o nome do aluno a ser buscado: ")
    
    try:
        with open("alunos.txt", "r") as arquivo:
            alunos = arquivo.readlines()
        
        encontrado = False
        for aluno in alunos:
            nome, email, curso = aluno.strip().split(",")
            if nome.lower() == nome_busca.lower():
                print(f"Aluno encontrado:\nNome: {nome}\nEmail: {email}\nCurso: {curso}\n")
                encontrado = True
                break
        
        if not encontrado:
            print("Aluno não encontrado.")
    except FileNotFoundError:
        print("Nenhum aluno registrado.")

def remover_aluno():
    nome_remover = input("Digite o nome do aluno a ser removido: ")
    
    try:
        with open("alunos.txt", "r") as arquivo:
            alunos = arquivo.readlines()
        
        removido = False
        with open("alunos.txt", "w") as arquivo:
            for aluno in alunos:
                nome, email, curso = aluno.strip().split(",")
                if nome.lower() != nome_remover.lower():
                    arquivo.write(f"{nome},{email},{curso}\n")
                else:
                    removido = True
        
        if removido:
            print(f"Aluno {nome_remover} removido com sucesso!")
        else:
            print("Aluno não encontrado.")
    except FileNotFoundError:
        print("Nenhum aluno registrado.")

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Registar novo aluno")
        print("2. Listar alunos registados")
        print("3. Buscar aluno")
        print("4. Remover aluno")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            registrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            buscar_aluno()
        elif opcao == "4":
            remover_aluno()
        elif opcao == "0":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
