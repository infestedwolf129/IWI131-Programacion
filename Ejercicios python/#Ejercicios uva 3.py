'''
#Ejercicios uva 3
usm = int(input("Ingrese nota obtenida: "))
if usm<55:
    print("Su equivalente en USA es: F")
elif usm< 70:
    print("Su equivalente en USA es: C")
elif usm< 90:
    print("Su equivalente en USA es: B")
else:
    print("Su equivalente en USA es: A")
'''
'''
anual = int(input('Ingreso anual (millones de pesos): '))
if anual < 8:
   tasa = 0
elif anual < 17:
   tasa = 0.04
elif anual < 29:
   tasa = 0.08
elif anual < 40:
   tasa = 0.14
elif anual < 52:
   tasa = 0.23
elif anual < 69:
   tasa = 0.3
elif anual < 87:
   tasa = 0.35
else:
   tasa =0.4
print (tasa)
'''
'''
certamenes= 55
controles= 55
tareas= 55
formativas= 55
smoj= 55
if certamenes >= 55:
   nf = certamenes*0.5 + controles*0.2 + tareas*0.2 + formativas*0.05 + smoj*0.05
   if nf >= 55:
      print('Felicitaciones, ¡aprobaste!')
   else:
      print('Lo siento, aprobaste los certámenes pero reprobaste la asignatura')
else:
   nf = certamenes
   print('Lo siento, reprobaste')
print('Tu nota final es:', nf)
'''
'''
año= int(input("Ingresa año: "))
if ((año % 4 == 0 and año % 100 != 0) or año % 400 == 0):
     print("El año es bisiesto")
else:
     print("El año no es bisiesto")
'''
usm= int(input("Ingrese nota: "))
if usm<55:
    print("Nota F")
if 55<=usm<70:
    print("Nota C")
if 70<=usm<90:
    print("Nota B")
else:
    print("Nota A")    