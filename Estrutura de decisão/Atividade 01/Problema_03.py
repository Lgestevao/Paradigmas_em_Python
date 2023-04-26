try:
  num = float(input("Digite um número inteiro: "))
  if num > 0:
    calc = num % 4
    if calc == 0:
      print("Este número é par!")
    else:
      print("Este número é ímpar!")
  else:
    print("Só é permitido números positivos")
except:
  print("Tente novamente digitando um número inteiro")