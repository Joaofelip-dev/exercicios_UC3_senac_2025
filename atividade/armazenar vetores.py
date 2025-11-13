nome = []
n1 = []
n2 = []
media = []
situacao = []

for i in range(6):
    nome.append(input("informe o seu nome:"))
    n1.append(float(input("informe a primeira nota;")))
    n2.append(float(input("informe a segunda nota:")))
    media.append((n1[i]+n2[i]/2))
    if media[i]>=5:
        situacao.append("aprovado")
    else:
        situacao.append("reprovado")
print(nome,n1,n2,media,situacao)



