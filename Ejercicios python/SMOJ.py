clave = str("FLDSMDFR21")
intentos = 1
peticion = str("")
while intentos <= 5 and peticion != clave: 
    peticion = str(input(""))
    intentos += 1
if intentos > 5:
    print("FLDSMDFR bloqueada!")
else:
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