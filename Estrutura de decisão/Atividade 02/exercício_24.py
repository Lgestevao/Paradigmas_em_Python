try:
  numero1 = float(input("Digite o primeiro número: "))
  numero2 = float(input("Digite o segundo número: "))
  operacao = int(input("\nEscolha a operação: \n 1 - Adição \n 1 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n \nOpção: "))
  if 1 <= operacao <= 4:
    try:
      match operacao:
        case 1:
          soma = numero1 + numero2  
          print(f"O valor da soma foi {soma}.")
          if soma % 2 == 0:
            print("É um número par!")
          else:
            print("É um número ímpar!")
          if soma > 0:
            print("É um número positivo!")
          else:
            print("É um número negativo!")
          if soma % 1 == 0:
            print("É um número inteiro!")
          else:
            print("É um número decimal!")
        case 2:
          sub = numero1 - numero2
          print(f"O valor da subtração foi {sub}")
          if sub % 2 == 0:
            print("É um número par!")
          else:
            print("É um número ímpar!")
          if sub > 0:
            print("É um número positivo!")
          else:
            print("É um número negativo!")
          if sub % 1 == 0:
            print("É um número inteiro!")
          else:
            print("É um número decimal!")
        case 3:
          mult = 0
          if numero1 != 0 or numero2 != 0:
            mult = numero1 * numero2
          print(f"O valor da Multiplicação foi {mult}")
          if mult % 2 == 0:
            print("É um número par!")
          else:
            print("É um número ímpar!")
          if mult > 0:
            print("É um número positivo!")
          else:
            print("É um número negativo!")
          if mult % 1 == 0:
            print("É um número inteiro!")
          else:
            print("É um número decimal!")
        case 4:
          div = 0
          if numero1 != 0 or numero2 != 0:
            div = (numero1 / numero2)
          print(f"O valor da Divisão foi {div}")  
          if div % 2 == 0:
            print("É um número par!")
          else:
            print("É um número ímpar!")
          if div > 0:
            print("É um número positivo!")
          else:
            print("É um número negativo!")
          if div % 1 == 0:
            print("É um número inteiro!")
          else:
            print("É um número decimal!")
    except:
      print("Número inválido")
except:
  print("Tente novamente.")