
archivo = open("saludo.txt","w")
saludo = "Bienvenida a IWI131"
archivo.write(saludo+"\n")
saludo = saludo.replace("IWI131","Programación")
archivo.write(saludo)
archivo.close()

l = [37, 17, 51, 59, 77]
s = 'La suma de los {} elementos es {} y el promedio es {}'
print(s.format(len(l), sum(l), sum(l)/len(l)))