# Tarea 1: Calcular Pagos
# Autor: Jeremi Aron Chancan Labajos

"""
    Programa para calcular pagos de una empresa para la
    TAREA 1- Programación Esencial en PYTHON
    
    Aplicar:
        Variables,
        Tipos de datos, 
        Ingreso de datos con la función input,
        Sentencia condicional IF
"""

# Datos de referencia
categorias = {
    "A": 50,
    "B": 40,
    "C": 30,
    "D": 20,
}

horas_minimas: int = 48
espacios: int = 46

# Datos de entrada
empleado: str = input("Nombre del empleado: ").title()
while True:
    try:
        horas_de_trabajo: int = int(input("Horas de trabajo: "))
        categoria: str = input("Categoria: ").upper()
        break
    except ValueError:
        print("Debes escribir un número entero")

# Inicio
def calcular_pagos():
    """Funcion principal"""
    global empleado

    # Calcular
    pago_por_hora = categorias[categoria] if categoria in categorias else 0
    horas_extra = (
        horas_de_trabajo - horas_minimas if horas_de_trabajo > horas_minimas else 0
    )
    sueldo_basico = horas_de_trabajo * pago_por_hora
    pago_por_horas_extras = (pago_por_hora * 1.40) * horas_extra  # 1.40 == 140%
    bonificacion_1 = ((sueldo_basico + pago_por_horas_extras) / 2) * 0.20  # 0.20 == 20%
    bonificacion_2 = (
        (sueldo_basico + pago_por_horas_extras + bonificacion_1) / 2
    ) * 0.18
    descuento = (sueldo_basico - bonificacion_2) * 0.8 if horas_extra else 0
    neto_a_pagar = (
        sueldo_basico + pago_por_horas_extras + bonificacion_1 + bonificacion_2
    ) - descuento

    # Motrar en pantalla
    mensaje = "Boleta de pago"
    espacios_mensaje: int = (espacios - len(mensaje)) >> 1  # Calcula la mitad ">>1"
    datos = {
        "Pago por hora": pago_por_hora,
        "Sueldo Basico": sueldo_basico,
        "Pago por horas extras": pago_por_horas_extras,
        "Bonificación 1": bonificacion_1,
        "Bonificación 2": bonificacion_2,
        "Descuento": descuento,
        "Neto a pagar": neto_a_pagar,
    }

    print(" " + "-" * espacios + " ")
    print(f"|{' '*espacios_mensaje}{mensaje}{' '*espacios_mensaje}|")
    print("|" + "-" * espacios + "|")
    print("|" + " " * espacios + "|")

    if len(empleado) > 16:
        empleado = empleado[:16] + "..."  # si supera 16 caracteres cortarlo

    mensaje = f"| Nombre del empleado: {empleado}"
    print(mensaje + " " * (espacios - len(mensaje)) + " |")
    print("|" + " " * espacios + "|")
    for (pago, cantidad) in datos.items():
        cantidad_formato = f"{cantidad:.2f}"
        cantidad = f"| S/. {cantidad_formato}{' '*(7-len(cantidad_formato))}"
        espacios_centro = 43 - (len(pago) + len(cantidad))
        print(f"| {pago}:{'_'*espacios_centro}{cantidad} |")
    print("|" + "_" * espacios + "|")


calcular_pagos()