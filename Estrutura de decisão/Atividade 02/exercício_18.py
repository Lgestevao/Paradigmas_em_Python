try:
  dia = int(input("Digite um dia à sua escolha: "))
  mes = int(input("Digite um mês à sua escolha: "))
  ano = int(input("Digite um ano à sua escolha: "))
  0 < mes <= 12
  0 < ano
  if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    0 < dia <= 31
    print(f"A sua data é {dia:.f0}/{mes:.f0}/{ano:.f0}")
  elif mes == 2:
    0 < dia <= 28
    print(f"A sua data é {dia:.f0}/{mes:.f0}/{ano:.f0}")
  else:
    0 < dia <= 30
    print(f"A sua data é {dia:.f0}/{mes:.f0}/{ano:.f0}")
except:
  print("Tente novamente digitando a data em formato numérico.")