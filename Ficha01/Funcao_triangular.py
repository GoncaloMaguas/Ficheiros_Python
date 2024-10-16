#-----------------------------------------------------------------------------
#* LEIC – Programação II - Ficha de exercício 01
#* Exercício: 2
#* Função: triangular
#* Autor (autores) : 13091, 13092, 13098
#* Data: 08/03/2023
#-----------------------------------------------------------------------------

def triangular(n):
    i = 1
    while i * (i+1) * (i+2) < n:
        i = i + 1

    if i * (i+1) * (i+2) == n:
        return True
    else:
        return False

n = int(input("Introduza um valor: "))
print(triangular(n))
