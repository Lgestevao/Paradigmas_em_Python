meses = [
    "janeiro",
    "fevereiro",
    "março",
    "abril",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro",  
]
temperaturas = []
for i in range (12):
    temperaturas.append(float(input(f"Digite a temperatura do mês de {meses[i]} em °C: ")))
  
media = sum(temperaturas) / 12
print(f"A média das temperaturas durante o ano foi de {media:.2f} °C.")
print("\nMeses com a temperatura maior do que a média anual: ")
for i in range (12):
    if temperaturas[i] > media:
        print(f"{i+1} - {meses[i].capitalize()} com {temperaturas[i]:.2f} °C.")