def imprime_tablero(tablero):
    for l in tablero:
        print("|" , " ".join(l), "|")
    print("")

def revisa_ganador(sim, mat):
    objetivo = len(mat)
    #filas
    for l in mat: #cada linea
        if l.count(sim)== objetivo:
            return True
    #diagonales        
    comp = []
    comp_i = []
    for i in range(objetivo): 
         comp.append(mat[i][i])
         comp_i.append(mat[i][-(i+1)])
    if comp.count(sim)== objetivo or comp_i.count(sim)==objetivo: 
        return True

    #columnas
    for j in range(objetivo):
        columna = []
        for l in mat:
            columna.append(l[j])
        if columna.count(sim) == objetivo:
            return True

    return False

t = [
["-","-","-"], 
["-","-","-"],
["-","-","-"]
]


            
