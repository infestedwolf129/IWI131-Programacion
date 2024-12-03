'''
monto = int(input('Ingrese suma de la cuenta: '))
medio = input("Medio de pago (Contado/Tarjeta): ")
if medio == "Contado":
    monto-= monto*0.1
    print("A pagar", monto)

''' 
'''
temperatura= float(input("Temperatura: "))
if temperatura >= 38:
    print("Vaya a cuarentena inmediata")
else:
    print("Mantenga distanciamiento social")
'''
'''
num = int(input("Ingrese numero positivo: "))
resto = num%2
if resto== 0:
    print("Par")
else:
    print("Impar")
'''
'''
from random import randint
n = randint(0,1)
if n == 0:
    print("Cara")
else:
    print("Sello")
'''