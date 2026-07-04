# ============================================
# main.py - Menú principal del sistema
# ============================================

from funciones import *
from datos import pedidos_realizados, total_ventas_dia
import sys

def main():
    """
    Función principal del sistema
    """
    
    print("\n" + "="*50)
    print("---BIENVENIDO AL SISTEMA DE PEDIDOS---")
    print("="*50)
    print("Restaurante 'El Buen Sabor'")
    print("="*50)
    print("\n¡Hola! ¿Qué deseas hacer hoy?")
    
    # Bucle principal del programa
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ver menú completo")
        print("2. Realizar un pedido")
        print("3. Ver promociones")
        print("4. Ver estadísticas del día")
        print("5. Guardar estadísticas en archivo")
        print("6. Leer estadísticas del archivo")
        print("7. Salir")
        
        opcion = input("\nSeleccione una opción (1-7): ")
        
        # Estructura condicional multiple
        if opcion == "1":
            limpiar_pantalla()
            mostrar_menu_completo()
            input("\nPresione Enter para continuar...")
            
        elif opcion == "2":
            limpiar_pantalla()
            pedido, total = armar_pedido()
            
            # Verifico que el pedido no este vacío
            if pedido is not None:
                # Aplico promociones
                total_con_descuento, descuento_total, promociones_aplicadas = aplicar_promociones(pedido, total)
                
                # Muestro resumen
                total_final = mostrar_resumen_pedido(pedido, total, total_con_descuento, descuento_total, promociones_aplicadas)
                
                # Selecciona medio de pago
                medio_pago = seleccionar_medio_pago()
                print(f"\nMedio de pago seleccionado: {medio_pago}")
                print(f"Total a pagar: ${total_final:,.0f}")
                
                # Confirmo pedido
                confirmar = input("\n¿Confirmar pedido? (S/N): ")
                confirmar = validar_si_no(confirmar)
                
                # Si la validacion falla, preguntamos de nuevo
                while confirmar is None:
                    confirmar = input("¿Confirmar pedido? (S/N): ")
                    confirmar = validar_si_no(confirmar)
                
                if confirmar == "S":
                    # Actualizo estadisticas
                    actualizar_estadisticas(pedido, total_final)
                    print("\n¡PEDIDO CONFIRMADO!")
                    print(f"Número de pedido: {pedidos_realizados}")
                    print("¡Gracias por su compra!")
                else:
                    print("\n❌ Pedido cancelado")
            else:
                print("\n❌ No se pudo realizar el pedido")
            
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
            limpiar_pantalla()
            guardar_estadisticas_en_archivo()
            input("\nPresione Enter para continuar...")
            
        elif opcion == "6":
            limpiar_pantalla()
            leer_estadisticas_de_archivo()
            input("\nPresione Enter para continuar...")
            
        elif opcion == "7":
            print("\n" + "="*50)
            print("¡Gracias por usar nuestro sistema!")
            print("="*50)
            print(f"Resumen del día: {pedidos_realizados} pedidos")
            print(f"Total vendido: ${total_ventas_dia:,.0f}")
            print("="*50)
            print("¡Vuelva pronto!")
            sys.exit()
            
        else:
            print("\nOpción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
