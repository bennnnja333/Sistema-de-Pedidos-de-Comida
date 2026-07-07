# Sistema de Pedidos de Comida

## Integrantes del grupo
- Bentolila, David Benjamín - Legajo: 30202
- Carballo, Santino - Legajo: 28954  
- Escobar, Martín - Legajo: 30117
- Segura , Pedro Tomas A. - Legajo: 24350

## Comisión
ISI - Comisión 1.2 - 2026

## Descripción del sistema
Sistema de gestión de pedidos para un local gastronómico. Permite:
- Visualizar el menú completo con categorías
- Armar pedidos seleccionando productos y cantidades
- Aplicar promociones automáticas (2x1 en bebidas, combo familiar)
- Calcular totales con descuentos
- Seleccionar medio de pago
- Ver estadísticas del día (total vendido, producto más pedido)

## Requisitos
- Python 3.8 o superior

## Instrucciones de ejecución
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/TU-USUARIO/sistema-pedidos-comida.git

## Uso de IA:
 - Se eligió CHATGPT como el agente a utilizar. Se utilizó principalmente como una herramienta de apoyo durante el desarrollo del trabajo. Su uso estuvo enfocado, principalmente, en dos aspectos: la modularización del programa y las validaciones de datos.
En una primera versión del proyecto, gran parte del código se encontraba dentro de la función principal (main). A partir de las sugerencias de la IA, se reorganizó el programa separando responsabilidades en distintas funciones (por ejemplo, mostrar el menú, armar el pedido, aplicar promociones y mostrar estadísticas), logrando un código más ordenado, reutilizable y fácil de mantener. Del mismo modo, la IA ayudó a identificar qué entradas del usuario era conveniente validar y cómo implementar dichas validaciones mediante funciones específicas.
También se utilizó como apoyo para implementar la lectura y escritura de estadísticas en un archivo, ya que el grupo no tenía experiencia previa con el manejo de archivos en Python. En este caso, la IA permitió comprender la lógica general de la solución, la cual luego fue adaptada e integrada al resto del sistema.
Durante el desarrollo, la IA también se empleó como herramienta de revisión ("feedback"), ayudando a detectar errores de programación y proponer mejoras de organización del código o agregar fragmentos para casos no contemplados.
 Sin embargo, el grupo encontró algunas limitaciones. Al trabajar con porciones grandes de código, la IA generaba respuestas con errores, como funciones que luego no eran utilizadas, llamadas a funciones con nombres incorrectos, variables innecesarias o inconsistencias entre distintos módulos del programa. Estos errores obligaban a revisar cuidadosamente cada sugerencia antes de incorporarla.
Además, se observaron dificultades relacionadas con el pensamiento algorítmico. En varias ocasiones la IA proponía algoritmos que resolvían únicamente el caso más simple del problema, sin contemplar situaciones particulares o casos límite. Por ejemplo, sugería soluciones que no validaban correctamente las entradas del usuario, no consideraban pedidos vacíos o aplicaban promociones "inútiles". En otros casos, proponía utilizar herramientas o funciones de Python más avanzadas que las trabajadas en la materia, alejándose del objetivo de ejercitar estructuras condicionales, repetitivas y funciones básicas.
Esta experiencia permitió concluir que, si bien la Inteligencia Artificial facilita y acelera el desarrollo de software, no reemplaza el análisis del programador. Fue necesario comprender el algoritmo propuesto, verificar su funcionamiento, adaptarlo a los requisitos de la consigna y realizar pruebas antes de incorporarlo al proyecto. En consecuencia, la IA fue utilizada como una herramienta de apoyo al aprendizaje y al desarrollo, pero las decisiones finales sobre el diseño y la implementación del sistema fueron tomadas por el grupo.
