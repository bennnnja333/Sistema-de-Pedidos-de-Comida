from funciones import *
from datos import *
from validaciones import *

def main():
    print("SISTEMA DE PEDIDOS")
    print("1. Ver menú")
    print("2. Salir")
    
    opcion = input("Elija: ")
    
    if opcion == "1":
        mostrar_menu()
    elif opcion == "2":
        print("Hasta luego")

if __name__ == "__main__":
    main()