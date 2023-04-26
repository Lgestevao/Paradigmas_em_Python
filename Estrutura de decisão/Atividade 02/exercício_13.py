try:
  dia = int(input("Digite de 1 à 7 para escolher um dia da semana, começando por domingo: "))
  if dia == 1:
    print("\n Domingo!")
  elif dia == 2:
    print("\n Segunda!")
  elif dia == 3:
    print("\n Terça!")
  elif dia == 4:
    print("\n Quarta!")
  elif dia == 5:
    print("\n Quinta!")
  elif dia == 6:
    print("\n Sexta!")
  elif dia == 7:
    print("\n Sábado!")
  else:
    print("\n Número inválido. Digite um número entre 1 e 7.")
except:
  print("\n Só é perminito a entrada do dado com números. Tente novamente.")