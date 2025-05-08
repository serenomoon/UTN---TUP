# Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
# 6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
# 4 y 5                ---> Aprobado, la nota es ...
# 1, 2 y 3            ---> Desaprobado, la nota es ...

nota = int(input("Ingresar nota del 1 al 10: "))

if nota < 1 or nota > 10:
    print("La nota ingresada es incorrecta.")
elif nota >= 6:
    print(f"Promoción directa, la nota es: {nota}")
elif nota >= 4:  
    print(f"Aprobado, la nota es: {nota}")
else:  
    print(f"Desaprobado, la nota es: {nota}")