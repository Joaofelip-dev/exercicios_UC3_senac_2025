lista = []
for i in range(1,11,1):
    lista.append(int(input(f"digite o {i} valor:")))

menor = lista[0]
for i in range(len(lista)):
    if lista[i] < menor:
            menor = lista[i]

print(f"o menor numero é {menor}")