def obtener_lista_equipos(resultados):
    participantes = []
    for equipo_1, equipo_2 in resultados:
        if equipo_1 not in participantes:
            participantes.append(equipo_1)
        if equipo_2 not in participantes:
            participantes.append(equipo_2)
    participantes.sort()
    return participantes
