# Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. 
# Tendrá intentos indeterminados.
clave = input("Ingrese una clave: ") #Clave 

while clave != "Clave":
    clave = input("Error!! Reingrese la clave: ")

print("Clave correcta")