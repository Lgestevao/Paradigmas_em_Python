try:
  operacao = int(input("Escolha a operação: \n 1 - Adição \n 1 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n: Opção: "))
  if 1 <= operacao <= 4:
    try:
      numero1 = int(input("Digite o primeiro número: "))
      numero2 = int(input("Digite o segundo número: "))
      if operacao == 1:
        soma = numero1 + numero2  
        print(f"O valor da soma foi {soma}")
      elif operacao == 2:
        sub = numero1 - numero2
        print(f"O valor da subtração foi {sub}")
      elif operacao == 3:
        mult = 0
        if numero1 != 0 or numero2 != 0:
          mult = numero1 * numero2
        print(f"O valor da Multiplicação foi {mult}")
      elif operacao == 4:
        div = 0
        if numero1 != 0 or numero2 != 0:
          div = round(numero1 / numero2)
        print(f"O valor da Divisão foi {div}")   
    except:
      print("Número inválido")