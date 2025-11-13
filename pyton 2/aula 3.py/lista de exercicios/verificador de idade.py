idade = int(input("informe a sua idade:"))
if idade>=18 and idade<=69:
    print("voto obrigatorio")
elif idade>=16 and idade<=17 or idade>=70:
    print("Voto opcional")
elif idade<16:
    print("não pode votar")