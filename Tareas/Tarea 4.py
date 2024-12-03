#Inicializamos las variables para evitar errores de codigo
n = 1
x_1 = 0
x_2 = 0
x_3 = 0
y_1 = 0
y_2 = 0
y_3 = 0
sucursal_1 = ""
sucursal_2 = ""
sucursal_3 = ""
while n <= 3 : #Hacemos el ciclo a repetir para las sucursales y coordenadas
    sucursal= str(input(f'Nombre sucursal {n}: '))
    x= int(input(f"Coordenada x_{n}: "))
    y= int(input(f"Coordenada y_{n}: "))
    print("")
    if n == 1:
        sucursal_1 = sucursal
        x_1 = x
        y_1 = y
    elif n == 2:
        sucursal_2 = sucursal
        x_2 = x
        y_2 = y
    else:
        sucursal_3 = sucursal
        x_3 = x
        y_3 = y
    sucursal = ""
    x = 0
    y = 0  
    n+= 1
#Importamos el operador de raiz e inicializamos las variables sobre el pedido
from math import sqrt
T_pedido = 0 
plato = 0
suma_total= 0 #En esta variable guardaremos la suma de los pedidos totales en caso de ser más de 1
registro = True
menor= float('inf')
#INICIALIZAMOS CONTADORES DE PEDIDOS
sucursal_1_pedidos = 0
sucursal_2_pedidos = 0
sucursal_3_pedidos = 0
#PLATOS 
carnivoro= 4000
vegetariano = 3000
vegano= 3500
#COMENZAMOS CICLO A SEGUIR PARA INGRESAR DATOS SOBRE PEDIDOS
while registro: 
    while plato != -1:
        plato= int(input("Ingrese número de plato: "))
        if plato == 1:
            T_pedido+= carnivoro
            plato = 0
        elif plato == 2:
            T_pedido += vegetariano
            plato= 0
        elif plato == 3:
            T_pedido+= vegano
            plato= 0
    print("Total del pedido",T_pedido)
    suma_total+= T_pedido
    T_pedido = 0
    x= int(input("Ingrese coordenada x cliente: "))
    y= int(input("Ingrese coordenada y cliente: "))
    #CALCULAMOS DISTANCIAS PARA COMPARAR
    distancia_sucursal_1 = sqrt(((x-x_1)**2)+((y-y_1)**2))
    distancia_sucursal_2 = sqrt(((x-x_2)**2)+((y-y_2)**2))
    distancia_sucursal_3 = sqrt(((x-x_3)**2)+((y-y_3)**2))
    if distancia_sucursal_1 < menor:
        menor= distancia_sucursal_1
    elif distancia_sucursal_2 < menor:
        menor= distancia_sucursal_2
    else:
        menor = distancia_sucursal_3
    if menor == distancia_sucursal_1:
        print (f'El pedido sera entregadó por {sucursal_1}')
        sucursal_1_pedidos +=1
    elif menor == distancia_sucursal_2:
        print (f'El pedido sera entregadó por {sucursal_2}')
        sucursal_2_pedidos+=1
    elif menor == distancia_sucursal_3:
        print (f'El pedido sera entregadó por {sucursal_3}')
        sucursal_3_pedidos+= 1
    registro = str(input("¿Desea agregar otro pedido?(si/no): ")) #PREGUNTAMOS SI DESEA REPETIR EL CICLO
    print("")
    if registro == str("si"):
        registro = True
        plato = 0
    else:
        registro = False
print('##### ESTADÍSTICAS FINALES #####')
print(f'Monto total recaudado ${suma_total}')
print(f'{sucursal_1} entregó {sucursal_1_pedidos}')
print(f'{sucursal_2} entregó {sucursal_2_pedidos}')
print(f'{sucursal_3} entregó {sucursal_3_pedidos}')