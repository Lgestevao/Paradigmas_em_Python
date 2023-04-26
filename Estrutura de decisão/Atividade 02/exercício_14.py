try:
  num_1 = float(input("Digite o primeiro número: "))
  num_2 = float(input("Digite o segundo número: "))
  if 0 < num_1 and 0 < num_2:
    media = (num_1 + num_2) / 2
    if 9 <= media <= 10:
      print(f"Aprovado! Você tirou 'A'! Sua média foi {media:.2f}.")
    elif 7.5 <= media < 9:
      print(f"Aprovado! Você tirou 'B'! Sua média foi {media:.2f}.")
    elif 6 <= media < 7.5:
      print(f"Aprovado! Você tirou 'C'! Sua média foi {media:.2f}.")
    elif 4 <= media < 6:
      print(f"Reprovado! Você tirou 'D'! Sua média foi {media:.2f}.")
    else:
      print(f"Reprovado! Você tirou 'E'! Sua média foi {media:.2f}.")
  else:
    print("Digite um número entre 0 e 10 para sua nota.")
except:
  print("Digite um número!")