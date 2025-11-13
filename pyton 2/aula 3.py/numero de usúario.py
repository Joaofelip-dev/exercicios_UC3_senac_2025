n1= int(input("informe o seu numero de usuario:"))
n2 = int(input("informe o seu numero de usuario:"))
n3 = int(input("informe o seu numero de usuario:"))

if n1>n2>n3:
    print("o maior numero é:",n1)
elif n2>n1>n3:
    print("o maior numero é:",n2)
elif n3>n2>n1:
    print("o maior numero é:",n3)

if n1<n2<n3:
    print("o menor numero é:",n1)
elif n2<n3<n1:
    print("o menor numero é:",n2)
elif n3<n2<n1:
    print("o menor numero é:",n3)
