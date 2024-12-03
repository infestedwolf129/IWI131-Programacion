def verificacion_dosis(rut,dosis):
    if rut in dosis:
        if len(dosis[rut]) < 3:
            return 1
        elif len(dosis[rut]) == 3:
            return 2
    else:
        return 0

def vacuna_correspondiente(rut,vacunas):
    for vacuna in vacunas:
        if rut in vacunas[vacuna]:
            return vacuna

def actualizacion_vacunas (rut,vacuna,vacunas):
    if vacuna in vacunas:
        vacunas[vacuna].append(rut)
    elif vacuna not in vacunas:
        vacunas[vacuna] = [rut]

def actualizacion_dosis (rut,fecha,edad,dosis):
    if rut in dosis:
        dosis[rut].append(fecha)
    else:
        dosis[rut] = [edad,fecha]



#EJEMPLOS DE PRUEBA (inicio)
vacunas = {
"Sinovac":["11.111.111-1", "12.345.678-9"],
"Pfizer": ["8.978.657-3"],
"CanSino": ["13.789.456-k"]
}
dosis = {
"11.111.111-1":[55,(2021,4,11),(2021,5,10)],
"12.345.678-9":[47,(2021,6,3)],
"8.978.657-3":[79,(2021,3,23)],
"13.789.456-k":[40,(2021,5,18),(2021,6,10)]
}
#EJEMPLOS DE PRUEBA (fin)

dd = int (input ("Día: "))
mm = int (input ("Mes: "))
aaaa = int (input("Año: "))
fecha = (aaaa,mm,dd)
terminar = True
while terminar == True:
    rut = input("RUT: ")
    if verificacion_dosis(rut,dosis) == 1:
        x = vacuna_correspondiente(rut,vacunas)
        print(f'Segunda dosis. Paciende debe ser inoculado con: {x}')
        dosis[rut].append((aaaa,mm,dd))
        continuar = input("¿Desea continuar? (s/n): ")
        if continuar == "n":
            terminar = False
    if verificacion_dosis(rut,dosis) == 0:
        edad = int(input("Edad: "))
        vacuna = input("Tipo vacuna: ")
        actualizacion_vacunas(rut,vacuna,vacunas)
        actualizacion_dosis(rut,fecha,edad,dosis)
        continuar = input("¿Desea continuar? (s/n): ")
        if continuar == "n":
            terminar = False
    if verificacion_dosis(rut,dosis) == 2:
        print("Ya tiene todas las dosis requeridas.")
        continuar = input("¿Desea continuar? (s/n): ")
        if continuar == "n":
            terminar = False

dosis_completas = {}
for key in dosis:
    if len(dosis[key]) == 3:
        if dosis[key][0] not in dosis_completas:
            dosis_completas[dosis[key][0]] = 0
        dosis_completas[dosis[key][0]] += 1

lista_edades = []
for edad_ordenada in dosis_completas:
    tupla = (dosis_completas[edad_ordenada],edad_ordenada)
    lista_edades.append(tupla)
lista_edades.sort()

print(f'Edades con más personas con más esquema de inoculacion completo:')
print(f'{lista_edades[-1][1]} años: {lista_edades[-1][0]} personas') 
print(f'{lista_edades[-2][1]} años: {lista_edades[-2][0]} personas')
print(f'{lista_edades[-3][1]} años: {lista_edades[-3][0]} personas')