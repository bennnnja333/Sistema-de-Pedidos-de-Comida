from datos import MENU, PROMOCIONES, MEDIOS_PAGO, pedidos_realizados, total_ventas_dia, productos_vendidos
from validaciones import *
import os

# ============ FUNCIONES DE VISUALIZACIÓN ============

def mostrar_menu_completo():
    """Muestra todo el menú con sus categorías"""
    print("\n" + "="*50)
    print("📋 MENÚ DEL DÍA")
    print("="*50)
    
    categorias = ["Entradas", "Platos Principales", "Bebidas", "Postres"]
    
    for categoria in categorias:
        print(f"\n🍽️ {categoria.upper()}:")
        for producto in MENU:
            if producto["categoria"] == categoria:
                print(f"  [{producto['id']:2d}] {producto['nombre']:30} ${producto['precio']:,.0f}")
    
    print("\n" + "="*50)

def mostrar_promociones():
    """Muestra las promociones disponibles"""
    print("\n🎉 PROMOCIONES DISPONIBLES:")
    for nombre, promocion in PROMOCIONES.items():
        print(f"  • {nombre}: {promocion['descuento']}% de descuento comprando {promocion['minimo']} {promocion['categoria']}")

# ============ FUNCIONES DE PEDIDO ============

def armar_pedido():
    """Función principal para armar un pedido"""
    pedido = []
    total = 0
    
    print("\n🛒 ARMANDO PEDIDO")
    print("="*50)
    
    # Mostrar promociones al inicio
    mostrar_promociones()
    
    while True:
        mostrar_menu_completo()
        
        # Seleccionar producto
        print("\n0. Finalizar pedido")
        opcion = input("Seleccione el número del producto (o 0 para finalizar): ")
        
        if opcion == "0":
            break
        
        # Validar opción
        opcion_valida = validar_opcion_menu(opcion, len(MENU))
        if opcion_valida is None:
            continue
        
        # Buscar el producto
        producto_seleccionado = None
        for producto in MENU:
            if producto["id"] == opcion_valida:
                producto_seleccionado = producto
                break
        
        if producto_seleccionado is None:
            print("⚠️ Producto no encontrado")
            continue
        
        # Pedir cantidad
        print(f"\nProducto seleccionado: {producto_seleccionado['nombre']} (${producto_seleccionado['precio']:,.0f})")
        cantidad = input("Cantidad: ")
        cantidad_valida = validar_cantidad(cantidad)
        
        if cantidad_valida is None:
            continue
        
        # Agregar al pedido
        pedido.append({
            "producto": producto_seleccionado,
            "cantidad": cantidad_valida,
            "subtotal": producto_seleccionado["precio"] * cantidad_valida
        })
        
        total += producto_seleccionado["precio"] * cantidad_valida
        
        print(f"✅ Agregado: {cantidad_valida} x {producto_seleccionado['nombre']}")
        print(f"Subtotal actual: ${total:,.0f}")
        
        # Preguntar si quiere seguir agregando
        continuar = input("\n¿Agregar otro producto? (S/N): ")
        while continuar.upper() not in ["S", "N"]:
            print("⚠️ Responda con S o N")
            continuar = input("¿Agregar otro producto? (S/N): ")
        
        if continuar.upper() == "N":
            break
    
    if not pedido:
        print("❌ No se agregaron productos al pedido")
        return None
    
    return pedido, total

def aplicar_promociones(pedido, total):
    """Aplica promociones al pedido y calcula descuentos"""
    descuento_total = 0
    promociones_aplicadas = []
    
    # Contar productos por categoría
    categorias_pedido = {}
    for item in pedido:
        categoria = item["producto"]["categoria"]
        if categoria not in categorias_pedido:
            categorias_pedido[categoria] = 0
        categorias_pedido[categoria] += item["cantidad"]
    
    # Aplicar cada promoción
    for nombre_promo, datos_promo in PROMOCIONES.items():
        categoria = datos_promo["categoria"]
        minimo = datos_promo["minimo"]
        descuento = datos_promo["descuento"]
        
        if categoria in categorias_pedido and categorias_pedido[categoria] >= minimo:
            # Calcular descuento (se aplica sobre el total de esa categoría)
            total_categoria = 0
            for item in pedido:
                if item["producto"]["categoria"] == categoria:
                    total_categoria += item["subtotal"]
            
            descuento_aplicado = total_categoria * (descuento / 100)
            descuento_total += descuento_aplicado
            promociones_aplicadas.append({
                "nombre": nombre_promo,
                "descuento": descuento_aplicado
            })
    
    total_con_descuento = total - descuento_total
    
    return total_con_descuento, descuento_total, promociones_aplicadas

def mostrar_resumen_pedido(pedido, total, total_con_descuento, descuento_total, promociones_aplicadas):
    """Muestra el resumen del pedido"""
    print("\n" + "="*50)
    print("🧾 RESUMEN DEL PEDIDO")
    print("="*50)
    
    for item in pedido:
        print(f"  {item['cantidad']} x {item['producto']['nombre']:30} ${item['subtotal']:,.0f}")
    
    print("-"*50)
    print(f"Subtotal: ${total:,.0f}")
    
    if promociones_aplicadas:
        print("\n🎉 PROMOCIONES APLICADAS:")
        for promo in promociones_aplicadas:
            print(f"  • {promo['nombre']}: -${promo['descuento']:,.0f}")
        print(f"Total con descuento: ${total_con_descuento:,.0f}")
    else:
        print(f"Total: ${total:,.0f}")
    
    return total_con_descuento

def seleccionar_medio_pago():
    """Permite seleccionar el medio de pago"""
    print("\n💳 MEDIOS DE PAGO:")
    for i, medio in enumerate(MEDIOS_PAGO, 1):
        print(f"  {i}. {medio}")
    
    while True:
        opcion = input("Seleccione medio de pago (1-4): ")
        opcion_valida = validar_medio_pago(opcion)
        if opcion_valida is not None:
            return MEDIOS_PAGO[opcion_valida - 1]

# ============ FUNCIONES DE ESTADÍSTICAS ============

def actualizar_estadisticas(pedido, total_venta):
    """Actualiza las estadísticas globales del sistema"""
    global pedidos_realizados, total_ventas_dia, productos_vendidos
    
    pedidos_realizados += 1
    total_ventas_dia += total_venta
    
    for item in pedido:
        nombre = item["producto"]["nombre"]
        cantidad = item["cantidad"]
        if nombre in productos_vendidos:
            productos_vendidos[nombre] += cantidad
        else:
            productos_vendidos[nombre] = cantidad

def mostrar_estadisticas():
    """Muestra las estadísticas del día"""
    global pedidos_realizados, total_ventas_dia, productos_vendidos
    
    print("\n" + "="*50)
    print("📊 ESTADÍSTICAS DEL DÍA")
    print("="*50)
    print(f"Pedidos realizados: {pedidos_realizados}")
    print(f"Total vendido: ${total_ventas_dia:,.0f}")
    
    if productos_vendidos:
        # Producto más vendido
        producto_mas_vendido = max(productos_vendidos, key=productos_vendidos.get)
        print(f"Producto más vendido: {producto_mas_vendido} ({productos_vendidos[producto_mas_vendido]} unidades)")
        
        print("\n📦 Detalle de ventas:")
        for producto, cantidad in sorted(productos_vendidos.items(), key=lambda x: x[1], reverse=True):
            print(f"  • {producto}: {cantidad} unidades")
    else:
        print("No se han vendido productos aún")

def limpiar_pantalla():
    """Limpia la pantalla (para mejor visualización)"""
    os.system('cls' if os.name == 'nt' else 'clear')
