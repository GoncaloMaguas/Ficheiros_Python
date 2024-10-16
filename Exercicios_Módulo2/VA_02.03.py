mes=str(input("Introduza um mês do ano: "))

if (mes=="Janeiro" or mes=="Março" or mes=="Maio" or mes=="Julho" or mes=="Agosto" or mes=="Outubro" or mes=="Dezembro"):
    print(mes, "tem 31 dias")
elif (mes=="Fevereiro"):
        print(mes, "tem 28 dias")

elif (mes=="Abril" or mes=="Junho" or mes=="Setembro" or mes=="Novembro"):
            print(mes, "tem 30 dias")

else:
    print("Mês não reconhecido")
