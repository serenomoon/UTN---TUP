# Ingresar 10 números enteros. Determinar el máximo y el mínimo.
contador = 0

while contador < 10:
    numero = int(input("Ingrese un numero: "))
    if contador == 0 or numero > maximo:
        maximo = numero
    if contador == 0 or numero < minimo:
        minimo = numero
    
    contador += 1

print(f"Maximo: {maximo}")
print(f"Minimo: {minimo}")