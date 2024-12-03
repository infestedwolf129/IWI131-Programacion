características = [
('kawaii',10), ('leal',20), ('acusete',-10), ('avaro',-15), ('respetuoso',20),
('otaku',25),('lolero',25),('furro',-50),('vtuver',25),('mechero',-30)
]

amigos = [('Sneki',('leal','kawaii','vtuver')),
          ('Otaku-taku',('otaku','avaro','lolero','leal')),
          ('Maiga',('paciente','otaku','leal')),
          ('Mojojojo',('mechero','kawaii','Furro','lolero')),
          ('Seiya',('leal','acusete')),
          ('Vegeta',('otaku','avaro')),
          ('Kalila',('lolero','kawaii')),
          ('Grogu',('avaro','kawaii','lolero','otaku')),
          ('Freezer',('acusete','furro','otaku','lolero'))
]

######### FUNCION 1 ########################################
def obtener_valor_característica(características,buscada):##
    for tupla in características:                         ##
        caracter,puntaje = tupla                          ##
        if caracter == buscada:                           ##
            return puntaje                                ##
    return 0                                              ##
############################################################

######### FUNCION 2 ######################################################
def puntaje_amigo(amigo,características):                               ##
    suma = 0                                                            ##
    _, buscado = amigo                                                  ##
    i = 0                                                               ##
    while i < len(buscado):                                             ##
        suma += obtener_valor_característica(características,buscado[i])##
        i +=1                                                           ##
    return suma                                                         ##
##########################################################################

############## PROGRAMA ################################################
nombre_1 = ""                                                         ##
puntaje_1 = -1                                                        ##
nombre_2 = ""                                                         ##
puntaje_2 = -1                                                        ##
for amigo in amigos:                                                  ##
    nombre,contenido = amigo                                          ##
    puntaje = puntaje_amigo(amigo,características)                    ##
    if puntaje > puntaje_1 and ("lolero" in contenido):               ##
        puntaje_2 = puntaje_1                                         ##
        nombre_2 = nombre_1                                           ##
        puntaje_1 = puntaje                                           ##
        nombre_1 = nombre                                             ##
    if puntaje_1 > puntaje > puntaje_2 and ("lolero" in contenido):   ##
        puntaje_2 = puntaje                                           ##
        nombre_2 = nombre                                             ##
print(f'{nombre_1},{puntaje_1} puntos\n{nombre_2},{puntaje_2} puntos')##
########################################################################