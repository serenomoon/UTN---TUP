# Esto tendria q hacer con varias variables:
def mostrar(nombre,edad,profesion,esta_soltero):
    print(nombre, edad, profesion, esta_soltero)

nombre = "Juan"
edad = 25
profesion = "Ingeniero"
esta_soltero = True

mostrar(nombre, edad, profesion, esta_soltero)


# Si tengo muchos datos se complica, entonces usamos diccionarios
# Estos estan formados por clave y valor

persona = {
    "nombre": ["Juan", "Pablo"],
    "edad": 25, # Puedo poner el tipo de valor que quiera (int,float,bool,str,lista,etc...)
    "profesion": "Ingeniero",
    "esta_soltero": True
}

print(persona["nombre"]) # Imprime ["Juan","Pablo"]


# Son mutables

persona["esta_soltero"] = False # Puedo cambiar los valores
persona["email"] = "juancito@gmail.com" # Agrego una clave y le pongo un valor
persona.pop("email") # Quito la clave y sus valores, y retorna el valor (no la clave) que elimine

print(persona.keys()) # Devuelve una lista con todas las claves del diccionario
print(persona.values()) # Devuelve una lista con todas las valores del diccionario
print(persona.items()) # Devuelve una lista de tuplas con clave y valor
# [('nombre', ['Juan', 'Pablo']), ('edad', 25), ('profesion', 'Ingeniero'), ('esta_soltero', False)]

# Iterarmos un diccionario:
# Esto: 
# for clave in persona.keys():
for clave in persona: # Es lo mismo que esto
    print(f"Clave: {clave} -> Valor: {persona[clave]}")

for valor in persona.values():
    print(valor) # Devuelve los valores

for clave, valor in persona.items(): # Desempaqueto la tupla
    print(f"Clave: {clave} -> Valor: {valor}") # Accedo directamente al desempaquetar la tupla

