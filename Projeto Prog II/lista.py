def verifica_membro(elemento, lista):
    
    #Verifica se um elemento está presente na lista.
    
    if not lista:
        return 'nao'
    elif elemento == lista[0]:  #elemento encontrado na posição inicial
        return 'sim'
    else:
        #chama a função com a lista reduzida em uma posição
        return verifica_membro(elemento, lista[1:])


def contaRepetido(elemento, lista):
    
    #Conta quantas vezes um elemento aparece na lista.
    
    if not lista:
        return 0
    elif elemento == lista[0]:
        #soma 1 e chama a função com a lista reduzida em uma posição
        return 1 + contaRepetido(elemento, lista[1:])
    else:
        #chama a função com a lista reduzida em uma posição
        return contaRepetido(elemento, lista[1:])


def repetidos(lista):
    
    #Retorna uma lista com os elementos que aparecem duas ou mais vezes na lista original.
    
    if not lista:
        return []
    elif contaRepetido(lista[0], lista) > 1:  #elemento repetido
        #adiciona o elemento à lista de repetidos e chama a função com a lista reduzida sem o elemento repetido
        return [lista[0]] + repetidos([x for x in lista if x != lista[0]])
    else:
        #chama a função com a lista reduzida sem o elemento não-repetido
        return repetidos([x for x in lista if x != lista[0]])


def elementos_comuns(lista1, lista2):
    
    #Retorna uma lista com os elementos comuns às duas listas.
    
    elementos = []
    for elemento in lista1:
        if elemento in lista2:
            elementos.append(elemento)
    return elementos



def maior_elemento(lista):
    
    #Retorna o maior elemento da lista.
    
    if len(lista) == 1:  #caso a lista contenha apenas um elemento
        return lista[0]
    else:
        max_rest = maior_elemento(lista[1:])  #chama a função com a lista reduzida
        #compara o elemento da posição inicial com o maior elemento da lista reduzida
        return lista[0] if lista[0] > max_rest else max_rest

