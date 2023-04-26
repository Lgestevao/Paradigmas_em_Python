try:
  nota1 = float(input("Informe a primeira nota: "))
  nota2 = float(input("Informe a segunda nota: "))
  nota3 = float(input("Informe a terceira nota: "))
  
  if (nota1 > 0 and nota1 <= 10) and (nota2 > 0 and nota2 <=10)  and (nota3 > 0 and nota3 <=10):
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7 and media < 10:
      print("Aprovado!")
    elif media == 10:
      print("Aprovado com Distinção!")
    else:
      print("Reprovado!")
  else:
    print("Notas inválidas!")
except ValueError:
  print("Só é permitido números. Tente novamente!")