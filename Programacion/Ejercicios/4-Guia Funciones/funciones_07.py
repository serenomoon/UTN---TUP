# Crea una función que verifique si un número dado es par o impar. 
# La función retorna True si el número es par, False en caso contrario.
def num_t_or_f(numero: float | int):
    if numero % 2 == 0:
        return True
    else:
        return False

numero_t_or_f = num_t_or_f(7)
print(f"¿El numero es par?: {numero_t_or_f}")