import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Datos proporcionados
tiempo = np.array([0, 5, 10, 15, 20, 25, 30])  # Tiempo en minutos
temperatura = np.array([38, 51, 61, 73, 63, 63, 68])  # Temperatura en °C
temperatura_ambiente = np.mean([24.4, 25.0, 24.5, 24.5, 24.5, 24.6, 24.7])  # Temperatura ambiente promedio
titulo = 'Ajuste de la Ley de Enfriamiento de Newton para un Procesador de Computadora'


# Función para el ajuste: Modelo de enfriamiento de Newton
def modelo_enfriamiento(t, T0, k):
    return temperatura_ambiente + (T0 - temperatura_ambiente) * np.exp(-k * t)

# Ajuste de curva
parametros_optimizados, _ = curve_fit(modelo_enfriamiento, tiempo, temperatura, p0=[38, 0.01])

# Resultados del ajuste
T0_ajustado, k_ajustado = parametros_optimizados
print(f"Temperatura inicial ajustada (T0): {T0_ajustado:.2f} °C")
print(f"Constante de enfriamiento ajustada (k): {k_ajustado:.4f} por minuto")

# Gráfica
tiempo_pred = np.linspace(0, 30, 300)
temperatura_pred = modelo_enfriamiento(tiempo_pred, T0_ajustado, k_ajustado)

plt.figure(figsize=(10, 6))
plt.scatter(tiempo, temperatura, color='blue', label='Datos Experimentales')
plt.plot(tiempo_pred, temperatura_pred, color='red', label='Ajuste del Modelo')
plt.title(titulo)
plt.xlabel('Tiempo (minutos)')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid(True)
plt.show()

