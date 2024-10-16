frase = "                  !!!!!!   Olá, mundo!!!!!!\n\n\nola\n\nhey\n"
caracteres_indesejados = " "
print(frase)
palavras=[]

for linha in frase:
    linha.strip()
    palavras.append(linha)


print(palavras)  # Saída: "Olá, mundo"
