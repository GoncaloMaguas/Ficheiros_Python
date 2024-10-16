def somatorio(calc_termo, linf, prox,lsup):
    soma=0
    while linf<=lsup:
        soma=soma+calc_termo(linf)
        linf=prox(linf)
    return soma

somatorio(lambda x : somatório(lambda x: x, 1, lambda x: x+1, x))


somatorio(1,2,3)
