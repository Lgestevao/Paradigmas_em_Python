try:
  numero = []

  for i in range(5):

    digito = int(input("Digite um número: "))
    numero.append(digito)
#função sum para somar os números da lista.
    soma = numero[0] + numero[1] + numero[2] + numero[3] + numero[4]
    
    mult = numero[0] * numero[1] * numero[2] * numero[3] * numero[4]
    
  print(f"\nNúmeros da lista: {numero}")
  print(f"\nSoma dos números da lista: {soma}")
  print(f"\nMultiplicação dos números da lista: {mult}")
except:
  print("Tente novamente digitando números.")