#declarando uma lista
lista_numeros = list()

#adicionando elementos
lista_numeros.append(5)
lista_numeros.append(6)
lista_numeros.append("8")
print("Lista de números: ",lista_numeros)
print("Verificar o tipo: ",type(lista_numeros))

#pegando  objeto pela posição
num_pos_2 = lista_numeros[2]
print("\nQuem está na posição 2?", num_pos_2)
print("\nQual o tipo do obj da posição 2?", type(num_pos_2))

#acessando todos os objets da lista usando o for objeto in lista
print("\nAcessando todos os objetos da lista usando for obj in lista")
for numero in lista_numeros:
  print(numero)

#adicionar elementos pela posição
posicao = 0
novo_numero = 10
print("\nAdicionando um obj em uma posição específica")
lista_numeros.insert(posicao, novo_numero)
print("Lista de números", lista_numeros)

print("\nTentando adicionar em uma posição inexistente negativa")
lista_numeros.insert(-6, 2)
print("Lista de números: ",lista_numeros)
print("\nTentando adicionar em uma posição inexistente maior do que existe")
lista_numeros.insert(8, 2)
print("Lista de números: ",lista_numeros)

#remover objeto
try:
  lista_numeros.remove("8")
  print("\nLista de números: ", lista_numeros)
  print("Removido com sucesso!")
except ValueError:
  print("\nNão foi possível remover o objeto porque ele não existe!")

#ordenar uma lista
print("\nOrdenando do menor para o maior")
lista_numeros.sort()
print("Lista de números: ", lista_numeros)
print("\nOrdenando do maior para o menor")
lista_numeros.reverse()
print("Lista de números: ", lista_numeros)

#removendo o ultimo objeto
print("\nRemovendo o último objeto")

#usando a função pop sem parametros remove ao final
lista_numeros.pop()
print("Lista de números: ", lista_numeros)

#removendo por uma posição específica usando o pop
#e passando a posiçã como parametro
print("\nRemovendo o objeto pela posição: ")

try:
  lista_numeros.pop(6)
  print("Lista de números: ", lista_numeros)
  print("Removido com sucesso!")
except IndexError:
  print("Não foi possível remover o objeto porque sua posição não foi encontrada!")

lista_numeros.append(5)
lista_numeros.append(6)
lista_numeros.append(5)
lista_numeros.append(6)
print("\nLista de números: ", lista_numeros)
#buscando um objeto e achando a sua posição
print("\nAchando um objeto por sua posição, procurando o nº 2: ")
#O index recebe o objeto e te retorna a sua respectiva posição
#se houver objetos repetidos ele retorna o primeiro que encontrar
posicao_obj = lista_numeros.index(2)
print("Qual a posição entranda? ", posicao_obj)