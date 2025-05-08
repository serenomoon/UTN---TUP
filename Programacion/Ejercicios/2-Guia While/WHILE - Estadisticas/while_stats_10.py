# Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma de los números 
# ingresados y el promedio de los mismos.
i = 0
suma = 0
continuar = 1

while i < 10 and continuar == 1:
    j = int(input(f"Ingrese el {i + 1}° numero: "))
    suma += j
    i += 1
    
    if i >= 5 and i < 10:
        confirmacion = int(input("Ingrese 1 si quiere agregar mas numeros: "))
        continuar = confirmacion

promedio = suma / i
print(f"Promedio de los numeros: {promedio}")
print(f"Suma de los numeros: {suma}")