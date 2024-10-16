palavra=str(input("Introduza uma string:"))

a=palavra[0]
b=palavra[1]
c=palavra[-2]
d=palavra[-1]


print(palavra,end=(""))
count=0

while count<4:
    print(a+b+c+d,end=(""))
    count+=1

