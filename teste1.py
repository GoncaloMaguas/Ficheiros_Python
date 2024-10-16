def xx(arg):
    print(arg)
    if arg==0:
        return 0
    else:
        return(arg%2) + 10 *xx(arg//2)

a=xx(10)
print(a)
