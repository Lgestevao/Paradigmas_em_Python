try:
  num = float(input("Digite o um número: "))
  if num % 1 == 0:
    print("O número é inteiro!")
  else:
    print("O número é decimal!")
except:
  print("Digite um número!")