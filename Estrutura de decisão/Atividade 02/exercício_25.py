try:
  print("Respoda as perguntas com SIM ou Não. \n")
  perg1 = str(input("Telefonou para a vítima? ")).upper()
  perg2 = str(input("Esteve no local do crime? ")).upper()
  perg3 = str(input("Mora perto da vítima? ")).upper()
  perg4 = str(input("Devia para a vítima? ")).upper()
  perg5 = str(input("Já trabalhou com a vítima? ")).upper()

  soma_perg = 0
  if perg1 == "SIM":
    soma_perg += 1
    
  if perg2 == "SIM":
    soma_perg += 1
    
  if perg3 == "SIM":
    soma_perg += 1
    
  if perg4 == "SIM":
    soma_perg += 1
    
  if perg5 == "SIM":
    soma_perg += 1
    
  match soma_perg:
    case 0:
      print("Inocente!")
    case 1:
      print("Inocente!")
    case 2:
      print("Supeita!")
    case 3:
      print("Cúmplice!")
    case 4:
      print("Cúmplice!")
    case 5:
      print("Assassino!")
except:
  print("Tente novamente respondendo SIM ou Não.")