'''
from math import sqrt

#Lee los datos de entrada
print("Circulo:")
centro= float(input("ingrese coordenada x"))
centro_2= float(input("ingrese coordenada y"))
radio= float(input("ingrese radio"))
print("Punto")
punto= float(input("Ingrese x de punto"))
punto_2= float(input("ingrese y de punto"))

#Calcula la distancia
d= sqrt((centro-punto)**2 + (centro_2-punto_2)**2)

#Determina la salida
if d<radio:
    print("el punto esta dentro del circulo")
elif d == radio:
    print("el punto esta en el arco del circulo")
else:
    print("el punto esta fuera del circulo")
'''
'''
a = int(input("Ingrese edad"))
b = int(input("Ingrese edad"))
c = int(input("Ingrese edad"))

if a > b:
    if a > c:
        print("el mayor es",a)
    else:
        print("el mayor es",c)
else:
    if b>c:
         print("el mayor es",b)
    else:
       print("el mayor es",c)
'''
valor = int(input("Valor de la propiedad en UF(1500-13000): "))
if valor<1500 or valor>13000:
    print("ERROR: El valor es invalido")
else:
     pie= int(input("Ingrese '%' del Pie(20-45'%'): "))
     if pie> 45 or pie<20:
         print("ERROR: Pie no valido")
     else:
        plazo= int(input("Ingrase plazo (20,25,30): "))
        if plazo !=20:
            if plazo != 25:
                if plazo != 30:
                    print("ERROR: Plazo no valido")
                else:
                    vivienda = int(input("Tipo de vivienda Casa(1) o Departamento(2): "))
                if vivienda>2 or vivienda<1:
                    print("ERROR: Vivienda no valida")
                else:
                    estado = int(input("Estado de vivienda Nuevo(1) o Usado(2): "))
                    if estado>2 or estado<1:
                        print("ERROR: Estado no valido")
            else:
                vivienda = int(input("Tipo de vivienda Casa(1) o Departamento(2): "))
                if vivienda>2 or vivienda<1:
                    print("ERROR: Vivienda no valida")
                else:
                    estado = int(input("Estado de vivienda Nuevo(1) o Usado(2): "))
                    if estado>2 or estado<1:
                        print("ERROR: Estado no valido")
        else:
            vivienda= int(input("Tipo de vivienda Casa(1) o Departamento(2): "))
            if vivienda>2 or vivienda<1:
                print("ERROR: Vivienda no valida")
            else:
                estado = int(input("Estado de vivienda Nuevo(1) o Usado(2): "))
                if estado>2 or estado<1:
                    print("ERROR: Estado no valido")

