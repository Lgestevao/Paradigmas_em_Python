try:
  idade = int(input("Informe a sua idade: "))
  genero = str(input("Informe o seu gênero através das sigla M ou F: ")).upper

  if idade > 0:
    if genero == "M" or genero == "F":
      if (genero == "M" and idade >= 65) or (genero == "F" and idade >= 60):
        print("Muito bem. Você pode se aposentar")
      else:
        print("Informe um gênero correto.")
    else:
      print("Informe uma idade válida.")

except:
  print("Idade inválida. Tente novamente.")