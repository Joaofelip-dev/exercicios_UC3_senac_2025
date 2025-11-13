n = int(input("insira o numero da lista:"))
i = 0
a = 0
b = 1
while i < n:
    print(a)
    a,b = b, a+b
    i+=1