def buscar_profesional (profesional, identificador):
    for tupla in profesional:
        identificadorp,nombre,_ = tupla
        if identificadorp== identificador:
            return nombre
    return " "
def jefeX(profesionales,turnos):
    menor = float("inf")
    id_menor = 0
    for turno in turnos:
        id,horas = turno
        if len(horas) <= menor:
            menor = len(horas)
            id_menor = id
    return buscar_profesional(profesionales,id_menor)
def jefe(profesionales,turnos):
    lista = []
    for id,l_turnos in turnos:
        lista.append((len(l_turnos),id))
    lista.sort()
    return buscar_profesional (profesionales, lista[0][1])


profesionales = [
   (125,'Ann','M'),
   (271,'Beth','E'),
   (443,'John','G'),
   (105,'Ben','M'),
   (85,'Fer','E')
]

turnos = [
   (443,[5,8,2]),
   (126,[6,2,4,7]),
   (271,[1,9]),
   (85,[2,9])
]

print(jefeX(profesionales,turnos))

