from funciones import *
from datos import pedidos_realizados, total_ventas_dia, productos_vendidos
import sys

def main():
    """Función principal del sistema"""
    
    print("\n" + "="*50)
    print("🍕 BIENVENIDO AL SISTEMA DE PEDIDOS")
    print("="*50)
    print("Restaurante 'El Buen Sabor'")
    print("="*50)
    
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ver menú completo")
        print("2. Realizar un pedido")
        print("3. Ver promociones")
        print("4. Ver estadísticas del día")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción (1-5): ")
        
        if opcion == "1":
            limpiar_pantalla()
            mostrar_menu_completo()
            input("\nPresione Enter para continuar...")
            
        elif opcion == "2":
            limpiar_pantalla()
            resultado = armar_pedido()
            
            if resultado is not None:
                pedido, total = resultado
                
                # Aplicar promociones
                total_con_descuento, descuento_total, promociones_aplicadas = aplicar_promociones(pedido, total)
                
                # Mostrar resumen
                total_final = mostrar_resumen_pedido(pedido, total, total_con_descuento, descuento_total, promociones_aplicadas)
                
                # Seleccionar medio de pago
                medio_pago = seleccionar_medio_pago()
                print(f"\n💵 Medio de pago seleccionado: {medio_pago}")
                print(f"💰 Total a pagar: ${total_final:,.0f}")
                
                # Confirmar pedido
                confirmar = input("\n¿Confirmar pedido? (S/N): ")
                while confirmar.upper() not in ["S", "N"]:
                    print("⚠️ Responda con S o N")
                    confirmar = input("¿Confirmar pedido? (S/N): ")
                
                if confirmar.upper() == "S":
                    actualizar_estadisticas(pedido, total_final)
                    print("\n✅ ¡PEDIDO CONFIRMADO! Gracias por su compra.")
                else:
                    print("\n❌ Pedido cancelado")
            
            input("\nPresione Enter para continuar...")
            
        elif opcion == "3":
            limpiar_pantalla()
            mostrar_promociones()
            input("\nPresione Enter para continuar...")
            
        elif opcion == "4":
            limpiar_pantalla()
            mostrar_estadisticas()
            input("\nPresione Enter para continuar...")
            
        elif opcion == "5":
            print("\n" + "="*50)
            print("👋 ¡Gracias por usar nuestro sistema!")
            print("="*50)
            print(f"Resumen del día: {pedidos_realizados} pedidos - ${total_ventas_dia:,.0f} vendidos")
            sys.exit()
            
        else:
            print("⚠️ Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
