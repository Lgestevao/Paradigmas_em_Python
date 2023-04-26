try:
  num_1 = float(input("Digite o preço do primeiro produto: "))
  num_2 = float(input("Digite o preço do segundo produto: "))
  num_3 = float(input("Digite o preço do terceiro produto: "))
except:
  print("Digite um número!")
if num_3 < num_1 > num_2:
  if num_3 > num_2:
    print("Você deve comprar o segundo produto!")
  else:
    print("Você deve comprar o terceiro produto!")
elif num_1 < num_2 > num_3:
  if num_1 > num_3:
    print("Você deve comprar o terceiro produto!")
  else:
    print("Você deve comprar o primeiro produto!")
else:
  if num_1 > num_2:
    print("Você deve comprar o segundo produto!")
  else:
    print("Você deve comprar o primeiro produto!")