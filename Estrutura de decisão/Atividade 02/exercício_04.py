letra = input("Digite uma letra: ")
if letra.isalpha():
  if (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
    print("A letra escolhida é uma vogal!")
  else:
    print("A letra escolhida é uma consoante")
else:
  print("Digite uma letra!")