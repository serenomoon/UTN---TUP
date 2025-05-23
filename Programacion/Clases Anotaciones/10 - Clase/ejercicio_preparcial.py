# Una clinica veterinaria cuenta con 10 profesionales veterinarios, que trabajan en consultorios
# invidividuales. Cada profesional puede brindar 3 tipos de servicios veterinarios. Los precios de los
# servicios estan expresados en pesos(hardcodear los datos).
# Se necesita conocer las siguientes metricas:

# a.Cantidad de servicios prestados por cada profesional
# b.Promedio de turnos por tipo de servicio entre todos los veterinarios
# c.Veterinarios ordenados alfabeticamente de la A-Z junto al total que recaudo en concepto de servicios.
# d.Total recaudado por la veterinaria.

profesionales = ["Fernandez","Otero","Oviedo","Gomez","Zapata","Matienzo","Quico","Gutierrez","Romero","Albanto"]

servicios = ["Vacunacion","Peluqueria","Cirugia"]
servicios_precios = [200,300,1000]
turnos = [[2,1,3],[1,3,5],[2,4,6],[3,1,0],[1,2,1],[2,1,3],[1,3,5],[2,0,6],[3,1,0],[1,2,1]]

def servicios_por_profesional(turnos: list, profesionales: list) -> list:
    print("Servicios por profesional: ")
    for i in range(len(profesionales)):
        contador = 0
        for j in range(len(turnos[i])):
            if turnos[i][j] != 0:
                contador += 1
        print(f"{profesionales[i]}: {contador}")

def promedio_turnos_servicio(servicios: list, turnos: list) -> list:
    contador_vacunacion = 0
    contador_peluqueria = 0
    contador_cirugia = 0
    for i in range(len(turnos)):
        contador_vacunacion += turnos[i][0]
        contador_peluqueria += turnos[i][1]
        contador_cirugia += turnos[i][2]
    promedio_vacunacion = contador_vacunacion / len(turnos)
    promedio_peluqueria = contador_peluqueria / len(turnos)
    promedio_cirugia = contador_cirugia / len(turnos)

    print(f"Promedio de turnos para {servicios[0]}: {promedio_vacunacion}")
    print(f"Promedio de turnos para {servicios[1]}: {promedio_peluqueria}")
    print(f"Promedio de turnos para {servicios[2]}: {promedio_cirugia}")

def ordenar_alfabeticamente_y_recaudacion(lista_profesionales: list, turnos:list, precios: list) -> list:
    total_por_profesional = [[0] for _ in range(len(lista_profesionales))]
    for i in range(len(lista_profesionales)):
        for j in range(i+1, len(lista_profesionales)):
            if lista_profesionales[i] > lista_profesionales[j]:
                auxiliar_profesional = lista_profesionales[i]
                lista_profesionales[i] = lista_profesionales[j]
                lista_profesionales[j] = auxiliar_profesional
                
                auxiliar_turnos = turnos[i]
                turnos[i] = turnos[j]
                turnos[j] = auxiliar_turnos
    
    for i in range(len(turnos)):
        total = 0
        for j in range(len(turnos[i])):
            total += turnos[i][j] * precios[j]
        print(f"{profesionales[i]} total recaudado: ${total}")


def total_recaudado(turnos:list, precios: list) -> list:
    contador_vacunacion = 0
    contador_peluqueria = 0
    contador_cirugia = 0
    for i in range(len(turnos)):
        contador_vacunacion += turnos[i][0]
        contador_peluqueria += turnos[i][1]
        contador_cirugia += turnos[i][2]
    
    total_vacunacion = contador_vacunacion * precios[0]
    total_peluqueria = contador_peluqueria * precios[1]
    total_cirugia = contador_cirugia * precios[2]

    print(f"Total recaudado: ${total_cirugia+total_peluqueria+total_vacunacion}")

servicios_por_profesional(turnos, profesionales)

promedio_turnos_servicio(servicios,turnos)

ordenar_alfabeticamente_y_recaudacion(profesionales, turnos, servicios_precios)

total_recaudado(turnos, servicios_precios)

