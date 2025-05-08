# Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.
nota = int(input("Ingrese una nota: "))

while nota < 1 or nota > 10:
    nota = int(input("Error!! La nota ingresada debe estar entre 1 y 10, Reingrese la nota: "))
print("Nota ingresada")
