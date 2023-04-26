try:
  idade = int(input("Informe a sua idade: "))
  if(idade > 0 and idade <= 120):
    if idade >= 16:
      print("Parabéns! Você já pode votar.")
    else:
      print("Aguarde mais um pouco, você precisa ter pelo menos 16 para poder votar.")
except:
  print("Só é permitido inserir números, tente novamente.")