lista_pessoas = list()
def cadastrar_pessoa(pessoa):
  lista_pessoas.append(pessoa)

#testando o cadastro de pessoas
for i  in range(0, 1):
  nome = "Guzinho"
  cpf = "000"
  idade = 13
  pessoa = {
            "nome": nome, 
            "cpf": cpf, 
            "idade": idade
  }
  cadastrar_pessoa(pessoa)
  nome = "Guzinho 2"
  cpf = "000"
  idade = 13
  pessoa = {
            "nome": nome, 
            "cpf": cpf, 
            "idade": idade
  }
  cadastrar_pessoa(pessoa)
  
"""for i  in range(0, 2):
  nome = str(input("Informe seu nome: ")).upper()
  cpf = input("Informe seu cpf:")
  idade = int(input("Informe a sua idade:"))
  pessoa = {
            "nome": nome, 
            "cpf": cpf, 
            "idade": idade
  }
  cadastrar_pessoa(pessoa)"""
print(lista_pessoas)
#listando pessoas
for pessoa in lista_pessoas:
  print(f"Nome: {pessoa['nome']}\n CPF: {pessoa['cpf']}\n  Idade:{pessoa['idade']}")