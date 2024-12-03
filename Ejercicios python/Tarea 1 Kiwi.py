import turtle
import random

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)

"""Describe this function...
"""
def tope():
  global Tope, tama_C3_B1o_columna, n_columnas, Lado, columnas, angle
  Tope = float(text_prompt('Para introducir tope ingrese 1 en caso contrario ingrese 0 :'))
  turtle.color('#%06x' % random.randint(0, 2**24 - 1))
  turtle.penup()
  if Tope == 1:
    turtle.right(90)
    turtle.forward(Lado / 2)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(int(Lado / 4))
    turtle.speed(100)
    angle = 180 - 180 / 33
    for count in range(int(33)):
      turtle.forward(Lado)
      turtle.right(angle)
    turtle.penup()
    turtle.speed(5)
    turtle.backward(int(Lado / 4))
    turtle.right(90)
    turtle.backward(Lado / 2)
    turtle.left(90)
    turtle.pendown()
  elif Tope != 1:
    print('Continuando con la columna siguiente columna...')
  turtle.color('#000000')
  turtle.pendown()

"""Describe this function...
"""
def cuadrado():
  global Tope, tama_C3_B1o_columna, n_columnas, Lado, columnas, angle
  turtle.left(90)
  for count4 in range(int(tama_C3_B1o_columna)):
    for count3 in range(4):
      turtle.forward(Lado)
      turtle.right(90)
    turtle.forward(Lado)

"""Describe this function...
"""
def continuacion_de_columna():
  global Tope, tama_C3_B1o_columna, n_columnas, Lado, columnas, angle
  turtle.penup()
  turtle.right(90)
  turtle.forward(Lado)
  turtle.right(90)
  for count5 in range(int(tama_C3_B1o_columna)):
    turtle.forward(Lado)
  turtle.left(90)
  turtle.pendown()

"""Describe this function...
"""
def pregunta_enumerada():
  global Tope, tama_C3_B1o_columna, n_columnas, Lado, columnas, angle
  tama_C3_B1o_columna = float(text_prompt(''.join([str(x) for x in ['Introduce altura de columna ', n_columnas + 1, ' : ']])))
  n_columnas = n_columnas + 1


turtle.speed(5)
print('¡Llego la hora de construir!')
turtle.shape("classic")
Lado = float(text_prompt('Introduce tamaño de el lado : '))
columnas = float(text_prompt('Introduce cantidad de columnas :'))
n_columnas = 0
turtle.penup()
turtle.goto(-150,-150)
turtle.pendown()
for count2 in range(int(columnas)):
  pregunta_enumerada()
  cuadrado()
  tope()
  continuacion_de_columna()
print('Finalizaste tu construcción, ¡felicidades!')
