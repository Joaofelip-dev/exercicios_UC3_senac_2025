sexo = (input("Qual é o seu sexo ?"))
A = float(input("Qual a sua altura ?"))
M = "Masculino"
F = "Feminino"
if M and A>=1.70:
    print("Apta")
elif F and A>=1.60:
    print("Apta")
else:
    print("Inapta")

