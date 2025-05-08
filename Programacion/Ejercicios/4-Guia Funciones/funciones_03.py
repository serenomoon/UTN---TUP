# Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 
def nuevo_texto():
    texto = input("Ingresá un texto: ")
    return texto

print(f"El texto es: {nuevo_texto()}")