l1 = int(input("onforme o lado 1:"))
l2 = int(input("informe o lado 2:"))
l3 = int(input("informe o lado 3:"))

if l1+l2>l3:
    print("triângulo")
else: 
    print("não é triângulo")
if l1 == l2 == l3:
    print("triângulo Equilátero")
elif l1==l2 or l1==l3 or l3==l1 or l3==l2 or l2==l1 or l1==l2 or l2==l3:
    print("triângulo Isóseles")
elif l1!=l2!=l3:
    print("triângulo Escaleno")