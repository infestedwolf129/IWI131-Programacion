##########################################
#                                        #
#  Programe sus funciones aquí           #
#                                        #
##########################################

def disparo(tablero, barcos, fila, columna):

    # Desarrolle aquí su código para la función
    flag = False
    for barco in barcos: #Separamos el barco por partes
        largo = barco[0]
        orientacion = barco[1]
        f = barco[2] 
        c = barco[3]

        if orientacion == 1 and (c == columna):
            i = 0
            while i < largo and (flag == False):
                if fila == f+i:
                    flag = True
                i += 1
        elif orientacion == 2 and (f == fila):
            i = 0
            while i < largo and (flag == False):
                if columna == c+i:
                    flag = True
                i += 1
        if flag == True:
            tablero[fila].pop(columna)
            tablero[fila].insert(columna,"O")
        else:
            tablero[fila].pop(columna)
            tablero[fila].insert(columna," ")


        
        




def destruidos(tablero, barcos):

    # Desarrolle aquí su código para la función
    destruidos = 0
    for barco in barcos:
        largo = barco[0]
        orientacion = barco[1]
        f = barco[2]
        c = barco[3]
        x = 0
        #Primero vemos la orientacion
        #Luego, iniciamos un ciclo que recorre todo el barco y determina si fue destruido
        if orientacion == 1:  
            i = 0
            while i <largo: 
                if tablero[f+i][c]== "O":
                    x += 1
                i +=1
        elif orientacion == 2:  
            i = 0
            while i <largo: 
                if tablero[f][c+i]== "O":
                    x += 1
                i +=1
        #Una vez determinamos que todo el barco fue destruido, modificamos en el tablero
        if x == largo:
            if orientacion == 1:
                z = 0
                while z < largo:
                    tablero[f+z].pop(c)
                    tablero[f+z].insert(c,"X")
                    z += 1
            elif orientacion == 2:
                z = 0
                while z < largo:
                    tablero[f].pop(c+z)
                    tablero[f].insert(c+z,"X")
                    z += 1
    #Ciclo para hacer el conteo de los barcos destruidos en el tablero ya modificado
    for barco in barcos:
        f = barco[2]
        c = barco[3]
        if tablero[f][c] == "X":
            destruidos +=1
        
    return destruidos




# OPCIONAL:
# Cambie el valor de esta variable a 1 si desea ver
# la ubicación de los barcos antes de comenzar.
# Esto puede ser útil para probar sus funciones.
mostrar_solucion = 1



##################################################
#                                                #
#  NO MODIFIQUE EL CÓDIGO A PARTIR DE ESTE PUNTO #
#                                                #
##################################################

import random as rd

# Función que muestra el tablero con el formato deseado para la pantalla
def show(tablero):
    print("\n  123456789")
    for i in range(9):
        fila_texto = " "
        for j in tablero[i]:
            fila_texto += str(j)
        print(chr(65+i)+fila_texto)

# Creación del tablero (inicialmente únicamente con "-" en todas las posiciones)
tablero = []
board = []
for i in range(9):
    fila = []
    for j in range(9):
        fila.append("-")
    tablero.append(fila)
    board.append(list(fila))

# Creación de los barcos con orientación y posición aleatorias
barcos = []
length = [2,3,3,4,5]
for i in range(5):
    l = length[i]
    orientation = rd.randint(1,2)
    if orientation == 1:
        flag = True
        while flag:
            row = rd.randint(0,9-l)
            column = rd.randint(0,8)
            empty = True
            for j in range(l):
                empty = empty and board[row+j][column] != "X"
            if empty:
                flag = False
        for j in range(l): board[row+j][column] = "X"
    else:
        flag = True
        while flag:
            row = rd.randint(0,8)
            column = rd.randint(0,9-l)
            if "X" not in board[row][column:column+l]:
                flag = False
        for j in range(l): board[row][column+j] = "X"
    barcos.append([l,orientation,row,column])
print(barcos)
# Se muestra la solución al inicio en caso de que se haya seleccionado esta opción
if mostrar_solucion == 1:
    print("Solución:")
    show(board)
    print("\n\n")

# Ciclo principal del programa donde se reciben los disparos, se validan y se llama a la función disparo()
print("¡Bienvenido a Solitary Battleship!")
destroyed = 0
while destroyed < 5:
    not_valid = True
    while not_valid:
        turn = input("\n¿Que casilla desea disparar? (Ejemplo: A1): ")
        not_valid = False
        if len(turn) != 2:
            not_valid = True
            print("Ingrese una casilla válida por favor.")
        elif not("A" <= turn[0] and turn[0] <= "I"):
            not_valid = True
            print("Ingrese una casilla válida por favor.")
        elif not("1" <= turn[1] and turn[1] <= "9"):
            not_valid = True
            print("Ingrese una casilla válida por favor.")
        else:
            fila = "ABCDEFGHI".index(turn[0])
            columna = int(turn[1])-1
            if tablero[fila][columna] != "-":
                not_valid = True
                print("Ya ha disparado a esta casilla.")
    disparo(tablero, barcos, fila, columna)
    destroyed = destruidos(tablero, barcos)
    show(tablero)
    print("\n"+str(destroyed)+" barcos destruidos.")
    # Fin del juego
    if destroyed == 5:
        print("Felicidades, juego terminado.")
