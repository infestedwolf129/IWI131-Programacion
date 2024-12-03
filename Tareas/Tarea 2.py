
NN = float(input("Nevarro Nummies consumidas (en unidades): "))
SS = float(input("Space Soup consumida (en [ml]): "))
CR = float(input("Carne de rana consumida (en [g]): "))

#ingresamos lo equivalente a gramos de: grasas,carbohidratos y proteínas por cada comida 
#NN es Nevarro Nummies
grasas_NN= 1.90*NN*11
carbohidratos_NN= 6.00*NN*11
proteínas_NN= 0.80*NN*11

#SS es Space Soup
grasas_SS=10.0*SS
carbohidratos_SS= 12.0*SS
proteínas_SS= 11.0*SS

#CR es Carne de rana
#En el caso de la Carne de Rana omitimos los carbohidratos
grasas_CR= 0.30*CR
proteínas_CR= 16.0*CR

#Se suman las grasas, los carbohidratos y las proteínas para dar el total en cada una
grasa_total = round(((grasas_NN/11)+(grasas_SS/285)+(grasas_CR/100)),2)
carbohidratos_total = round(((carbohidratos_NN/11)+(carbohidratos_SS/285)),2)
proteínas_total = round(((proteínas_NN/11)+(proteínas_SS/285)+(proteínas_CR/100)),2)

print("Grogu a consumido:")
print(grasa_total, "[g] de grasas")
print(carbohidratos_total, "[g] de carbohidratos")
print(proteínas_total, "[g] de proteínas")

#Multiplicamos cada una por su equivalente en calorias
calorías= round(grasa_total*9+carbohidratos_total*4+proteínas_total*4)
print("dando un total de: ")
print(calorías,"[calorías]")

'''
CASO DE PRUEBA #1
NN == 2
SS == 310
CR == 150
RESULTADO:
15.13 [g] de grasas
25.05 [g] de carbohidratos
37.56 [g] de proteínas
387 [calorías]

CASO DE PRUEBA #2
NN == 3.1
SS == 180
CR == 400
RESULTADO:
13.41 [g] de grasas
26.18 [g] de carbohidratos
73.43 [g] de proteínas
519 [calorías]

CASO DE PRUEBA #3
NN == 10
SS == 0
CR == 0
RESULTADO:
19.0 [g] de grasas
60.0 [g] de carbohidratos
73.43 [g] de proteínas
443 [calorías]
'''