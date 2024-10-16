a = str(input("Introduza a sua data de nascimento (DD/MM/AAAA): "))
d = a[0:2]
dia = d[::-1]
m = a[3:5]
mes = m[::-1]
ano = a[6:10]
print(m+"$"+dia+"#"+d+"!"+mes+"/"+ano)
