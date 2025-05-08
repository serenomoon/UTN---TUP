# Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.
i = 0
suma = 0
while i < 5:
    j = int(input(f"Ingrese el {i + 1}° numero: "))
    suma += j
    i += 1
print(f"Suma de los numeros: {suma}")
promedio = suma / i
print(f"Promedio de los numeros: {promedio}")