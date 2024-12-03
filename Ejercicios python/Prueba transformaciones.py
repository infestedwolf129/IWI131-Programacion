
import os

def menu():
    os.system('cls')
    print ("Selecciona una opción")
    print ("\t1 - transformar in a cm")
    print ("\t2 - transformar cm a in")
    print ("\t3 - transformar ft a cm")
    print ("\t4 - transformar cm a ft")
    print ("\t9 - salir")

while True:
    menu()
    opcionMenu = input("Ingrese una opción >>")

    if opcionMenu== "1":
        n1 = float(input("Introduce dato para transformar de in a cm: "))
        print("Su resultado es",n1*2.54,"cm")
    elif opcionMenu== "2":
        n1 = float(input("Introduce dato para transformar de cm a in: "))
        print("Su resultado es",round(n1/2.54),"in")
    elif opcionMenu== "3":
        n1 = float(input("Introduce dato para transformar de ft a cm: "))
        print("Su resultado es",n1*30.48,"cm")
    elif opcionMenu== "4":
        n1 = float(input("Introduce dato para transformar de cm a ft: "))
        print("Su resultado es",n1/30.48,"ft")
    elif opcionMenu== "9":
        break
    
    
