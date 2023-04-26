lista_pessoas = list()
for contador in range(0, 2):
  nome = str(input("Informe o nome: ")).lower()
  idade = int(input("Informe a idade: "))
  pessoa = list()
  pessoa.append(nome)
  pessoa.append(idade)
  #copiando uma lista x e adicionando dentro de outra
  lista_pessoas.append(pessoa.copy())
  pessoa.clear()
print(lista_pessoas)
lista_pessoas[0].append(89.0)
print(lista_pessoas)