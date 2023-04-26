turno = input("Escolha uma das opções sobre qual turno você estuda e digite: \n 1 - M - Matutino. \n 2 - V - Vespertino. \n 3 - N - Noturno. \n Opção: ")
match turno:
  case "M":
    print("Bom dia!")
  case "V":
    print("Boa tarde!")
  case "N":
    print("Boa noite!")