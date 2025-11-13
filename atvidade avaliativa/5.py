vendas = [ 

    [1200, 1500, 1000],  # Vendedor A 

    [2100, 1900, 2500],  # Vendedor B 

    [900, 1400, 1100]    # Vendedor C 

] 
vendas_total = 0
vendas_B = 0 
for i in range(len(vendas)):
    for j in range(len(vendas)):
        vendas_total+=vendas[i][j]
for v in vendas[1]:
    vendas_B+=v
print(f"O valoor total de vendas é: {vendas_total}")
print(f"O valor de vendas do vendedor b é: {vendas_B}")
