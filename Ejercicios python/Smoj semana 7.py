'''
repeticiones = int(input())
i= 0
lista = []
while i < repeticiones:
    lista.append(int(input()))
    i+=1
lista.sort()
if len(lista)%2 != 0:
    mediana = int(len(lista)/2)
    print(lista[mediana]*2)
elif len(lista)%2 == 0:
    mediana = int((lista[int((len(lista)/2)-1)]+lista[int(len(lista)/2)])/2)
    print(mediana)

'''
'''
def filtrar (original,eliminar):
    lista= []
    for elemento in original:
        if elemento not in eliminar:
            if elemento not in lista:
                lista.append(elemento)
    return lista
'''
'''
lista = []
orden = int(input())
repeticiones = orden**2
i = 0
while i < repeticiones:
    x = 0
    while x < orden:
        lista.append(list(input()))
        x += 1
    i += 1
print(lista)
'''