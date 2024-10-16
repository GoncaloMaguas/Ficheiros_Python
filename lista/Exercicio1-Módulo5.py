l=[1,4,3,2]

print(len(l))

print(max(l))

print(min(l))

print(sum(l))

l.sort()
print(l)

l.reverse()
print(l)
i=0
count=3

l=list(range(0,51,3))
del l[0]
print(l)


l=[]
while count<50:
    if(count%3==0):
        l.append(count)
        count=count+1
        i=i+1

    else:
        count=count+1


print(l)
