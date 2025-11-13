nomes = ["felipe","alexandre","pedro"]
a=0
e=0
for nome in nomes:# ou for i in range(len(nomes))
    for letra in nome:# for j in range(len(nomes[i]))
        if letra == 'a':#nomes[i][j]=='a'
            a+=1
        elif letra == 'e':#elif[i][j]=='e'
            e+=1
    print(f"O nome {nome} possui {a} 'a' e {e}'e' ") 
