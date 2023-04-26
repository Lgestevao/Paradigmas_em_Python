try:
  lista_numeros = list()
  for contador in range(1):
    if 0 <= contador <= 10:
      lista_numeros.append(float(input("Informe a primeira nota: ")))
      lista_numeros.append(float(input("Informe a segunda nota: ")))
      lista_numeros.append(float(input("Informe a terceira nota: ")))
      lista_numeros.append(float(input("Informe a quarta nota: ")))
      media = sum(lista_numeros) / 4
      print(f"\nMédia de: {media}")
    else:
      print("Informe as notas entre 0 e 10. Tente novamente!")
except:
  print("Só é permitido representar as notas por números. Tente novamente!")