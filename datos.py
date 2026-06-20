# Menú del restaurante
# Cada producto es un diccionario con: nombre, precio, categoría

MENU = [
    {"id": 1, "nombre": "Empanadas (x6)", "precio": 4500, "categoria": "Entradas"},
    {"id": 2, "nombre": "Papas fritas", "precio": 3500, "categoria": "Entradas"},
    {"id": 3, "nombre": "Hamburguesa completa", "precio": 8500, "categoria": "Platos Principales"},
    {"id": 4, "nombre": "Pizza muzzarella", "precio": 7500, "categoria": "Platos Principales"},
    {"id": 5, "nombre": "Milanesa con puré", "precio": 9000, "categoria": "Platos Principales"},
    {"id": 6, "nombre": "Gaseosa 500ml", "precio": 2000, "categoria": "Bebidas"},
    {"id": 7, "nombre": "Agua mineral", "precio": 1500, "categoria": "Bebidas"},
    {"id": 8, "nombre": "Cerveza artesanal", "precio": 3000, "categoria": "Bebidas"},
    {"id": 9, "nombre": "Helado (2 bochas)", "precio": 4000, "categoria": "Postres"},
    {"id": 10, "nombre": "Brownie con helado", "precio": 5000, "categoria": "Postres"},
]

# Promociones (diccionario con condiciones)
PROMOCIONES = {
    "2x1 en bebidas": {"categoria": "Bebidas", "descuento": 50, "minimo": 2},
    "Combo familiar": {"categoria": "Platos Principales", "descuento": 15, "minimo": 3},
}

# Medios de pago disponibles
MEDIOS_PAGO = ["Efectivo", "Tarjeta de débito", "Tarjeta de crédito", "Transferencia"]

# Variables para estadísticas (se actualizarán durante la ejecución)
pedidos_realizados = 0
total_ventas_dia = 0
productos_vendidos = {}  # Diccionario: {nombre_producto: cantidad_vendida}
