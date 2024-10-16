#-----------------------------------------------------------------------------
#* LEIC – Programação II - Ficha de exercício 01 
#* Exercício: 1
#* Função: primo
#* Autor (autores) : 13091, 13092, 13098
#* Data: 08/03/2023
#-----------------------------------------------------------------------------




def primo(x) : 


    if (x <= 1) : 
        return False
    if (x <= 3) : 
        return True  
    if (x % 2 == 0 or x % 3 == 0) : 
        return False
    i = 5
    while(i * i <= x) : 
        if (x % i == 0 or x % (i + 2) == 0) : 
            return False
        i = i + 6
    return True

n=int(input("Digite um número inteiro: "))
 
 
print(primo(n))
