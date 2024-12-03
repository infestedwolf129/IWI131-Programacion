def votos_partido(votos,partido):
    votos+= "$"
    i = 0
    conteo_de_votos  = 0
    while i < len(votos):
        voto_a_partido = ""
        if votos[i] == "$":
             voto_a_partido += votos[:i]
             votos = votos [i+1:]
             i=0
             if voto_a_partido == partido:
                 conteo_de_votos  +=1
        i+=1
    return conteo_de_votos 