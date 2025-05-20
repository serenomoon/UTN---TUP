# Divide la lista en 2 y elijge un pivot, se fija cual es <= al pivot y >= al pivot
# Si la lista es larga vuelve a particionar y a repetir
# Luego recolecta los elementos que se quedaron solos, sin particionar, los pivots

# Usamos recursividad
import time #Para ver cuanto tarda cada uno
start = time.time()

def swap(a: int, b: int):
    return b,a

def particionar(array, low, high):
    pivote = array[high] #El pivote sera el ultimo elemento de la lista
    i = low - 1

    for j in range(low, high):

        if array[j] <= pivote:
            i += 1
            array[i], array[j] = swap(array[i], array[j]) 
    
    array[i + 1], array[high], = swap(array[i + 1], array[high])

    return i + 1

def quick_sort(array, low, high):
    if low < high:
        pi = particionar(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)

vector = [5,1,4,3,2]
quick_sort(vector, 0, len(vector) -1)

end = time.time()
print((end - start)*1000000) #Lo multiplico por mil porque es un numero muy chiquito

print(vector)
