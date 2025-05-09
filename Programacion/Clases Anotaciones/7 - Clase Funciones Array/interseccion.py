vector_a = [4,9,6,5]
vector_b = [9,4,3,2,6,4,4,4,4,4,4]

for i in range(len(vector_a)):
    for j in range(len(vector_b)):
        if vector_a[i] == vector_b[j]:
            print(f"Interseccion: {vector_a[i]}")
            break

# producto cartesiano

# modo pythonesco:
vector_c = {4,9,6,5}
vector_d = {9,4,3,2,6,4,4,4,4,4,4}
print(vector_c.intersection(vector_d)) #No se puede usar con listas