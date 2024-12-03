def f1(dia, rut):
    p = 0
    while p<len(rut)-1:
        if dia==rut[p:p+2]:
            return True
        p+=1
    return False

def f2(dia,rut):
    p=0
    dia = int(dia)
    if dia <=10:
        return p
    elif dia <=20:
        return p+2
    else:
        return p+5

d = int(input("Día de Nacimiento: "))
r = input("Rut (ej: 12345678-9): ")
r = r[:-2]
if d<10:
    d = "0" + str(d)
else:
    d = str(d)

v= f1(d,r)
p= f2(d,r)

if v:
    c=0
    s=""
    while c<3:
        s+=r[p+c]
        c+=1
    print(s)
else:
    c=0
    s=0
    while c<3:
        s+= int(r[p+c])
        c+=1
    print(s)