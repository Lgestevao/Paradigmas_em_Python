try:
  salario = float(input("Digite o valor do seu salário: "))
  if salario < 0:
    print("Não existe salário negativo. Digite novamente.")
  else:
    if 0 < salario <= 280:
      reajuste = salario * 0.20
      salario_novo = salario + reajuste
      print(f"\n O salário antes do reajuste era: R${salario:.2f}.\n O percentual do reajuste aplicado foi de 20%.\n O aumento dado foi de R${reajuste:.2f}.\n O salário reajustado ficou R${salario_novo:.2f}.")
    elif 280 < salario <= 700:
      reajuste = salario * 0.15
      salario_novo = salario + reajuste
      print(f"\n O salário antes do reajuste era: R${salario:.2f}.\n O percentual do reajuste aplicado foi de 15%.\n O aumento dado foi de R${reajuste:.2f}.\n O salário reajustado ficou R${salario_novo:.2f}.")
    elif 700 < salario <= 1500:
      reajuste = salario * 0.10
      salario_novo = salario + reajuste
      print(f"\n O salário antes do reajuste era: R${salario:.2f}.\n O percentual do reajuste aplicado foi de 10%.\n O aumento dado foi de R${reajuste:.2f}.\n O salário reajustado ficou R${salario_novo:.2f}.")
    else:
      reajuste = salario * 0.05
      salario_novo = salario + reajuste
      print(f"\n O salário antes do reajuste era: R${salario:.2f}.\n O percentual do reajuste aplicado foi de 5%.\n O aumento dado foi de R${reajuste:.2f}.\n O salário reajustado ficou R${salario_novo:.2f}.")
except:
    print("O valor do salário só poderá ser dado em números. Digite novamente.")