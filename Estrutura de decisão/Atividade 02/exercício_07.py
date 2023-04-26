try:
  num_1 = float(input("Digite o primeiro número: "))
  num_2 = float(input("Digite o segundo número: "))
  num_3 = float(input("Digite o terceiro número: "))
except:
  print("Digite um número!")
if num_3 < num_1 > num_2:
  print(f"O primeiro número, {num_1}, é o maior entre os três.")
  if num_3 > num_2:
    print(f"E o segundo número, {num_2}, é o menor entre os três.")
  else:
    print(f"E o terceiro número, {num_3}, é o menor entre os três.")
elif num_1 < num_2 > num_3:
  print(f"O segundo número, {num_2}, é o maior entre os três.")
  if num_1 > num_3:
    print(f"E o terceiro número, {num_3}, é o menor entre os três.")
  else:
    print(f"E o primeiro número, {num_1}, é o menor entre os três.")
else:
  print(f"O terceiro número, {num_3}, é o maior entre os três.")
  if num_1 > num_2:
    print(f"E o segundo número, {num_2}, é o menor entre os três.")
  else:
    print(f"E o primeiro número, {num_1}, é o menor entre os três.")