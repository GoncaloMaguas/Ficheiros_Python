def somade3(x,y,z):
    return x+y+z

def maiorde3(x,y,z):
    if(x>y and x>z):
        return x
    elif(y>x and y>z):
            return y
    elif(z>x and z>y):
        return z

x=float(input("Digite o primeiro valor (X)"))
y=float(input("Digite o segundo valor (y)"))
z=float(input("Digite o terceiro valor (z)"))

print("total= ", somade3(x,y,z))



a=float(input("Digite o primeiro valor (a)"))
b=float(input("Digite o segundo valor (b)"))
c=float(input("Digite o terceiro valor (c)"))

print("o maior numero é:", maiorde3(a,b,c))

