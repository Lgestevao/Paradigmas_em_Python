try:
  ano = int(input("Informe um ano de sua escolha: "))
  if ano%4 == 0 and ano%100 != 0:
    print("O ano é bissexto!")
  else:
    print("O ano não é bissexto.")
except:
  print("Digite um número!")