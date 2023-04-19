try:
  nota1 = float(input("Informe a primeira nota: "))
  nota2 = float(input("Informe a segunda nota: "))
  if(nota1 > 0 and nota1 <= 10) and (nota2 > 0 and nota2 <= 10):
    media = (nota1 + nota2) / 2
    if media >= 7 and media < 10:
      print("Aprovado!")
    elif media == 10:
      print("Aprovado com distinção!")
    else:
      print("Reprovado!")
  else:
    print("Inicie novamente e insira uma nota entre 0 à 10")
except:
  print("Só é permitido inserir números, tente novamente")