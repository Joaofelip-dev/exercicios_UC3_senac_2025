lista = [1,8,3,7]

for i in range(len(lista)):
    for j in range(len(lista)-i-1):
        if lista[j]>lista[j+1]:
            lista[j],lista[j+1]=lista[j+1],lista[j]
print(lista)
    