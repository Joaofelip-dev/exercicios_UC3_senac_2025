saldo = 1500
saque = float(input("Digite o valor do saque: "))

if saque > saldo:
    print("Saldo insuficiente.")
elif saque < 0:
    print("Valor inválido.")
elif saque == 0:
    print("Nenhum valor sacado.")
else:
    saldo -= saque
    print("Saque realizado com sucesso. Seu novo saldo é:", saldo)
 
 