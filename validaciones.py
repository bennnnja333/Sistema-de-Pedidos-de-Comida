# ============================================
# validaciones.py - Validaciones de datos
# ============================================

def validar_opcion_menu(opcion, max_opciones):
    """
    Valida que la opción sea un número entre 1 y max_opciones
    Retorna: el número válido o None si es inválido
    """
    try:
        opcion = int(opcion)  # Convierto a entero
        if opcion >= 1 and opcion <= max_opciones:
            return opcion
        else:
            print(f"Error: Ingrese un número entre 1 y {max_opciones}")
            return None
    except ValueError:
        print("Error: Debe ingresar un número válido")
        return None

def validar_cantidad(cantidad):
    """
    Valida que la cantidad sea un número entero positivo
    Retorna: la cantidad válida o None si es inválida
    """
    try:
        cantidad = int(cantidad)
        if cantidad > 0:
            return cantidad
        else:
            print("Error: La cantidad debe ser mayor a 0")
            return None
    except ValueError:
        print("Error: Debe ingresar un número válido")
        return None

def validar_medio_pago(opcion):
    """
    Valida que el medio de pago sea uno de los disponibles (1-4)
    Retorna: el número válido o None si es inválido
    """
    try:
        opcion = int(opcion)
        if opcion >= 1 and opcion <= 4:
            return opcion
        else:
            print("Error: Seleccione una opción entre 1 y 4")
            return None
    except ValueError:
        print("Error: Debe ingresar un número válido")
        return None

def validar_si_no(respuesta):
    """
    Valida que la respuesta sea S o N (mayúscula o minúscula)
    Retorna: la respuesta en mayúscula o None si es inválida
    """
    respuesta = respuesta.upper()
    if respuesta == "S" or respuesta == "N":
        return respuesta
    else:
        print("Error: Responda con 'S' para sí o 'N' para no")
        return None
