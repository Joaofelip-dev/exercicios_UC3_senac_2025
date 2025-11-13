matriz = [
    [12, 17, 90, 65, 43],
    [55, 456, 60, 50, 14],
    [0, 98, 90, 24, 26],
    [7, 10, 11, 56, 36],
    [46, 75, 45, 30, 0]
]

x = int(input("Digite o valor a ser pesquisado: "))
 
encontrado = False
 
for i in range(5):
    for j in range(5):
        if matriz[i][j] == x:
            print(f"Valor {x} encontrado na posição: linha {i}, coluna {j}")
            encontrado = True

if encontrado == False:
    print("Valor não encontrado na matriz.")
else:
    print("Busca concluída.")