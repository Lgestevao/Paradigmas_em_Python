criar_pessoas = dict()
lista_pessoas = list()

for i  in range(0, 2):
  nome = str(input("Informe o nome de uma pessoa: "))
  cpf = str(input("Informe o CPF: "))
  idade = str(input("Informe a idade: "))
  criar_pessoas = {
            "nome": nome, 
            "cpf": cpf, 
            "idade": idade
            }
  lista_pessoas.append(criar_pessoas.copy())
  criar_pessoas.clear()

for aux_criar_lista in lista_pessoas:
  print("Cadastro criado:\n")
  for chave, valor in aux_criar_lista.items():
    print(f"{chave}: {valor}")
  print("\n")  