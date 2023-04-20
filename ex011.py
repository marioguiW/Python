altura = float(input("Qual é a altura da parede que deve ser pintada :"))
base = float(input("Qual é a base da parede que deve ser pintada : "))
area = altura * base
tinta = area / 2
print("A area será de {:.2f} e será necessário de {:.2f} Litros de tinta para pintar a parede inteira!".format(area, tinta))