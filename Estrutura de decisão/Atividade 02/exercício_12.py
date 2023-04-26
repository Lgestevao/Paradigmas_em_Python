try:
  qtd_horas = int(input("Informe quantas horas trabalhou: "))
  if qtd_horas >= 20:
    vl_hora = int(input("Informe o valor da hora: "))
    salario = qtd_horas * vl_hora
    if salario <= 900:
      pass
    elif salario > 900 and salario <= 1500:
      pass
    elif salario > 1500 and salario <= 2500:
      pass
    else:
      pass
  else:
    print("Quantidade mínima de horas trabalha tem que ser maior que 20 horas.")
except:
  print("Houve um erro!")