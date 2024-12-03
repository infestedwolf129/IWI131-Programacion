def mas_jovenes(nacimientos, fecha):
    lista =[] 
    for persona in nacimientos:
        _,nombre,fecha_n= persona
        print (fecha_n)
        if fecha_n < fecha:
            lista.append(nombre)
    lista.sort()
    return lista