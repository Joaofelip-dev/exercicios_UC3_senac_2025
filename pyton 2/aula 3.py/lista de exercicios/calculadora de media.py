n1 = float(input("insira a sua nota:"))
n2 = float(input("insira a sua segunda nota:"))
média = (n1+n2)/2
if média>=7:
    print(média,"aprovado")
elif média>=5 and média<=6.9:
    print(média,"recuperação")
else:
    print(média,"reprovado")