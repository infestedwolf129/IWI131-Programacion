#Problema 1
def suma_productos(rut):
    suma_n = 0
    i = 2
    while rut != 0:
        n = rut%10
        rut = rut//10
        suma_n += n*i
        i += 1
        if i == 8:
            i = 2
    return suma_n

def digito_verificador(rut):
    p = suma_productos(rut)
    verificador = 11 - (p%11) 
    if verificador == 10:
        verificador = "k"
    return verificador

#Problema 2
Rut = int(input("Ingrese rut sin digito verificador y sin puntos: "))
verificador = digito_verificador(Rut)
print(verificador)

#Problema 3
