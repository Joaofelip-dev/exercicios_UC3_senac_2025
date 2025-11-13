user = (input("informe o seu tipo de usuario:"))
pagamento = (input("informe o seu pagamento:"))
idade = int(input("insira a sua idade:"))   

if user == "socio" and pagamento =="em dia" or user == "visitante" and idade>60:
        print("acesso liberado")
elif user == "socio" and pagamento == "atrasado" or user == "visitante" and idade>=18 and idade<=60:
    print("acesso restrito")
else: 
    print("acesso negado")