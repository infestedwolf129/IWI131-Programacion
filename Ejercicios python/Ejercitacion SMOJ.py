'''
a= float(input(""))
b= float(input(""))
c= float(input(""))

Triangulo = (a+b)>c and (b+c)>a and (a+c)>b
Equilatero = (a == b) and c
Isoceles = (a==b) or (a==c)or (b==c)
Escaleno = a!=b!=c

Hipotenusa = 0
if Hipotenusa == 0:
    if a> (b or c):
        Hipotenusa = a
    elif b> (a or c):
        Hipotenusa = b
    else:
        Hipotenusa = c
if Hipotenusa == a:
    Rectangulo = b**2+c**2 == a**2
elif Hipotenusa == b:
   Rectangulo = a**2+c**2 == b**2
else:
    Rectangulo = a**2+b**2 == c**2
if Triangulo:
    if Equilatero:
        print("Triangulo equilatero")
    elif Isoceles:
        if Rectangulo:
          print("Triangulo isosceles rectangulo")
        else:
            print("Triangulo isosceles")
    elif Escaleno:
        if Rectangulo:
            print("Triangulo escaleno rectangulo")
        else:
            print("Triangulo escaleno")
else:
    print("No es Triangulo")
'''

n1 = int(input(""))
n2 = int(input(""))

if(n1>=n2):
    Mayor = n1
    Menor = n2
if(n2>=n1):
    Mayor = n2
    Menor = n1
if(Menor==0):
    print("error")
else:
    Cociente = Mayor/Menor
    print(float(Cociente))
