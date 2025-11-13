senha = input("Digite uma senha que tenha 1 letra maiúscula e 1 número: ")
while True:
    tem_maiuscula = False
    tem_numero = False
    # Usando for para verificar cada caractere
    for caractere in senha:
        if caractere in "QWERTYUIOPASDFGHJKLZXCVBNM":
            tem_maiuscula = True
        elif caractere in "1234567890":
            tem_numero = True
    # Verificando com if/else
    if tem_maiuscula and tem_numero:
        print("Senha válida!")
        break
    else:
        print("senha invalida!")
        break
        