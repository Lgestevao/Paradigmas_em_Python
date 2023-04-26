try:
  num_1 = float(input("Digite o primeiro lado do triângulo: "))
  num_2 = float(input("Digite o segundo lado do triângulo: "))
  num_3 = float(input("Digite o terceiro lado do triângulo: "))
  if num_1 < num_2 + num_3 and num_2 < num_1 + num_3 and num_3 < num_1 + num_2:
    if (num_1 == num_2 == num_3):
      print("É um triângulo Equilátero!")
    elif (num_1 == num_2 or num_1 == num_3 or num_2 == num_3):
      print("É um triângulo Isósceles!")
    elif (num_1 != num_2 or num_1 != num_3 or num_2 != num_3):
      print("É um triângulo Escaleno!")
  else:
    print("Não é um triângulo. Tente novamente.")
except:
  print("Digite um número!")