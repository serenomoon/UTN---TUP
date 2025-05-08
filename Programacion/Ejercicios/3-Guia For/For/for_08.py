# Realizar un programa que permita mostrar una pirámide de números. Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:
# 1
# 12
# 123
# 1234
# 12345
numero_ingresado = int(input("Ingrese un numero: "))
for i in range(1,numero_ingresado+1):
    for j in range(i):
        print(f"{j+1}", end="")
    print("")