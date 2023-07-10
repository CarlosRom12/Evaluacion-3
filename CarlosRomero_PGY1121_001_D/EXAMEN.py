# Definición de variables y listas
import os
os.system ("cls")

ubicaciones = ["Santiago", "Valparaíso", "Concepción"]
asientos_disponibles = [30, 20, 40]
precio_platinum = 120000
precio_gold = 80000
precio_silver = 50000
ganancia_total = 0
entradas_vendidas = [3, 4, 10]

# Función para mostrar el menú de ubicaciones o asientos disponibles
def mostrar_menu():
    print("=== Menú de Ubicaciones/Asientos ===")
    for i in range(len(ubicaciones)):
        print(f"{i+1}. {ubicaciones[i]} ({asientos_disponibles[i]} asientos disponibles)")
    print("==========================")

# Función para calcular la ganancia total y la cantidad de entradas vendidas
def calcular_ganancia():
    global ganancia_total
    global entradas_vendidas
    ganancia_total = (entradas_vendidas[0] * precio_platinum) + (entradas_vendidas[1] * precio_gold) + (entradas_vendidas[2] * precio_silver)
    entradas_vendidas_total = sum(entradas_vendidas)
    print(f"Cantidad de entradas vendidas: {entradas_vendidas_total}")

# Función principal
def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la ubicación/asiento (0 para salir): ")
        
        if opcion == "0":
            calcular_ganancia()
            print(f"Ganancia total: ${ganancia_total}")
            break
        
        try:
            opcion = int(opcion)
            if opcion >= 1 and opcion <= len(ubicaciones):
                ubicacion_seleccionada = ubicaciones[opcion-1]
                asientos_disponibles_seleccionados = asientos_disponibles[opcion-1]
                print(f"Ubicación seleccionada: {ubicacion_seleccionada}")
                print(f"Asientos disponibles: {asientos_disponibles_seleccionados}")
                cantidad_entradas = int(input("Ingrese la cantidad de entradas a comprar (1-3): "))
                if cantidad_entradas >= 1 and cantidad_entradas <= 3:
                    if cantidad_entradas <= asientos_disponibles_seleccionados:
                        asientos_disponibles[opcion-1] -= cantidad_entradas
                        entradas_vendidas[opcion-1] += cantidad_entradas
                        print(f"¡Compra exitosa! Se han comprado {cantidad_entradas} entradas.")
                    else:
                        print("No hay suficientes asientos disponibles.")
                else:
                    print("La cantidad de entradas a comprar debe ser entre 1 y 3.")
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el programa principal
if __name__ == "_main_":
    main()