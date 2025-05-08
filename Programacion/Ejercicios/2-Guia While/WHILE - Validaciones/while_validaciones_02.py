# Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. 
# Solo tendrá 3 intentos.
clave = input("Ingrese una clave: ")
i = 0

while clave != "Clave" and i < 2:
    i += 1
    clave = input("Error!! Reingrese la clave: ")

if clave == "Clave":
    print("Clave correcta")
else:
    print("Cuenta bloqueada")