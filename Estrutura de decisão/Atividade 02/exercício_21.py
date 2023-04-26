#O caso será para o dado de entrada de R$256,00 e R$399,00.
try:
  vlr = int(input("As notas disponíveis no caixa são: \n \n R$1,00 - R$5,00 - R$10,00 - R$50,00 - R$100,00. \n \nInforme o valor que deseja sacar: "))
  10 <= vlr <= 600
  match vlr:
    case 256:
      print(f"\nPara R${vlr}, serão duas notas de R$100,00, uma nota de R$50,00 e uma nota de R$1,00.")
    case 399:
      print(f"\nPara R${vlr}, serão três notas de R$100,00, uma nota de R$50,00, quatro notas de R$10,00, uma nota de R$5,00 e quatro notas de R$1,00.")
except:
  print("\nDigite um valor! Tente novamente.")