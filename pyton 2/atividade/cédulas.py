saque = int(input("informe o valore do saque:"))

cedulas_100 = saque // 100
resto = saque % 100
print(f"Cédulas de 100:{cedulas_100}")

cedulas_50 = saque // 50
resto = saque % 50
print(f"Cédulas de 50:{cedulas_50}")

cedulas_20 = saque // 20
resto = saque % 20
print(f"Cédulas de 20:{cedulas_20}")

cedulas_10 = saque // 10
resto = saque % 10
print(f"Cédulas de 100:{cedulas_10}")

cedulas_5 = saque // 5
resto = saque % 5
print(f"Cédulas de 5:{cedulas_5}")

cedulas_2 = saque // 2
resto = saque % 2
print(f"Cédulas de 2:{cedulas_2}")

cedulas_1 = saque // 1
resto = saque % 1
print(f"Cédulas de 1:{cedulas_1}")

