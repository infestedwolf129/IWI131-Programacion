lista = []
lista_numeros = [32,5,12,6,43,89,32,54,9,10]
for i in lista_numeros:
  if i%2 == 0:
    lista.append(i)

print("El promedio de los pares es", sum(lista)/len(lista))