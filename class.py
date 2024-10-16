class UrnaVotacao:
    def __init__(self, candidatos):
        self.candidatos = candidatos
        self.votos = {candidato: 0 for candidato in candidatos}
    
    def votar(self):
        print("Escolha o número do candidato:")
        for i, candidato in enumerate(self.candidatos):
            print(f"{i+1}. {candidato}")
        
        opcao = input("Opção: ")
        try:
            opcao = int(opcao)
            if 1 <= opcao <= len(self.candidatos):
                candidato = self.candidatos[opcao - 1]
                self.votos[candidato] += 1
                print("Voto registrado para o candidato:", candidato)
            else:
                print("Opção inválida. Voto não registrado.")
        except ValueError:
            print("Opção inválida. Voto não registrado.")
    
    def resultados(self):
        for candidato, votos in self.votos.items():
            print("Candidato:", candidato, "| Votos:", votos)

candidatos = ["Candidato A", "Candidato B", "Candidato C"]

urna = UrnaVotacao(candidatos)

while True:
    print("\nMENU DE OPÇÕES:")
    print("1. Votar")
    print("2. Resultados")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        urna.votar()
    elif opcao == "2":
        urna.resultados()
    elif opcao == "3":
        break
    else:
        print("Opção inválida. Tente novamente.")

print("Encerrando o programa.")

