tabuleiro = []

for i in range(10):
    lista = []
    tabuleiro.append(lista)
    for j in range(10):
        lista.append(0)

for i in range(10):
    for j in range(10):
        print(tabuleiro[i][j], end=' ')
    print("")
print(tabuleiro) 

'''

0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0
0 0 3 3 3 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
'''