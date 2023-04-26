try:
  num = int(input("Digite um número entre 0 e 1000: "))
  if 0 < num < 1000:
    if num % 4 == 0:
      print("Este número é divisível por 4!")
    else:
      print("Este número não é divisível por 4!")
  else:
    print("Número fora do range, tente novamente.")
except:
  print("Tente novamente digitando um número válido!")