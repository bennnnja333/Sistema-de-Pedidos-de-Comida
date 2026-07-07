# ============================================
# datos.py - Datos del sistema
# ============================================

# Menu del restaurante
# Cada producto es un diccionario con: id, nombre, precio, categoria
MENU = [
    {"id": 1, "nombre": "Empanadas (x6)", "precio": 8500, "categoria": "Entradas"},
    {"id": 2, "nombre": "Papas fritas", "precio": 3500, "categoria": "Entradas"},
    {"id": 3, "nombre": "Hamburguesa completa", "precio": 12000, "categoria": "Platos Principales"},
    {"id": 4, "nombre": "Pizza muzzarella", "precio": 10000, "categoria": "Platos Principales"},
    {"id": 5, "nombre": "Milanesa con puré", "precio": 11000, "categoria": "Platos Principales"},
    {"id": 6, "nombre": "Gaseosa 500ml", "precio": 3000, "categoria": "Bebidas"},
    {"id": 7, "nombre": "Agua mineral", "precio": 2000, "categoria": "Bebidas"},
    {"id": 8, "nombre": "Cerveza artesanal", "precio": 3000, "categoria": "Bebidas"},
    {"id": 9, "nombre": "Helado (2 bochas)", "precio": 7000, "categoria": "Postres"},
    {"id": 10, "nombre": "Brownie con helado", "precio": 8000, "categoria": "Postres"},
]

# Promociones
PROMOCIONES = {
    "50% de descuento en bebidas desde 2 unidades": {"categoria": "Bebidas", "descuento": 50, "minimo": 2},
    "Combo familiar": {"categoria": "Platos Principales", "descuento": 15, "minimo": 3},
}

# Medios de pago
MEDIOS_PAGO = ["Efectivo", "Tarjeta de débito", "Tarjeta de crédito", "Transferencia"]

# Variables globales para estadisticas (se inicializan en 0)
pedidos_realizados = 0
total_ventas_dia = 0
productos_vendidos = {}  # Diccionario vacio
