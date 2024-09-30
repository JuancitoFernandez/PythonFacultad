import random
from heap import HeapMax 

# Crear una instancia de HeapMax para manejar las misiones
misiones = HeapMax()

# Definir recursos totales
recursos_totales = {
    "Scout Troopers": 0,
    "Stormtroopers": 0,
    "Speeders": 0,
    "AT-AT": 0,
    "AT-RT": 0,
    "AT-TE": 0,
    "AT-DP": 0,
    "AT-ST": 0,
    "AT-M6": 0,
    "AT-MP": 0,
    "AT-DT": 0
}

# Función para añadir una misión
def añadir_mision(tipo_mision, planeta, general):
    # Determinar la prioridad de la misión
    prioridad = 1 if general in ["Palpatine", "Darth Vader"] else 0  # Alta prioridad para Palpatine y Darth Vader
    mision = {
        "tipo": tipo_mision,
        "planeta": planeta,
        "general": general,
        "prioridad": prioridad  # Usar un número para facilitar la comparación
    }
    misiones.add((prioridad, mision))  # Agregar como tupla (prioridad, misión)

# Función para asignar recursos a las misiones
def asignar_recursos():
    while misiones.elements:
        mision_actual = misiones.remove()[1]  # Obtener la misión de la tupla
        recursos = {}

        if mision_actual["prioridad"] == 1:  # Alta prioridad
            recursos = {"Recursos Personalizados": "Asignados según especificaciones de la misión."}
        else:  # Baja prioridad
            if mision_actual["tipo"] == "exploración":
                recursos = {"Scout Troopers": 15, "Speeders": 2}
            elif mision_actual["tipo"] == "contención":
                recursos = {"Stormtroopers": 30}
                # Asignar vehículos aleatorios
                tipos_vehiculos = ["AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST"]
                vehiculos_seleccionados = random.choices(tipos_vehiculos, k=3)
                for vehiculo in vehiculos_seleccionados:
                    recursos[vehiculo] = recursos.get(vehiculo, 0) + 1
            elif mision_actual["tipo"] == "ataque":
                recursos = {"Stormtroopers": 50}
                # Asignar vehículos aleatorios
                tipos_vehiculos = ["AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST", "AT-M6", "AT-MP", "AT-DT"]
                vehiculos_seleccionados = random.choices(tipos_vehiculos, k=7)
                for vehiculo in vehiculos_seleccionados:
                    recursos[vehiculo] = recursos.get(vehiculo, 0) + 1

        # Mostrar recursos asignados
        print(f"Recursos asignados para la misión(Tipo: {mision_actual['tipo']}, Planeta: {mision_actual['planeta']}, General: {mision_actual['general']}, Prioridad: {'Alta' if mision_actual['prioridad'] == 1 else 'Baja'}): {recursos}")

        # Actualizar recursos totales
        for clave, valor in recursos.items():
            if clave in recursos_totales:
                recursos_totales[clave] += valor

# Añadir misiones
añadir_mision("exploración", "Tatooine", "Palpatine")
añadir_mision("contención", "Hoth", "Darth Vader")
añadir_mision("ataque", "Endor", "General Grievous")

# Asignar recursos a las misiones
asignar_recursos()

# Mostrar recursos totales asignados
print("\nRecursos Totales Asignados:")
for recurso, cantidad in recursos_totales.items():
    print(f"{recurso}: {cantidad}")
