n = float(input("informe a sua nota:"))
soma = n
contador = 1
while n>0:
    n = float(input("informe a sua nota:"))
    while n>10:
        print("nota invalida tente novalmente.")
        n = float(input("informe a sua nota:"))
    if n>0:
        soma+=n
        contador+=1
media = soma/contador
print(f" a soma das notas é: {soma}")
print(f"a media das notas é:{media}")
