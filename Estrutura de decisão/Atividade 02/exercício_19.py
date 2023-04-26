try:
  num = int(input("Digite um número 1 à 999: "))
  if num < 0 or num > 999:
    print("O número deve estar entre 1 e 999. Tente novamente.")
  else:
    centena = num/100
    dezena = num/10
    unidade = num/1
    print(f"O número escolhido foi {num:.0f}. \n {num:.0f} = {centena:.0f} centenas, {dezena:.0f} dezenas e {unidade:.0f} unidades.")
except:
  print("Tente novamente. Digite um número.")