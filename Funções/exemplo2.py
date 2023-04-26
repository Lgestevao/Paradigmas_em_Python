#delcamando uma função com paramentros e retorno
def somar_numeros(num1, num2):
  soma = num1 + num2
  return soma

#testar função com parametros e retorno
"""for i in range(0, 3):
  num1 = in(input("n1: "))
  num2 = in(input("n2: "))
  result = somar_numeros(num1, num2)
  print(result)"""

#declamando uma função com parametros e sem retorno
lista_numeros = list()
def cadastrar_numero(numero):
  lista_numeros.append(numero)

#testar função com parametros e sem retorno
for i in range(0, 3):
  numero = input("add numero: ")
  print(type(numero))
  #is digit verfica se é um numero, função com retorno True ou False
  if numero.isdigit() == True:
    #realizando um type cast de string para inteiro
    numero = int(numero)
    cadastrar_numero(numero)
    print(type(numero))
print(lista_numeros)