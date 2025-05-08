# Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y 
# el promedio de los mismos.
i = 0
suma = 0
while i < 5:
    j = int(input(f"Ingrese el {i + 1}° numero: "))
    suma += j
    i += 1
promedio = suma / i
print(f"Promedio de los numeros: {promedio}")
print(f"Suma de los numeros: {suma}")