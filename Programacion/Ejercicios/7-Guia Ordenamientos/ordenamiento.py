# Ordenamiento
# 1-Crear una función llamada ordenar_array que reciba como parámetro un array de números enteros y lo ordene 
# de forma ascendente. La función debe implementar como algoritmo de ordenamiento el método de la burbuja. 
# Además, como parámetro opcional debe recibir un booleano (que por default está en False), que en caso de 
# ser True ordena el vector en forma descendente.

# 2-Crear una función intercalar_vectores que reciba dos vectores de números enteros ordenados en orden 
# ascendente, y devuelva un único vector también ordenado. La función debe tener un parámetro opcional 
# descendente para que el vector resultante esté en orden descendente.

# 3-Crear una función que reciba como parámetro un vector de números enteros. La función debe mostrar los 
# números negativos de forma decreciente y luego los positivos de forma creciente. 
# Nota: solo se puede usar un vector, y se debe utilizar la menor cantidad de estructuras repetitivas.

lista = [5,1,4,3,2]

def ordenar_array(array: list, opcional: bool = False) -> list:
    for i in range(len(array)-1):
        for j in range(1+i,len(array)):
            if not opcional:
                if array[i] > array[j]:
                    auxiliar = array[i]
                    array[i] = array[j]
                    array[j] = auxiliar
            else:
                if array[i] < array[j]:
                    auxiliar = array[i]
                    array[i] = array[j]
                    array[j] = auxiliar

lista1 = [1,3,5,7]
lista2 = [2,4,6,8]

def intercalar_vectores(array1: list, array2: list, opcional: bool = False) -> list:
    nuevo_array = [None for _ in range(len(array1)+len(array2))]
    for i in range(len(array1)):
        nuevo_array[i*2] = array1[i]
        nuevo_array[i*2+1] = array2[i]
    for i in range(len(nuevo_array)-1):
        for j in range(i+1,len(nuevo_array)):
            if not opcional:
                if nuevo_array[i] > nuevo_array[j]:
                    auxiliar = nuevo_array[i]
                    nuevo_array[i] = nuevo_array[j]
                    nuevo_array[j] = auxiliar
            else:
                if nuevo_array[i] < nuevo_array[j]:
                    auxiliar = nuevo_array[i]
                    nuevo_array[i] = nuevo_array[j]
                    nuevo_array[j] = auxiliar

    return nuevo_array


lista_con_negativos = [-1,-4,-5,-2,-3,0,5,1,4,3,2]

def ordenar_array_con_negativos(array: list) -> list:

    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            if array[i] > array[j]:
                auxiliar = array[i]
                array[i] = array[j]
                array[j] = auxiliar

    cantidad_negativos = 0
    for i in range(len(array)):
        if array[i] < 0:
            cantidad_negativos += 1

    for i in range(cantidad_negativos//2):
        auxiliar = array[i]
        array[i] = array[cantidad_negativos-1-i]
        array[cantidad_negativos-1-i] = auxiliar

    return array

ordenar_array_con_negativos(lista_con_negativos)
print(lista_con_negativos)

