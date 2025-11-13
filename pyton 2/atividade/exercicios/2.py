n = int(input("informe um  numero inteiro:"))
fatorial = n
while n != 1:
    fatorial *= n-1
    n-=1
print(f"o fatorial é {fatorial}:")