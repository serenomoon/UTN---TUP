# Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
# En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
# Si es invierno: solo se viaja a Bariloche.
# Si es verano: se viaja a Mar del plata y Cataratas.
# Si es otoño: se viaja a todos los lugares.
# Si es primavera: se viaja a todos los lugares menos Bariloche.


print("INDICAR ESTACION")
print("1 - Verano")
print("2 - Otoño")
print("3 - Invierno")
print("4 - Primavera")
estacion = int(input("Seleccionar la estacion: "))

print("A QUE LUGAR QUIERE IR?")
print("1 - Bariloche")
print("2 - Mar del plata")
print("3 - Cataratas")
lugar = int(input("Ingrese el lugar al que quiere viajar: "))

match estacion:
    # VERANO
    case 1: 
        match lugar:
            case 2 | 3:
                print("Se viaja")
            case _:
                print("No se viaja")
    
    # OTOÑO
    case 2:  
        print("Se viaja")
    
    # INVIERNO
    case 3:  
        match lugar:
            case 1:
                print("Se viaja")
            case _:
                print("No se viaja")
    
    # PRIMAVERA
    case 4: 
        match lugar:
            case 1:
                print("No se viaja")
            case _:
                print("Se viaja")
    
    case _: 
        print("La estacion no existe")
