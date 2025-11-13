temperaturas = [28.5, 30.1, 26.9, 31.8, 27.5, 29.3, 32.0, 25.8]
dias_acima_da_media = 0

for i in temperaturas:
    if i>29.0:
        dias_acima_da_media+=1
print(f"Lista de temperaturas {temperaturas}")
print(f" número total de dias que tiveram a temperatura acima de 29.0°C: {dias_acima_da_media}")