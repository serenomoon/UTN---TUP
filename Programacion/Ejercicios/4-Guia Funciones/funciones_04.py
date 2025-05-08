# Escribir una función que calcule el área de un rectángulo. 
# La función recibe la base y la altura y retorna el área.
def area_rectangulo(base: float | int, altura: float | int):
    area = base * altura
    return area

nueva_area_rectangulo = area_rectangulo(5, 3)
print(f"El area de el rectangulo es: {nueva_area_rectangulo}")