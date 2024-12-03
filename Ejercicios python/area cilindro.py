#Cilindro
radio = float(input("ingrese radio:"))
altura = float(input("ingrese altura: "))
from math import pi
area_de_bases = round(pi*radio**2,2)
area_de_lateral = round(2*pi*radio*altura,2)
area_total = round(2*area_de_bases+area_de_lateral,2)
volumen = area_de_bases*altura
print("El area de las bases es",area_de_bases)
print("el area de los laterales es",area_de_lateral)
print("el area total es ",area_total)
print("el volumen es",volumen)