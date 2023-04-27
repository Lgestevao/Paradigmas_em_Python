criar_pessoas = dict()
lista_pessoas = list()

for i  in range(1):
  nome = str(input("Informe o nome de uma pessoa: "))
  kg = float(input("Informe o seu peso: "))
  altura = float(input("Informe a sua altura: "))
  IMC = float(kg / (altura)**2)
  criar_pessoas = {
            "nome": nome, 
            "peso": kg, 
            "altura": altura,
            "IMC": IMC
            }
  lista_pessoas.append(criar_pessoas.copy())
  criar_pessoas.clear()

for aux_criar_lista in lista_pessoas:
  print("\n Dados da pessoa:")
  for chave, valor in aux_criar_lista.items():
    print(f"{chave}: {valor}")
  print("\n")  