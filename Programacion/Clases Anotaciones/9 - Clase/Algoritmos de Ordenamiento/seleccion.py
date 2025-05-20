vector = [5,1,4,3,2]

# el [] se queda con el valor mas pequeño
import time #Para ver cuanto tarda cada uno
start = time.time()

largo = len(vector)

for i in range(largo-1):
    minimo_indice = i

    for j in range(i+1, largo):
        if vector[j] < vector[minimo_indice]:
            minimo_indice = j
    
    if minimo_indice != i:
        aux = vector[i]
        vector[i] = vector[minimo_indice]
        vector[minimo_indice] = aux

end = time.time()
print((end - start)*1000000) #Lo multiplico por mil porque es un numero muy chiquito 

print(vector)