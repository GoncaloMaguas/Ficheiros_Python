a = str(input("Introduza uma palavra: "))

tam = len(a)
val = tam//2

print("#"+a[:val]+"#"+a[val:]+"#")
