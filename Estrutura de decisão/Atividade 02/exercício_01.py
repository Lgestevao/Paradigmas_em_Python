try:
  num_1 = float(input("Digite o primeiro número: "))
  num_2 = float(input("Digite o segundo número: "))
  if num_1 > num_2:
    print(f"O número {num_1} é o maior entre os dois.")
  else:
    print(f"O número {num_2} é o maior entre os dois.")
except:
  print("Digite um número!")