try:
  num = float(input("Digite o primeiro número: "))
  if num < 0:
    print(f"O número {num} é negativo.")
  else:
    print(f"O número {num} é positivo.")
except:
  print("Digite um número!")