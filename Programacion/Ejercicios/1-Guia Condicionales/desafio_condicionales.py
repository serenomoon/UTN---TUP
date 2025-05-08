# Facturación del Servicio de Agua Potable
# El acceso al agua potable es un servicio esencial para hogares, comercios e industrias. 
# Para garantizar un uso eficiente del recurso y establecer una estructura justa de costos, 
# se han definido diferentes tarifas y ajustes según el consumo y el tipo de cliente.
# Este sistema de facturación contempla una tarifa base que incluye un cargo fijo y un costo 
# variable por metro cúbico consumido. Además, se aplican bonificaciones y recargos dependiendo del consumo y 
# la categoría del usuario. En algunos casos especiales, también pueden otorgarse descuentos adicionales.
# A continuación, se detallan las reglas del sistema de facturación y los cálculos necesarios para determinar 
# el monto final a pagar.

# Tarifa base:
# Todas las facturas incluyen un cargo fijo de $7000 además del costo por consumo.
# El costo por metro cúbico (m³) de agua es de $200/m³.

# Bonificaciones y Recargos según tipo de cliente:

# Cliente Residencial:
# Si el consumo es menor a 30 m³, se aplica una bonificación del 10% sobre el costo del consumo.
# Si el consumo supera los 80 m³, se aplica un recargo del 15% sobre el costo del consumo.

# Cliente Comercial:
# Si el consumo es superior a 150 m³, se aplica una bonificación del 8% sobre el costo del consumo.
# Si el consumo supera los 300 m³, la bonificación aumenta al 12%.
# Si el consumo es menor a 50 m³, se aplica un recargo del 5%.

# Cliente Industrial:
# Si el consumo es superior a 500 m³, se aplica una bonificación del 20% sobre el costo del 
# consumo.
# Si el consumo supera los 1,000 m³, la bonificación aumenta al 30%.
# Si el consumo es menor a 200 m³, se aplica un recargo del 10%.

# Casos especiales:
# Si el cliente es Residencial y el total de la factura sin impuestos ni bonificaciones  es menor a $35000, se aplica un descuento adicional del 5%.
# En todos los casos, se aplica el IVA del 21% sobre el total.

# Requerimientos del programa:
# Solicitar al usuario:
# Cantidad de metros consumidos
# Tipo de cliente, que puede ser: Residencial, Comercial o Industrial.
# Calcular:
# Subtotal de consumo.
# Bonificaciones, si corresponde
# Recargos, si corresponde
# Subtotal, con recargos y bonificaciones.
# IVA aplicado (21%), si corresponde.
# Total final a pagar.
# Mostrar en pantalla el desglose de los cálculos.

CARGO_FIJO = 7000
COSTO_METRO = 200
IVA = 0.21

print("TIPOS DE CLIENTE:")
print("1 - Residencial")
print("2 - Comercial")
print("3 - Industrial")

cliente = int(input("Ingrese el tipo de cliente: "))
consumo = float(input("Ingrese la cantidad de m³ consumidos: "))

bonificacion = 0
recargo = 0
descuento = 0

costo_consumo = consumo * COSTO_METRO
subtotal_consumo = costo_consumo + CARGO_FIJO


match cliente:
    # RESIDENCIAL
    case 1:
        match consumo:
            case consumo if consumo < 30:
                bonificacion = costo_consumo * 0.1
            case consumo if consumo > 80:
                recargo = costo_consumo * 0.15

        match subtotal_consumo:
            case subtotal_consumo if subtotal_consumo < 35000:
                descuento = subtotal_consumo * 0.5

    # COMERCIAL
    case 2:
        match consumo:
            case consumo if consumo > 300:
                bonificacion = costo_consumo * 0.12
            case consumo if consumo > 150:
                bonificacion = costo_consumo * 0.08
            case consumo if consumo < 50:
                recargo = costo_consumo * 0.05

    # INDUSTRIAL
    case 3:
        match consumo:
            case consumo if consumo > 1000:
                bonificacion = costo_consumo * 0.3
            case consumo if consumo > 500:
                bonificacion = costo_consumo * 0.2
            case consumo if consumo < 200:
                recargo = costo_consumo * 0.1

subtotal = subtotal_consumo + recargo - bonificacion - descuento
monto_iva = subtotal * IVA
total = subtotal + monto_iva   

print("Total Facturado:")
print(f"Consumo: ${costo_consumo}")
print(f"Subtotal consumi: ${subtotal_consumo}")

print(f"Bonificacion: ${bonificacion}")
print(f"Recargo: ${recargo}")
print(f"Descuento: ${descuento}")

print(f"Subtotal: ${subtotal}")
print(f"IVA: ${monto_iva}")
print(f"TOTAL: ${total}")


                