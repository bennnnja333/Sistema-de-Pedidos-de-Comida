def validar_opcion_menu(opcion, max_opciones):
    """Valida que la opción sea un número dentro del rango permitido"""
    try:
        opcion = int(opcion)
        if 1 <= opcion <= max_opciones:
            return opcion
        else:
            print(f"⚠️ Error: Ingrese un número entre 1 y {max_opciones}")
            return None
    except ValueError:
        print("⚠️ Error: Debe ingresar un número válido")
        return None

def validar_cantidad(cantidad):
    """Valida que la cantidad sea un número entero positivo"""
    try:
        cantidad = int(cantidad)
        if cantidad > 0:
            return cantidad
        else:
            print("⚠️ Error: La cantidad debe ser mayor a 0")
            return None
    except ValueError:
        print("⚠️ Error: Debe ingresar un número válido")
        return None

def validar_medio_pago(opcion):
    """Valida que el medio de pago sea uno de los disponibles"""
    medios = ["1", "2", "3", "4"]
    if opcion in medios:
        return int(opcion)
    else:
        print("⚠️ Error: Medio de pago no válido")
        return None

def validar_continuar(respuesta):
    """Valida que la respuesta sea S o N"""
    respuesta = respuesta.upper()
    if respuesta in ["S", "N"]:
        return respuesta
    else:
        print("⚠️ Error: Responda con 'S' para sí o 'N' para no")
        return None
