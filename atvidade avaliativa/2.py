nivel_acesso = (input("Informe o seu nivel de acesso:"))
pontuação = int(input("Informe a sua pontuação:"))

if nivel_acesso == "Administrador" and pontuação>750:
    print("Acesso Liberado. Bem-vindo(a)!")
elif nivel_acesso == "premium" and pontuação>750:
    print("Acesso Liberado. Bem-vindo(a)!")
else:
    print("Acesso Negado: Nível de acesso não autorizado.")