import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Nuevos datos proporcionados
tiempo_nuevo = np.array([0, 5, 10, 15, 20, 25, 30])  # Tiempo en minutos
temperatura_nueva = np.array([49, 87, 90, 92, 86, 97, 66])  # Temperatura en °C
temperatura_ambiente_nueva = np.mean([24.4, 25.0, 24.5, 24.5, 24.5, 24.6, 24.7])  # Temperatura ambiente promedio

titulo_nuevo = 'Ajuste de la Ley de Enfriamiento de Newton computadora HP - Pavilion Gaming'


# Función para el ajuste: Modelo de enfriamiento de Newton
def modelo_enfriamiento(t, T0, k):
    return temperatura_ambiente_nueva + (T0 - temperatura_ambiente_nueva) * np.exp(-k * t)

# Ajuste de curva con los nuevos datos
parametros_optimizados_nuevo, _ = curve_fit(modelo_enfriamiento, tiempo_nuevo, temperatura_nueva, p0=[49, 0.01])

# Resultados del ajuste con los nuevos datos
T0_ajustado_nuevo, k_ajustado_nuevo = parametros_optimizados_nuevo
print(f"Temperatura inicial ajustada (T0) con nuevos datos: {T0_ajustado_nuevo:.2f} °C")
print(f"Constante de enfriamiento ajustada (k) con nuevos datos: {k_ajustado_nuevo:.4f} por minuto")

# Gráfica con los nuevos datos
temperatura_pred_nueva = modelo_enfriamiento(tiempo_nuevo, T0_ajustado_nuevo, k_ajustado_nuevo)

plt.figure(figsize=(10, 6))
plt.scatter(tiempo_nuevo, temperatura_nueva, color='blue', label='Datos Experimentales Nuevos')
plt.plot(tiempo_nuevo, temperatura_pred_nueva, color='red', label='Ajuste del Modelo con Nuevos Datos')
plt.title(titulo_nuevo)
plt.xlabel('Tiempo (minutos)')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid(True)
plt.show()