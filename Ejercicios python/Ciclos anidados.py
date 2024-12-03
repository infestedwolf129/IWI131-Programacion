
linea = 0
#contador de asteriscos
i=0
#guardar asteriscos
estrellas= ""
#mientras haya menos de 5 lineas
while linea < 5:
    #mientras haya menos de 5 asteriscos
    while i <= linea:
        #agregar asterisco
        estrellas += "*"
        i +=1
    #mostrarlo!
    print(estrellas)
    linea +=1
    estrellas =""
    i = 0

'''
factor_a = 5
factor_b = 5
while factor_a >=1:
    while factor_b >=1:
        print(factor_a*factor_b)
        factor_b-= 1
    
    factor_b=5  
    factor_a-=1
'''
'''
i = 3
j = 1
k = 0
while i > 0:
    while j < 2:
        k += j**i
        j+=1
    i-=1
print(k)
'''
'''
from random import randint
n = int(input("Cantidad de números a generar: "))
listo = False
pares = 0
intentos = 0
while intentos <n or intentos == False:
    num = randint(1,100)
    print(num)
    if num % 2 == 0:
        pares += 1
    if pares == int(n/2):
        listo =True 
    intentos += 1
if listo != False:
    print("Se completo la cantidad de pares necesarios en", intentos, "intentos")
else:
    print("No se logró generar la cantidad de pares necesarios")
'''