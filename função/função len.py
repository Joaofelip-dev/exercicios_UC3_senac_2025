lista = [1,2,3,4,5,6,7,8,8,10]
def tamanho(lista):
    contador = 0
    for i in lista:
        contador +=1
    return contador
print(tamanho(lista))