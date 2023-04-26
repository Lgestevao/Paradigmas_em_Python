try:
  num_1 = float(input("Digite o primeiro número: "))
  num_2 = float(input("Digite o segundo número: "))
  num_3 = float(input("Digite o terceiro número: "))
except:
  print("Digite um número!")
if num_3 > num_1 < num_2:
  if num_3 > num_2:
    print(f"A ordem decrescente é: \n 1- {num_1}; \n 2- {num_2}; \n 3- {num_3}.")
  else:
    print(f"A ordem decrescente é: \n 1- {num_1}; \n 2- {num_3}; \n 3- {num_2}.")
elif num_1 > num_2 < num_3:
  if num_1 > num_3:
    print(f"A ordem decrescente é: \n 1- {num_2}; \n 2- {num_3}; \n 3- {num_1}.")
  else:
    print(f"A ordem decrescente é: \n 1- {num_2}; \n 2- {num_1}; \n 3- {num_2}.")
else:
  if num_1 > num_2:
    print(f"A ordem decrescente é: \n 1- {num_3}; \n 2- {num_2}; \n 3- {num_1}.")
  else:
    print(f"A ordem decrescente é: \n 1- {num_3}; \n 2- {num_1}; \n 3- {num_2}.")