import time #Para ver cuanto tarda cada uno
start = time.time()

def merge_sort(arr):
    cantidad = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        cantidad += merge_sort(left_half)
        cantidad += merge_sort(right_half)

        i = j = k = 0

        #Combinar las dos mitades
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            cantidad += 1 #Contamos cada vez que copiamos

        #Copiar los elementos restantes del subarreglo izquierdo, si los hay
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            cantidad += 1 #Contamos cada vez que copiamos

        #Copiar los elementos restantes del subarreglo derecho, si los hay
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            cantidad += 1 #Contamos cada vez que copiamos

    return cantidad

vector = [5,1,4,3,2]
merge_sort(vector)

end = time.time()
print((end - start)*1000000) #Lo multiplico por mil porque es un numero muy chiquito
print(vector)

