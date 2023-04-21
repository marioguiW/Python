import math
valor1 = float(input("Digite o valor do cateto oposto :"))
valor2 = float(input("Digite o valor do cateto adjacente :"))
hipotenusa = math.hypot(valor1,valor2)
print("A hipotenusa do triangulo retangulo será de {:.2f}".format(hipotenusa))
