def avistamientos_por_region(nombre_archivo):
    archivo = open(nombre_archivo,"r")
    dict_regiones= {}
    for linea in archivo:
        if "año" in linea:
            del linea
        else:
            linea= linea.strip().split(";")
            fecha = linea[0].split("-")
            año = fecha[0]
            mes = fecha[1]
            region = linea[1]
            informados = int(linea[2])
            ovnis = int(linea[3])
            promedio = round((ovnis*100/informados),2)
            if region not in dict_regiones:
                dict_regiones[region] =[]
            dict_regiones[region].append((promedio,año,mes,informados,ovnis))
    for region in dict_regiones:
        dict_regiones[region].sort()
        dict_regiones[region].reverse()
        new_file= open(str(region)+".txt","w")
        formato = "En el mes {} de {} hubo {}% de avistamientos confirmados de un total de {}" + "\n"
        if len(dict_regiones[region]) < 3:
            rango = len(dict_regiones[region])
        else:

            rango = 3
        for dato in range(rango):
            mes = dict_regiones[region][dato][2]
            año = dict_regiones[region][dato][1]
            porcentaje = dict_regiones[region][dato][0]
            informados = dict_regiones[region][dato][3]
            new_file.write(formato.format(mes,año,porcentaje,informados))
        new_file.close()
    archivo.close()
    return(len(dict_regiones))

#print(avistamientos_por_region("ovnis_chico.csv"))
#print(avistamientos_por_region("ovnis_mediano.csv"))
#print(avistamientos_por_region("ovnis_grande.csv"))
