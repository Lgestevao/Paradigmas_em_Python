ELEMENTOS = 10
listaA = []
listaB = []
listas = []

for contador in range(ELEMENTOS):
  listaA.append(int(input(f"Digite o {contador+1}º número da a lista A: ")))
  
for contador in range(ELEMENTOS):
  listaB.append(int(input(f"Digite o {contador+1}º número da a lista B: ")))

for contador in range(ELEMENTOS):
  listas.append(listaA[contador])
  listas.append(listaB[contador])
print("O vetor com os elementos intercalados dos vetores 1 e 2 é: ")
for i in range(ELEMENTOS * 2):
    print(listas[contador], end=" ")