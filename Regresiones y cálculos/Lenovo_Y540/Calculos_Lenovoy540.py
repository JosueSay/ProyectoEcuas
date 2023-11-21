import numpy as np

def calcular_constante_enfriamiento(temperatura_t, tiempo_t, temperatura_ambiente, temperatura_inicial):
    """
    Calcula la constante de enfriamiento (k) para diferentes valores de T(t) y t.
    
    Args:
    temperatura_t (array-like): Temperatura en un momento dado (T(t)).
    tiempo_t (array-like): Tiempo correspondiente a las temperaturas (t).
    temperatura_ambiente (float): Temperatura ambiente (T_m).
    temperatura_inicial (float): Temperatura inicial (T_0).
    
    Returns:
    array-like: Valores de la constante de enfriamiento (k) calculados para cada par (T(t), t).
    """
    k_values = []
    for T, t in zip(temperatura_t, tiempo_t):
        if T == temperatura_ambiente:
            k_values.append(0.0)  # Evita divisiones por cero si T(t) es igual a T_m
        else:
            k = -1 / t * np.log((T - temperatura_ambiente) / (temperatura_inicial - temperatura_ambiente))
            k_values.append(k)
    return k_values

# Datos del escenario sin sistema de enfriamiento
tiempo_sin_enfriamiento = np.array([0, 5, 10, 15, 20, 25])  # Tiempo en minutos
temperatura_sin_enfriamiento = np.array([47, 73, 80, 82, 83, 70])  # Temperatura del procesador en °C
temperatura_ambiente_sin_enfriamiento = 24.6  # Temperatura ambiente promedio en °C

# Datos del escenario con sistema de enfriamiento
tiempo_con_enfriamiento = np.array([0, 5, 10, 15, 20, 25])  # Tiempo en minutos
temperatura_con_enfriamiento = np.array([45, 74, 70, 76, 85, 81])  # Temperatura del procesador en °C
temperatura_ambiente_con_enfriamiento = 25.2  # Temperatura ambiente promedio en °C

# Calcular k para el escenario sin sistema de enfriamiento
k_sin_enfriamiento = calcular_constante_enfriamiento(
    temperatura_sin_enfriamiento,
    tiempo_sin_enfriamiento,
    temperatura_ambiente_sin_enfriamiento,
    temperatura_sin_enfriamiento[0]  # Usamos la primera temperatura como T_0
)

# Calcular k para el escenario con sistema de enfriamiento
k_con_enfriamiento = calcular_constante_enfriamiento(
    temperatura_con_enfriamiento,
    tiempo_con_enfriamiento,
    temperatura_ambiente_con_enfriamiento,
    temperatura_con_enfriamiento[0]  # Usamos la primera temperatura como T_0
)

# Imprimir resultados
print("Valores de k para el escenario sin sistema de enfriamiento:")
print(k_sin_enfriamiento)

print("\nValores de k para el escenario con sistema de enfriamiento:")
print(k_con_enfriamiento)


