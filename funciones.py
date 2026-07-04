# ============================================
# funciones.py - Funciones del sistema
# ============================================

from datos import MENU, PROMOCIONES, MEDIOS_PAGO
from datos import pedidos_realizados, total_ventas_dia, productos_vendidos
import datos
from validaciones import *
import os

# FUNCIONES DE VISUALIZACION

def mostrar_menu_completo():
    """Muestra todo el menú con sus categorías"""
    print("\n" + "="*50)
    print("---MENÚ DEL DÍA---")
    print("="*50)
    
    # Lista de categorias en orden
    categorias = ["Entradas", "Platos Principales", "Bebidas", "Postres"]
    
    # Recorro cada categoria
    for categoria in categorias:
        print(f"\n{categoria.upper()}:")
        # Recorro todos los productos
        for producto in MENU:
            if producto["categoria"] == categoria:
                # Muestro el producto con formato
                print(f"  [{producto['id']:2d}] {producto['nombre']:30} ${producto['precio']:,.0f}")
    
    print("\n" + "="*50)

def mostrar_promociones():
    """Muestra las promociones disponibles"""
    print("\n" + "="*50)
    print("---PROMOCIONES DISPONIBLES---")
    print("="*50)
    
    # Recorro el diccionario de promociones
    for nombre, promocion in PROMOCIONES.items():
        print(f"  • {nombre}: {promocion['descuento']}% de descuento")
        print(f"    (comprando {promocion['minimo']} {promocion['categoria']})")
    
    print("="*50)

# FUNCIONES DE PEDIDO

def armar_pedido():
    """
    Función principal para armar un pedido
    Retorna: una lista con los items del pedido y el total
    """
    pedido = []  # Lista vacia para guardar los productos
    total = 0    # Acumulador para el total
    
    print("\n" + "="*50)
    print("🛒 ARMANDO PEDIDO")
    print("="*50)
    
    # Muestro promociones al inicio
    mostrar_promociones()
    
    # Bucle while para agregar productos
    while True:
        mostrar_menu_completo()
        
        print("\n0. Finalizar pedido")
        opcion = input("Seleccione el número del producto (o 0 para finalizar): ")
        
        # Si elige 0, salimos del bucle
        if opcion == "0":
            break
        
        # Validar la opción
        opcion_valida = validar_opcion_menu(opcion, len(MENU))
        if opcion_valida is None:
            continue  # Vuelve a preguntar
        
        # Busco el producto seleccionado
        producto_seleccionado = None
        for producto in MENU:
            if producto["id"] == opcion_valida:
                producto_seleccionado = producto
                break
        
        # Si no encontro el producto
        if producto_seleccionado is None:
            print("Producto no encontrado")
            continue
        
        # Muestro el producto seleccionado
        print(f"\nProducto seleccionado: {producto_seleccionado['nombre']}")
        print(f"Precio unitario: ${producto_seleccionado['precio']:,.0f}")
        
        # Pido la cantidad
        cantidad = input("Cantidad: ")
        cantidad_valida = validar_cantidad(cantidad)
        if cantidad_valida is None:
            continue  # Vuelve a preguntar
        
        # Calculo el subtotal
        subtotal = producto_seleccionado["precio"] * cantidad_valida
        
        # Agrego al pedido
        pedido.append({
            "producto": producto_seleccionado,
            "cantidad": cantidad_valida,
            "subtotal": subtotal
        })
        
        # Actualizo el total
        total = total + subtotal
        
        print(f"Agregado: {cantidad_valida} x {producto_seleccionado['nombre']}")
        print(f"Subtotal actual: ${total:,.0f}")
        
        # Preguntar si quiere seguir agregando
        continuar = input("\n¿Agregar otro producto? (S/N): ")
        continuar = validar_si_no(continuar)
        if continuar is None:
            # Si la validación falla, preguntamos de nuevo
            continuar = input("¿Agregar otro producto? (S/N): ")
            continuar = validar_si_no(continuar)
        
        if continuar == "N":
            break
    
    # Verifico si el pedido esta vacio
    if len(pedido) == 0:
        print("\n❌ No se agregaron productos al pedido")
        return None, 0
    
    return pedido, total

def aplicar_promociones(pedido, total):
    """
    Aplica promociones al pedido y calcula descuentos
    Retorna: total con descuento, descuento total, lista de promociones aplicadas
    """
    descuento_total = 0
    promociones_aplicadas = []
    
    # Contar productos por categoria
    categorias_pedido = {}
    for item in pedido:
        categoria = item["producto"]["categoria"]
        # Si la categoria no existe en el diccionario, la creamos
        if categoria not in categorias_pedido:
            categorias_pedido[categoria] = 0
        categorias_pedido[categoria] = categorias_pedido[categoria] + item["cantidad"]
    
    # Aplico cada promoción
    for nombre_promo, datos_promo in PROMOCIONES.items():
        categoria = datos_promo["categoria"]
        minimo = datos_promo["minimo"]
        descuento = datos_promo["descuento"]
        
        # Verifico si la categoria esta en el pedido y cumple el minimo
        if categoria in categorias_pedido:
            if categorias_pedido[categoria] >= minimo:
                # Calculo el total de esa categoria
                total_categoria = 0
                for item in pedido:
                    if item["producto"]["categoria"] == categoria:
                        total_categoria = total_categoria + item["subtotal"]
                
                # Calculo el descuento
                descuento_aplicado = total_categoria * descuento / 100
                descuento_total = descuento_total + descuento_aplicado
                
                # Guardo la promocion aplicada
                promociones_aplicadas.append({
                    "nombre": nombre_promo,
                    "descuento": descuento_aplicado
                })
    
    total_con_descuento = total - descuento_total
    return total_con_descuento, descuento_total, promociones_aplicadas

