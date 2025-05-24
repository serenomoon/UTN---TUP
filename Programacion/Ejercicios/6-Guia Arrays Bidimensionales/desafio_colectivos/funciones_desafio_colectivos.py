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

def crear_matriz(contenido: any, columnas: int, filas: int ) -> list:
    matriz = [[contenido] * columnas for _ in range(filas)]
    return matriz

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

def crear_choferes(cantidad: int) -> list:
    """Crea numeros de legajos aleatoriamente y chequea que no se repitan

    Args:
        cantidad (int): Cantidad de legajos a crear

    Returns:
        list: Lista de legajos
    """
    choferes = crear_vector(None, cantidad)
    for i in range(cantidad):
        repetido = True
        while repetido:
            nuevo_chofer = random.randint(1000,1500)
            repetido = False
            for j in range(i):
                if nuevo_chofer == choferes[j]:
                    repetido = True
                    break
        choferes[i] = nuevo_chofer
    return choferes


def crear_linea_y_coches(contenido: any, cantidad_coches_linea: int, cantidad_lineas: int) -> list:
    """Crea una cantidad de lineas y dentro de cada linea una cantidad especifica de coches

    Args:
        contenido (any): Dato que tendra cada coche
        cantidad_coches_linea (int): Cantidad de coches en cada linea
        cantidad_lineas (int): Cantidad de lineas

    Returns:
        list: Matriz de lineas con coches dentro
    """
    coches = crear_matriz(contenido, cantidad_coches_linea, cantidad_lineas)
    for i in range(len(coches)):
        for j in range(len(coches[i])):
            repetido = True
            while repetido:
                nuevo_coche = random.randint(10,150)
                repetido = False
                for k in range(i):
                    if nuevo_coche == coches[k]:
                        repetido = True
                        break
            coches[i][j] = nuevo_coche
    return coches

def confirmar_legajo(numero: int, choferes: list) -> bool:
    encontrado = False
    for i in range(len(choferes)):
        if numero == choferes[i]:
            encontrado = True
            break
    return encontrado

def confirmar_coche(numero: int, coche: list) -> bool:
    encontrado = False
    for i in range(len(coche)):
        for j in range(len(coche[i])):
            if numero == coche[i][j]:
                encontrado = True
                break
    return encontrado

def mostrar_matriz(matriz: list) -> list:
    for i in range(len(matriz)): 
        for j in range(len(matriz[i])): 
            print(f"{matriz[i][j]:>5}", end = " ") 
        print("") 

def carga_racaudacion(cantidad, numero_linea, coches, recaudaciones):
    for i in range(len(coches)):
        for j in range(len(coches[i])):
            if numero_linea == coches[i][j]:
                recaudaciones[i][j] += cantidad
    return recaudaciones

def mostrar_recaudacion_coche(coches, recaudacion):
    for i in range(len(coches)):
        for j in range(len(coches[i])): 
            print(f"Coche {coches[i][j]} ${recaudacion[i][j]}\t", end = " ")
        print("") 

def mostrar_recaudacion(coches, recaudacion):
    for i in range(len(coches)):
        total_linea = 0 
        for j in range(len(coches[i])): 
            total_linea += recaudacion[i][j]
        print(f"Total Linea {i+1}: ${total_linea}")
        print("") 

def mostrar_recaudacion_unidad(unidad, coches, recaudacion):
    recaudacion_unidad = 0
    for i in range(len(coches)):
        for j in range(len(coches[i])):
            if unidad == coches[i][j]:
                recaudacion_unidad = recaudacion[i][j]
    return recaudacion_unidad

def total_recaudacion(recaudacion):
    total_recaudado = 0
    for i in range(len(recaudacion)):
        for j in range(len(recaudacion[i])):
            total_recaudado += recaudacion[i][j]
    return total_recaudado