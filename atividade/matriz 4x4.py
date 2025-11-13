matriz = [[0]*4]*4
contador = 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        matriz[i][j] = int(input(f"informe o elemento na posicao [{i}] [{j}]"))
        if matriz[i][j]>10:
            contador+=1
        
print(f"os valores maires que dez sao:{contador}")




