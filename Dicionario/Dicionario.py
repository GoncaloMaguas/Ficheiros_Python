import statistics

Produtos={
    "Salgado":4.50, "Lanche": 6.50, "Suco": 3.00, "Refrigerante": 3.50, "Doce": 1.00, "Quente": 4.00
    }

print(Produtos["Salgado"])

total=sum(Produtos.values())

print("A média dos preços é: ", total/len(Produtos.values()))
media = statistics.mean(Produtos.values())
print("A média dos preços é: ",media)
