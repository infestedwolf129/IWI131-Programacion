# Programa para traducir emojis
texto = input("Ingrese texto: ")
significados = input("Ingrese significados: ")
# Se definen las variables a utilizar para evitar posibles errores

inicio_imagen = 0
fin_imagen = 0
inicio_significado = 0
fin_significado = 0
imagen = ""
emoji = ""
# buscamos en el texto de significados el emoji y su traduccion
while fin_significado < len(significados):
    if significados[fin_significado] == '*':
        fin_imagen = fin_significado
        imagen = significados[inicio_imagen:fin_imagen]
        inicio_significado= fin_significado +1
    elif significados[fin_significado] == '$':
        emoji = significados[inicio_significado:fin_significado].upper()
        inicio_imagen = fin_significado + 1
        #En caso de querer comprobar los emojis quitar comentario a linea anterior
        #Una vez tenemos el emoji y su significado lo buscamos en el texto original para generar el traducido
        pos=0
        nuevo_texto=""
        while pos < len(texto):
            if imagen == texto[pos:pos+len(imagen)]:
              nuevo_texto += emoji
              pos+= len(imagen)
            else:
              nuevo_texto+= texto[pos]
              pos += 1
        texto = nuevo_texto
    fin_significado += 1

print("Texto traducido:",nuevo_texto)