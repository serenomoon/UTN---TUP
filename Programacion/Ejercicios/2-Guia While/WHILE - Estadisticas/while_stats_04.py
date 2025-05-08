# Mostrar la suma de los números pares desde el 1 hasta el 10.
i = 0
suma = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        suma += i
print(f"La suma de los numeros pares es: {suma}")