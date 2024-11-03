from HeapMax import HeapMax, Pedido

# Inicialización de la cola de prioridad y la bitácora
cola_prioridad = HeapMax() 
bitacora = []  

# Agregar algunos pedidos
pedidos = [
    Pedido("Gran Inquisidor", "Lothal", "Necesito ayuda con Hera Syndulla."),
    Pedido("Agente Kallus", "Imperial", "Requiere apoyo para el Destructor Estelar."),
    Pedido("General Veers", "Hoth", "Solicito refuerzos para la batalla."),
    Pedido("General Tarkin", "Alderaan", "Necesito información sobre los rebeldes.")
]

# Determinar la prioridad y agregar a la cola
for pedido in pedidos:
    if (pedido.general == "Gran Inquisidor" or
        pedido.planeta == "Lothal" or
        "Hera Syndulla" in pedido.descripcion):
        prioridad = 3  # Alta prioridad
    elif (pedido.general == "Agente Kallus" or
          "Destructor Estelar" in pedido.descripcion or
          "AT-AT" in pedido.descripcion):
        prioridad = 2  # Media prioridad
    else:
        prioridad = 1  # Baja prioridad

    cola_prioridad.arrive(pedido, prioridad)

# Atender los pedidos
print("Atendiendo pedidos:")
for _ in range(len(pedidos)):
    pedido_atendido = cola_prioridad.atention()
    if pedido_atendido:
        bitacora.append(pedido_atendido[1])  # Almacenar solo el pedido en la bitácora
        print(f"Pedido atendido: {pedido_atendido[1]}")
    else:
        print("No hay más pedidos para atender.")

# Mostrar la bitácora
print("Bitácora de pedidos atendidos:")
for pedido in bitacora:
    print(pedido)