import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit  # Importa curve_fit desde scipy.optimize

# Datos del escenario sin sistema de enfriamiento
tiempo_sin_enfriamiento = np.array([0, 5, 10, 15, 20, 25])  # Tiempo en minutos
temperatura_sin_enfriamiento = np.array([38, 51, 61, 73, 63, 63])  # Temperatura del procesador en °C
temperatura_ambiente_sin_enfriamiento = 24.6  # Temperatura ambiente promedio en °C

# Modelo de enfriamiento de Newton
def modelo_enfriamiento(t, T0, k):
    return temperatura_ambiente_sin_enfriamiento + (T0 - temperatura_ambiente_sin_enfriamiento) * np.exp(-k * t)

# Ajuste de curva
parametros_optimizados, _ = curve_fit(modelo_enfriamiento, tiempo_sin_enfriamiento, temperatura_sin_enfriamiento, p0=[temperatura_sin_enfriamiento[0], 0.01])

# Resultados del ajuste
T0_sin_enfriamiento, k_sin_enfriamiento = parametros_optimizados
print(f"Temperatura inicial ajustada (T0): {T0_sin_enfriamiento:.2f} °C")
print(f"Constante de enfriamiento ajustada (k): {k_sin_enfriamiento:.4f} por minuto")

# Gráfica
tiempo_pred_sin_enfriamiento = np.linspace(0, 25, 300)
temperatura_pred_sin_enfriamiento = modelo_enfriamiento(tiempo_pred_sin_enfriamiento, T0_sin_enfriamiento, k_sin_enfriamiento)

plt.figure(figsize=(10, 6))
plt.scatter(tiempo_sin_enfriamiento, temperatura_sin_enfriamiento, color='blue', label='Datos Experimentales')
plt.plot(tiempo_pred_sin_enfriamiento, temperatura_pred_sin_enfriamiento, color='red', label='Ajuste del Modelo')
plt.title('Ajuste de la Ley de Enfriamiento de Newton (Sin Sistema de Enfriamiento) Lenovo Y540')
plt.xlabel('Tiempo (minutos)')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid(True)
plt.show()

# Datos del escenario con sistema de enfriamiento
tiempo_con_enfriamiento = np.array([0, 5, 10, 15, 20, 25])  # Tiempo en minutos
temperatura_con_enfriamiento = np.array([37, 52, 55, 70, 60, 60])  # Temperatura del procesador en °C
temperatura_ambiente_con_enfriamiento = 26.2  # Temperatura ambiente promedio en °C

# Ajuste de curva para el escenario con sistema de enfriamiento
parametros_optimizados_con_enfriamiento, _ = curve_fit(modelo_enfriamiento, tiempo_con_enfriamiento, temperatura_con_enfriamiento, p0=[temperatura_con_enfriamiento[0], 0.01])

# Resultados del ajuste para el escenario con sistema de enfriamiento
T0_con_enfriamiento, k_con_enfriamiento = parametros_optimizados_con_enfriamiento
print(f"Temperatura inicial ajustada (T0): {T0_con_enfriamiento:.2f} °C")
print(f"Constante de enfriamiento ajustada (k): {k_con_enfriamiento:.4f} por minuto")

# Gráfica para el escenario con sistema de enfriamiento
tiempo_pred_con_enfriamiento = np.linspace(0, 25, 300)
temperatura_pred_con_enfriamiento = modelo_enfriamiento(tiempo_pred_con_enfriamiento, T0_con_enfriamiento, k_con_enfriamiento)

plt.figure(figsize=(10, 6))
plt.scatter(tiempo_con_enfriamiento, temperatura_con_enfriamiento, color='blue', label='Datos Experimentales')
plt.plot(tiempo_pred_con_enfriamiento, temperatura_pred_con_enfriamiento, color='red', label='Ajuste del Modelo')
plt.title('Ajuste de la Ley de Enfriamiento de Newton (Con Sistema de Enfriamiento) Lenovo Y540')
plt.xlabel('Tiempo (minutos)')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid(True)
plt.show()


