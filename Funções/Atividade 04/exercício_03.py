dicionario = dict()
lista_dicionario = list()

for i  in range(5):
  item = str(input("Informe nome de um obejto para o dicionário: "))
  
  dicionario = {
            "Item": item
            }
  lista_dicionario.append(dicionario.copy())
  dicionario.clear()

for aux_lista_dicionario in lista_dicionario:
  print("\n Item informado: ")
  for chave, valor in aux_lista_dicionario.items():
    print(f"{chave}: {valor}")
  print("\n")  