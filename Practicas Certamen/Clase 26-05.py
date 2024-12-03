def dia_en_palabras(d):
   if d==0:
      return('Domingo')
   if d==1:
      return('Lunes')
   if d==2:
      return('Martes')
   if d==3:
      return('Miércoles')
   if d==4:
      return('Jueves')
   if d==5:
      return('Viernes')
   if d==6:
      return('Sábado')
      
def dia_de_la_semana(dia,mes,año):
    a = (14-mes)//12
    y = año - a
    m = mes+12*a-2
    d = (dia + y +y//4- y//100 + y//400 + (31*m)//12) % 7
    return dia_en_palabras(d)

amigos = input("Datos de amigos: ")
print("Fecha de nacimiento")
d = int(input("Día: "))
a = int(input("Mes: "))
m = int(input("Año: "))
mi_dia= dia_de_la_semana(d,m,a)
print("Naciste un",mi_dia)
print("Amigos a invitar:")

amigos = amigos + ";"
i= 0
while i<len(amigos):
    fecha = ""
    while amigos[i] != ",":
        fecha+=amigos[i]
        i+=1
    nombre=""
    i+= 1
    while amigos[i]!=";":
        nombre+=amigos[i]
        i+=1
    i+=1
    validacion = dia_de_la_semana(int(fecha[:2]),int(fecha[2:4]),int(fecha[4:]))
    if validacion == mi_dia:
        print(nombre)
'''
16052000,Sofia;29022000,Silvia;01082000,Andrea;28042000,Paula;04102000,Eduardo;26062001,Pedro;11072001,Federico;03112001,Claudia;20052001,Lucas;24061999,Gabriel;04101999,Camila
'''
