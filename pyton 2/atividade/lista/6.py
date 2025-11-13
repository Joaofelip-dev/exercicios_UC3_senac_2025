texto = "programaçao com python e fantastica"
 
contador = 0
 
for i in range(len(texto)):
    if texto[i] == "a":
        contador += 1
print(f"a quantidade de letra a e de:{contador}")