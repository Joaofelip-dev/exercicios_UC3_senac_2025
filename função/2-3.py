numero_secreto = int(input("Tente adivinhar o numero secreto:"))

while numero_secreto!=7:
   if numero_secreto>7:
      numero_secreto = int(input("Tente um numero menor"))
      
   if numero_secreto<7:
        numero_secreto = int(input("tente um  numero maior"))
        
      
