total = float(input("Informe o valor toal das compras:"))
pagamento = input("forma de pagamento 1 (a vista), forma de pagamento 2 (cartão de credito, forma de pagamento 3 (parcelado). )")
à_vista = total-(total*10)/100
parcelado = (total*5)/100+total

if pagamento == "1":
    print(f"o valor total é de {à_vista})")
elif pagamento == "2":
    print(f"o valor total é de {total}")
elif pagamento == "3":
    print(f"o valor total é de {parcelado}")
else:
    print("formato invalido")