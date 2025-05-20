descripciones = ["Coca-Cola", "7up", "Fanta", "Pepsi"]
precios = [3500.23, 2500, 3250.35, 2650.22]
stocks = [10, 4, 5, 12]

# burbujeo
# for i in range(0, len(descripciones)-1, 1):
#     for j in range(i+1, len(descripciones), 1):
#         if descripciones[i] > descripciones[j]:
#             auxiliar = descripciones[i]
#             descripciones[i] = descripciones[j]
#             descripciones[j] = auxiliar

# for i in range(len(descripciones)):
#     print(f"{descripciones[i]:<15}{precios[i]:<10}{stocks[i]:<5}")

# Si hago solo eso, no me acomoda precios y stocks


for i in range(0, len(descripciones)-1, 1):
    for j in range(i+1, len(descripciones), 1):
        if descripciones[i] > descripciones[j]:

            auxiliar = descripciones[i]
            descripciones[i] = descripciones[j]
            descripciones[j] = auxiliar

            auxiliar = precios[i]
            precios[i] = precios[j]
            precios[j] = auxiliar

            auxiliar = stocks[i]
            stocks[i] = stocks[j]
            stocks[j] = auxiliar


for i in range(len(descripciones)):
    print(f"{descripciones[i]:<15}{precios[i]:<10}{stocks[i]:<5}")

