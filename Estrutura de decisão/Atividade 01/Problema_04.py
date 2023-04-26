try:
  num1 = float(input("Digite o primeiro número para a operação: "))
  num2 = float(input("Digite o segundo número para a operação: "))
  oper = input("Qual operação você deseja fazer? Digite uma entre as quatros operações: Soma, subtração, divisão ou multiplicação. ")
  if (oper == soma):
    soma == num1 + num2
    print("Você escolheu a soma! O resultado da operação é: ", result)
    if (oper == subtração):
      sub == num1 - num2
      print("Você escolheu a subtração! O resultado da operação é: ", result)
      if (oper == divisão):
        divisão == num1 % num2
        print("Você escolheu a subtração! O resultado da operação é: ", result)
        if (oper == multiplicação):
          multiplicação == num1 * num2
          print("Você escolheu a multiplicação! O resultado da operação é: ", result)
  else:
    print("Escolha uma das quatros operações matemáticas e tente novamente")
except:
  print("Escolha uma das quatros operações matemáticas e tente novamente")