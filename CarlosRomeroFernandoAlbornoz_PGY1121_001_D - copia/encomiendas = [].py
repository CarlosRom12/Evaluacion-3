encomiendas = []

def grabar_encomienda():
    """Función para grabar una nueva encomienda"""
    nombre = input("Ingrese el nombre del destinatario: ")
    direccion = input("Ingrese la dirección de entrega: ")
    descripcion = input("Ingrese una descripción de la encomienda: ")
    peso = float(input("Ingrese el peso de la encomienda (en kg): "))
    valor = float(input("Ingrese el valor de la encomienda: "))
    
    if peso < 0.1 or valor < 2000:
        print("La encomienda no cumple con los requisitos mínimos.")
        return
    
    encomienda = {
        'nombre': nombre,
        'direccion': direccion,
        'descripcion': descripcion,
        'peso': peso,
        'valor': valor
    }
    
    encomiendas.append(encomienda)
    print("Encomienda grabada con éxito.")

def buscar_encomienda():
    """Función para buscar una encomienda por nombre de destinatario"""
    nombre = input("Ingrese el nombre del destinatario a buscar: ")
    
    for encomienda in encomiendas:
        if encomienda['nombre'] == nombre:
            print("Encomienda encontrada:")
            print(f"Nombre: {encomienda['nombre']}")
            print(f"Dirección: {encomienda['direccion']}")
            print(f"Descripción: {encomienda['descripcion']}")
            print(f"Peso: {encomienda['peso']} kg")
            print(f"Valor: ${encomienda['valor']}")
            return
    
    print("Encomienda no encontrada.")

def listar_encomiendas():
    """Función para listar todas las encomiendas"""
    if not encomiendas:
        print("No hay encomiendas registradas.")
        return
    
    print("Lista de encomiendas:")
    for encomienda in encomiendas:
        print(f"Nombre: {encomienda['nombre']}")
        print(f"Dirección: {encomienda['direccion']}")
        print(f"Descripción: {encomienda['descripcion']}")
        print(f"Peso: {encomienda['peso']} kg")
        print(f"Valor: ${encomienda['valor']}")
        print("--------------")

def menu():
    while True:
        print("** Menú de Encomiendas **")
        print("1. Grabar encomienda")
        print("2. Buscar encomienda")
        print("3. Listar encomiendas")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            grabar_encomienda()
        elif opcion == '2':
            buscar_encomienda()
        elif opcion == '3':
            listar_encomiendas()
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu()