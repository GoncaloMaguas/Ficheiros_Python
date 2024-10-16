def contar(tuplo, numero):

    count = 0
    for n in tuplo:
        if n == numero:
            count += 1
    return count


def pares(tuplo):
    for n in tuplo:
        if n % 2 != 0:
            return False
    return True

t=(2,2,4,6,8)

print(contar(t,2))


print(pares(t))



