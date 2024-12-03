#Comenzamos definiendo las variables que ocuparemos como 0 para que luego no colapse el codigo
valor = 0
pie = 0
plazo = 0
vivienda = 0
estado = 0
#Luego pedimos los datos correspondientes al usuario
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
                if estado<1 or estado>2:
                    print("ERROR: Estado no valido")

if valor >= 1500 or valor<=13000:
    if pie>= 20 or pie <= 45:
        if plazo == 20 or plazo == 25 or plazo ==30:
            if vivienda == 1 or vivienda == 2:
                if estado == 1 or estado ==2:
                    #calculamos el precio de la vivienda quitando el pie inicial
                    a_pagar = int(valor-(valor*(pie/100)))
                    #Definimos los posibles casos con sus respectivos calculos, como el del interes o el seguro.
                    #CASO 1 CASA NUEVA: Al ser una casa nueva se aplican 2 seguros, Desgravamen e Incendios y sismos.
                    if vivienda == 1 and estado == 1:
                        if plazo== 20:
                            interes = a_pagar*0.25
                            precio = a_pagar+interes
                            seguro = 1.3*12*20
                            precio_final= precio + seguro
                            dividendo_mensual= precio_final/(12*20)
                            precio_final = round(precio_final,2)
                            dividendo_mensual = round(dividendo_mensual,2)
                            print("Total del credito a pagar",precio_final,"UF")
                            print("Dividendo mensual de",dividendo_mensual,"UF")
                        elif plazo == 25:
                            interes = a_pagar*0.3
                            precio = a_pagar+interes
                            seguro = 1.3*12*25
                            precio_final= precio + seguro
                            dividendo_mensual= precio_final/(12*25)
                            precio_final = round(precio_final,2)
                            dividendo_mensual = round(dividendo_mensual,2)
                            print("Total del credito a pagar",precio_final,"UF")
                            print("Dividendo mensual de",dividendo_mensual,"UF")
                        else:
                            interes = a_pagar*0.35
                            precio = a_pagar+interes
                            seguro = 1.3*12*30
                            precio_final= precio + seguro
                            dividendo_mensual= precio_final/(12*30)
                            precio_final = round(precio_final,2)
                            dividendo_mensual = round(dividendo_mensual,2)
                            print("Total del credito a pagar",precio_final,"UF")
                            print("Dividendo mensual de",dividendo_mensual,"UF")
                    #CASO 2 CASA USADA: Al ser una casa usada se aplica 1 solo seguro, Desgravamen.
                    elif vivienda == 1 and estado == 2:
                        if plazo == 20:
                            interes = a_pagar*0.22
                            precio = a_pagar+interes
                            seguro = 0.5*12*20
                            precio_final= precio + seguro
                            dividendo_mensual= precio_final/(12*20)
                            precio_final = round(precio_final,2)
                            dividendo_mensual = round(dividendo_mensual,2)
                            print("Total del credito a pagar",precio_final,"UF")
                            print("Dividendo mensual de",dividendo_mensual,"UF")
                        elif plazo == 25:
                            interes = a_pagar*0.27
                            precio = a_pagar+interes
                            seguro = 0.5*12*25
                            precio_final= precio + seguro
                            dividendo_mensual= precio_final/(12*25)
                            precio_final = round(precio_final,2)
                            dividendo_mensual = round(dividendo_mensual,2)
                            print("Total del credito a pagar",precio_final,"UF")
                            print("Dividendo mensual de",dividendo_mensual,"UF")
                        else:
                            interes = a_pagar*0.31
                            precio = a_pagar+interes
                            seguro = 0.5*12*30
                            precio_final= precio + seguro
                            dividendo_mensual= precio_final/(12*30)
                            precio_final = round(precio_final,2)
                            dividendo_mensual = round(dividendo_mensual,2)
                            print("Total del credito a pagar",precio_final,"UF")
                            print("Dividendo mensual de",dividendo_mensual,"UF")
                    #CASO 3 DEPTO NUEVO: Al ser un departamento nuevo se aplican los 3 seguros, Desgravamen, Incendios y sismos, por ultimo, Tu banco te cuida.
                    elif vivienda == 2 and estado == 1:
                        if plazo == 20:
                            interes = a_pagar*0.28
                            precio = a_pagar+interes
                            seguro = 1.6*12*20
                            precio_final= precio + seguro
                            dividendo_mensual= precio_final/(12*20)
                            precio_final = round(precio_final,2)
                            dividendo_mensual = round(dividendo_mensual,2)
                            print("Total del credito a pagar",precio_final,"UF")
                            print("Dividendo mensual de",dividendo_mensual,"UF")
                        elif plazo == 25:
                            interes = a_pagar*0.33
                            precio = a_pagar+interes
                            seguro = 1.6*12*25
                            precio_final= precio + seguro
                            dividendo_mensual= precio_final/(12*25)
                            precio_final = round(precio_final,2)
                            dividendo_mensual = round(dividendo_mensual,2)
                            print("Total del credito a pagar",precio_final,"UF")
                            print("Dividendo mensual de",dividendo_mensual,"UF")
                        else:
                            interes = a_pagar*0.41
                            precio = a_pagar+interes
                            seguro = 1.6*12*30
                            precio_final= precio + seguro
                            dividendo_mensual= precio_final/(12*30)
                            precio_final = round(precio_final,2)
                            dividendo_mensual = round(dividendo_mensual,2)
                            print("Total del credito a pagar",precio_final,"UF")
                            print("Dividendo mensual de",dividendo_mensual,"UF")
                    #CASO 4 DEPTO USADO: Al ser un departamento usado, solo aplican 2 seguros, Desgravamen y Tu banco te cuida.
                    else:
                        if plazo == 20:
                            interes = a_pagar*0.26
                            precio = a_pagar+interes
                            seguro = 0.8*12*20
                            precio_final= precio + seguro
                            dividendo_mensual= precio_final/(12*20)
                            precio_final = round(precio_final,2)
                            dividendo_mensual = round(dividendo_mensual,2)
                            print("Total del credito a pagar",precio_final,"UF")
                            print("Dividendo mensual de",dividendo_mensual,"UF")
                        elif plazo == 25:
                            interes = a_pagar*0.32
                            precio = a_pagar+interes
                            seguro = 0.8*12*25
                            precio_final= precio + seguro
                            dividendo_mensual= precio_final/(12*25)
                            precio_final = round(precio_final,2)
                            dividendo_mensual = round(dividendo_mensual,2)
                            print("Total del credito a pagar",precio_final,"UF")
                            print("Dividendo mensual de",dividendo_mensual,"UF")
                        else:
                            interes = a_pagar*0.37
                            precio = a_pagar+interes
                            seguro = 0.8*12*30
                            precio_final= precio + seguro
                            dividendo_mensual= precio_final/(12*30)
                            precio_final = round(precio_final,2)
                            dividendo_mensual = round(dividendo_mensual,2)
                            print("Total del credito a pagar",precio_final,"UF")
                            print("Dividendo mensual de",dividendo_mensual,"UF")


'''
CASO DE PRUEBA 1:
Valor de la propiedad en UF(1500-13000): 3000
Ingrese '%' del Pie(20-45'%'): 20
Ingrase plazo (20,25,30): 20
Tipo de vivienda Casa(1) o Departamento(2): 1
Estado de vivienda Nuevo(1) o Usado(2): 2
Total del credito a pagar 3048.0 UF
Dividendo mensual de 12.7 UF  

CASO DE PRUEBA 2:
Valor de la propiedad en UF(1500-13000): 10000
Ingrese '%' del Pie(20-45'%'): 45
Ingrase plazo (20,25,30): 25
Tipo de vivienda Casa(1) o Departamento(2): 2
Estado de vivienda Nuevo(1) o Usado(2): 2
Total del credito a pagar 7500.0 UF
Dividendo mensual de 25.0 UF  

CASO DE PRUEBA 3:
Valor de la propiedad en UF(1500-13000): 12000
Ingrese '%' del Pie(20-45'%'): 33
Ingrase plazo (20,25,30): 20
Tipo de vivienda Casa(1) o Departamento(2): 1
Estado de vivienda Nuevo(1) o Usado(2): 1
Total del credito a pagar 10362.0 UF
Dividendo mensual de 43.17 UF  
'''