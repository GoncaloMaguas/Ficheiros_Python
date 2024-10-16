F = (100, "Joana Silva", "A", 110, "Telmo Costa", "B", 120, "Rui Velez", "C", 130, "Rosa Pais", "D")

# Cria a lista de tuplas
lista_tuplas = []
for i in range(0, len(F), 3):
    tupla = (F[i], F[i+1], F[i+2])
    lista_tuplas.append(tupla)

print(lista_tuplas)
