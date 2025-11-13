matriz = [[1,2,3,4],
          [5,6,7,8],
          [9,1,1,2],
          [6,2,5,1]]

for i in range(len(matriz)):
    for j in range(len(matriz)):
        matriz[i][j] = int(input(f"informe o elemento na posicao [{i}] [{j}]"))
print(matriz)