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

def resultado_elecciones (coalicion,votos):
    coalicion += ";"
    i = 0
    extraer_coalicion = ""
    while i < len(coalicion):
        if coalicion[i] == ";":
            extraer_coalicion += coalicion[:i]
            coalicion = coalicion[i+1:]
            i= 0
        elif extraer_coalicion != "":
            extraer_coalicion += "-"
            z = 0
            partido = ""
            n_coalicion = ""
            total_votos_coalicion = 0
            coalicion_anterior = ""
            votos_anteriores = 0
            while z < len(extraer_coalicion):
                if extraer_coalicion[z] == ":":
                    n_coalicion += extraer_coalicion[:z]
                    extraer_coalicion = extraer_coalicion [z+1:]
                    z = 0
                    print(f'Coalicion {n_coalicion}:')
                elif extraer_coalicion [z] == "-":
                    partido += extraer_coalicion[:z]
                    extraer_coalicion = extraer_coalicion [z+1:]
                    z= 0
                    print(partido, votos_partido(votos,partido))
                total_votos_coalicion+= votos_partido(votos,partido)
                print(f'Total votos coalicion {n_coalicion}: {total_votos_coalicion}')
                z+=1
                if votos_anteriores > total_votos_coalicion:
                    votos_anteriores = total_votos_coalicion
                    coalicion_anterior = n_coalicion
        i += 1
    return (f'La coalicion ganadora es {votos_anteriores} con {coalicion_anterior}')

coalicion = input("Ingrese coalicion: ")
votos = input ("Ingrese votos por partido: ")
ganador = resultado_elecciones(coalicion,votos)
print(ganador)