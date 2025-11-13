def taxa_importação(valor):
    if valor<=50:
        imposto=valor*0.20
        icms = (valor + imposto)*0.20
        return valor+imposto+icms
    else:
        imposto = (valor * 0.60) - 20
        icms = (valor + imposto) * 0.20
        return valor+imposto+icms
print(taxa_importação(995.73))

