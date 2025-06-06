tupla = (5,9,6,7) # La tupla es inmutable
# tupla[0] seria 5
# puedo hacerle un for tmb

tupla = tuple([3,5,9]) # Para convertir datos a tupla
# Usamos las tuplas para datos que no deben ser cambiados, x ej el tamaño de una pantalla
PANTALLA = (500,700)

alto, ancho = PANTALLA # Desempaquetado de tupla
# Alto seria 500 y ancho seria 700
# Si tengo 2 datos, tengo que ponerlas en 2 variables, ni mas ni menos

lista = list(PANTALLA) # Desempaqueto la tupla en una lista


tupla2 = (5,6,5,5,6,9)
print(tupla2.count(5)) # Me imprime cuantas veces aparece el 5
print(tupla2.index(6)) # En que inidice esta el valor 6 (el primero)
