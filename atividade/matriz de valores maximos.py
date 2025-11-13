matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
matriz2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
 
matriz_final = []
 
 
for i in range(len(matriz)):    
    for j in range(len(matriz)):
        matriz[i][j] = int(input("Digite os valores: "))
 
for i in range(len(matriz2)):    
    for j in range(len(matriz2)):
        matriz2[i][j] = int(input("Digite os valores: "))
for i in range(len(matriz)):
    linha = []
    for j in range(len(matriz[0])):
        if matriz[i][j] > matriz2[i][j]:
            linha.append(matriz[i][j])
        else:
            linha.append(matriz2[i][j])
    matriz_final.append(linha)
print(matriz_final)
