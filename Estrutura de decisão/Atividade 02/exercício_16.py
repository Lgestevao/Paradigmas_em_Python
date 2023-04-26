try:
  a = float(input("Digite o valor de a: "))
  b = float(input("Digite o valor de b: "))
  c = float(input("Digite o valor de c: "))
  if a == 0:
    print("A equação não é do segundo grau. Tente novamente.")
  else:
    delta = (b)**2 - 4 * a * c
    x1 = (-b (+ delta**(1/2))) / (2 * a)
    x2 = (-b (- delta**(1/2))) / (2 * a)    
    if delta < 0:
      print("A equação não possui raizes reais. Tente novamente.")
    else:
      print(f"A equação possui as duas raizes reais, sendo X1 = {x1:.2f} e X2 = {x2:.2f}")
      if delta == 0:
        x1 = -b / (2 * a)
        print(f"A equação possui apenas uma raiz real, sendo ela = {x1:.2f}")
except:
  print("Digite um número!")