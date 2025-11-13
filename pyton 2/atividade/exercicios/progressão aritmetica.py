termo = int(input("Digite o termo da progressão:"))
razao = int(input("Digite o termo da progressão:"))
quantidade = int(input("Digite a quantidade de termos:"))
tipo = input("Digite 'A' para PA e 'G' para PG:")
i = 0
while quantidade>i:
    print(termo)
    if tipo == 'A':
        termo+=razao
    elif tipo=='G':
        termo*=razao
    i+=1