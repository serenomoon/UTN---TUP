import random

def crear_vector(contenido: any, dimension: int) -> list:
    """Crea un vector repitiendo el "contenido" en cada uno de los espacios defiinidos por "dimension"
    Args:
        contenido (any): Contenido que llenara los indices del array (Ej: None)
        dimension (int): Cantidad de indices o posiciones que tendra el array

    Returns:
        list: Devuelve una lista "cruda"
    """
    vector = [contenido] * dimension
    return vector

def agregar_valor_lista(lista: list, nuevo_valor):
    """Toma una lista, y crea una nueva con el tamaño de la ingresada + 1 y luego agrega todos los valores
    de la anterior, mas el nuevo valor


    Args:
        lista (list): Lista a "actualizar"
        nuevo_valor (_type_): Valor nuevo a insertar en la nueva lista

    Returns:
        _type_: Devuelve una nueva lista actualizada
    """
    nueva_lista = crear_vector(None, len(lista) + 1)
    for i in range(len(lista)):
        nueva_lista[i] = lista[i]
    nueva_lista[len(lista)] = nuevo_valor
    return nueva_lista

def mostrar_cuadrado(matriz: list) -> list:
    for i in range(len(matriz)): 
        for j in range(len(matriz[i])): 
            print(f"{matriz[i][j]:>5}", end = " ") 
        print("") 



def suma_horizontal(matriz: list) -> list:
    matriz_resultados = [0] * len(matriz)
    for i in range(len(matriz)):
        suma = 0
        for j in range(len(matriz[i])):
            suma += matriz[i][j]
        matriz_resultados[i] = suma
    return matriz_resultados

def suma_vertical(matriz: list) -> list:
    matriz_resultados = [0] * len(matriz)
    for i in range(len(matriz)):
        suma = 0
        for j in range(len(matriz[i])):
            suma += matriz[j][i]
        matriz_resultados[i] = suma
    return matriz_resultados

def suma_diagonal(matriz: list) -> int:
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][i]
    return suma

def suma_diagonal_invertida(matriz: list) -> int:
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][len(matriz)-1-i]
    return suma

def verificar_cuadrado_magico(matriz: list) -> bool:
    es_magico = False
    n = len(matriz)
    M = (n * (n**2 + 1)) // 2
    suma_hor = suma_horizontal(matriz)
    suma_ver = suma_vertical(matriz)

    if len(matriz) == len(matriz[0]):
        if suma_diagonal(matriz) == M and suma_diagonal_invertida(matriz) == M:
            filas_ok = True
            for i in range(len(suma_hor)):
                if suma_hor[i] != M:
                    filas_ok = False
                    break

            columnas_ok = True
            for i in range(len(suma_ver)):
                if suma_ver[i] != M:
                    columnas_ok = False
                    break

            if filas_ok and columnas_ok:
                es_magico = True

    return es_magico

def check_in(vector: list, value: int) -> bool:
    repetido = False
    for i in range(len(vector)):
        for j in range(len(vector[i])):
            if value == vector[i][j]:
                repetido = True
    return repetido

def check_range(number: int, high: int, low: int = 1) -> bool:
    rango = False
    if number >= low and number <= high:
        rango = True
    return rango

def ingresar_cuadrado_magico(n: int) -> list:
    M = (n * (n**2 + 1)) // 2
    cuadrado = [[0] * n for _ in range(n)]
    es_magico = False
    numeros_utilizados = crear_vector(None, 0) 

    while not es_magico:
        numeros_utilizados = crear_vector(None, 0) 
        for i in range(len(cuadrado)):
            contador = 0
            for j in range(len(cuadrado[i])):
                numero_nuevo = int(input(f"Ingresa un numero entre 1 y {n**2} para la fila {i} / columna {j}: "))

                rango = check_range(numero_nuevo, n**2)
                while not rango or numero_nuevo in numeros_utilizados:
                    numero_nuevo = int(input("Error!!, el numero ya existe, o esta fuera de rango, reingreselo: "))
                    rango = check_range(numero_nuevo, n**2)
                
                cuadrado[i][j] = numero_nuevo
                numeros_utilizados = agregar_valor_lista(numeros_utilizados, numero_nuevo)
                contador += cuadrado[i][j]

            if contador != M:
                print(f"Error! La suma de los numeros de la fila ingresada deben dar como resultado: {M}")
                cuadrado = [[0] * n for _ in range(n)]
                break

        if not verificar_cuadrado_magico(cuadrado):
            print("El cuadrado ingresado no es magico.")
            si_no = input("¿Desea reingresarlo, ingrese si o no?: ")
            if si_no == "no":
                es_magico = True
        else:
            es_magico = True
            print("Cuadrado magico ingresado exitosamente!!")

    return cuadrado


def generador_cuadrado_magico():
    # n = random.randint(3, 10)  # Cambiar para aumentar el rango de nxn
    n = 3
    M = (n * (n**2 + 1)) // 2
    cuadrado = [[0] * n for _ in range(n)]
    es_magico = False
    numeros_utilizados = crear_vector(None, 0) 

    while not es_magico:
        numeros_utilizados = crear_vector(None, 0) 
        for i in range(len(cuadrado)):
            contador = 0
            for j in range(len(cuadrado[i])):
                numero_nuevo = random.randint(1,n**2)

                rango = check_range(numero_nuevo, n**2)
                while not rango or numero_nuevo in numeros_utilizados:
                    numero_nuevo = random.randint(1,n**2)
                    rango = check_range(numero_nuevo, n**2)
                
                cuadrado[i][j] = numero_nuevo
                numeros_utilizados = agregar_valor_lista(numeros_utilizados, numero_nuevo)
                contador += cuadrado[i][j]

            if contador != M:
                cuadrado = [[0] * n for _ in range(n)]
                break

        if verificar_cuadrado_magico(cuadrado):
            es_magico = True

    return cuadrado