def mostrar_resumen_pedido(pedido, total, total_con_descuento, descuento_total, promociones_aplicadas):
    """
    Muestra el resumen del pedido
    Retorna: el total final
    """
    print("\n" + "="*50)
    print("---RESUMEN DEL PEDIDO---")
    print("="*50)
    
    # Mostrar cada item del pedido
    for item in pedido:
        print(f"  {item['cantidad']} x {item['producto']['nombre']:30} ${item['subtotal']:,.0f}")
    
    print("-"*50)
    print(f"Subtotal: ${total:,.0f}")
    
    # Muestro promociones aplicadas si hay
    if len(promociones_aplicadas) > 0:
        print("\n🎉 PROMOCIONES APLICADAS:")
        for promo in promociones_aplicadas:
            print(f"  • {promo['nombre']}: -${promo['descuento']:,.0f}")
        print(f"\nTotal con descuento: ${total_con_descuento:,.0f}")
    else:
        print(f"\nTotal: ${total:,.0f}")
    
    print("="*50)
    
    return total_con_descuento

def seleccionar_medio_pago():
    """
    Permite seleccionar el medio de pago
    Retorna: el medio de pago seleccionado
    """
    print("\n" + "="*50)
    print("💳 MEDIOS DE PAGO")
    print("="*50)
    
    # Muestro los medios de pago con un bucle for
    for i in range(len(MEDIOS_PAGO)):
        print(f"  {i+1}. {MEDIOS_PAGO[i]}")
    
    while True:
        opcion = input("\nSeleccione medio de pago (1-4): ")
        opcion_valida = validar_medio_pago(opcion)
        if opcion_valida is not None:
            return MEDIOS_PAGO[opcion_valida - 1]

# FUNCIONES DE ESTADISTICAS

def actualizar_estadisticas(pedido, total_venta):
    """
    Actualiza las estadísticas globales del sistema
    """

    # Incremento contadores
    datos.pedidos_realizados = datos.pedidos_realizados + 1
    datos.total_ventas_dia = datos.total_ventas_dia + total_venta

    # Actualizo productos vendidos
    for item in pedido:
        nombre = item["producto"]["nombre"]
        cantidad = item["cantidad"]

        # Si el producto ya esta en el diccionario, sumamos
        if nombre in datos.productos_vendidos:
            datos.productos_vendidos[nombre] = datos.productos_vendidos[nombre] + cantidad
        else:
            # Si no esta, lo agregamos
            datos.productos_vendidos[nombre] = cantidad

def mostrar_estadisticas():
    """
    Muestra las estadísticas del día
    """

    print("\n" + "="*50)
    print("ESTADÍSTICAS DEL DÍA")
    print("="*50)
    print(f"Pedidos realizados: {datos.pedidos_realizados}")
    print(f"Total vendido: ${datos.total_ventas_dia:,.0f}")

    # Verifico si hay productos vendidos
    if len(datos.productos_vendidos) > 0:
        # Encontrar el producto mas vendido
        producto_mas_vendido = ""
        cantidad_maxima = 0

        for producto, cantidad in datos.productos_vendidos.items():
            if cantidad > cantidad_maxima:
                cantidad_maxima = cantidad
                producto_mas_vendido = producto

        print(f"\nProducto más vendido: {producto_mas_vendido}")
        print(f"   ({cantidad_maxima} unidades)")

        print("\nDetalle de ventas:")
        for producto, cantidad in datos.productos_vendidos.items():
            print(f"  • {producto}: {cantidad} unidades")
    else:
        print("\nNo se han vendido productos aún")

    print("="*50)

def limpiar_pantalla():
    """Limpia la pantalla para mejor visualización"""
    # os.name nos dice el sistema operativo
    # 'nt' es Windows, 'posix' es Linux/Mac
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# FUNCIONES DE ARCHIVOS

def guardar_estadisticas_en_archivo():
    """
    Guarda las estadísticas del día en un archivo .txt
    """

    try:
        with open("estadisticas_dia.txt", "w") as archivo:
            archivo.write("="*50 + "\n")
            archivo.write("ESTADÍSTICAS DEL DÍA\n")
            archivo.write("="*50 + "\n")
            archivo.write(f"Pedidos realizados: {datos.pedidos_realizados}\n")
            archivo.write(f"Total vendido: ${datos.total_ventas_dia:,.0f}\n")

            if len(datos.productos_vendidos) > 0:
                archivo.write("\nDetalle de ventas:\n")
                for producto, cantidad in datos.productos_vendidos.items():
                    archivo.write(f"  • {producto}: {cantidad} unidades\n")
            else:
                archivo.write("\nNo se han vendido productos aún\n")

            archivo.write("="*50 + "\n")

        print("\nEstadísticas guardadas en 'estadisticas_dia.txt'")
    except:
        print("\nError al guardar el archivo")

def leer_estadisticas_de_archivo():
    """
    Lee y muestra el contenido del archivo de estadísticas
    """
    try:
        with open("estadisticas_dia.txt", "r") as archivo:
            contenido = archivo.read()
            print("\n" + contenido)
    except FileNotFoundError:
        print("\nNo hay estadísticas guardadas aún")
    except:
        print("\nError al leer el archivo")
