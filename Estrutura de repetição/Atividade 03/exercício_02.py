try:
  numero = []
  par = []
  impar = []
  
  for contador in range (20):
    
    digito = int(input("Digite um número: "))
    numero.append(digito)
    
    if (digito % 2) == 0:
      par.append(digito)
    else:
      impar.append(digito)
      
  print(f"\nLista total de números: {numero}")
  print(f"\nLista de números pares: {par}")
  print(f"\nLista de números ímpares: {impar}")
except:
  print("Tente novamente digitando números.")