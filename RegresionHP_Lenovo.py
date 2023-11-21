import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Tercer conjunto de datos proporcionados
tiempo_tercero = np.array([0, 5, 10, 15, 20, 25, 30])  # Tiempo en minutos
temperatura_tercera = np.array([47, 73, 80, 82, 83, 70, 82])  # Temperatura en °C
temperatura_ambiente_tercera = np.mean([24.4, 25.0, 24.5, 24.5, 24.5, 24.6, 24.7])  # Temperatura ambiente promedio

titulo_tercero = 'Ajuste de la Ley de Enfriamiento de Newton computadora Lenovo - Legion'


# Función para el ajuste: Modelo de enfriamiento de Newton
def modelo_enfriamiento(t, T0, k):
    return temperatura_ambiente_tercera + (T0 - temperatura_ambiente_tercera) * np.exp(-k * t)

# Ajuste de curva con el tercer conjunto de datos
parametros_optimizados_tercero, _ = curve_fit(modelo_enfriamiento, tiempo_tercero, temperatura_tercera, p0=[47, 0.01])

# Resultados del ajuste con el tercer conjunto de datos
T0_ajustado_tercero, k_ajustado_tercero = parametros_optimizados_tercero
print(f"Temperatura inicial ajustada (T0) con tercer conjunto de datos: {T0_ajustado_tercero:.2f} °C")
print(f"Constante de enfriamiento ajustada (k) con tercer conjunto de datos: {k_ajustado_tercero:.4f} por minuto")

# Gráfica con el tercer conjunto de datos
temperatura_pred_tercera = modelo_enfriamiento(tiempo_tercero, T0_ajustado_tercero, k_ajustado_tercero)

plt.figure(figsize=(10, 6))
plt.scatter(tiempo_tercero, temperatura_tercera, color='blue', label='Datos Experimentales del Tercer Conjunto')
plt.plot(tiempo_tercero, temperatura_pred_tercera, color='red', label='Ajuste del Modelo con Tercer Conjunto de Datos')
plt.title(titulo_tercero)
plt.xlabel('Tiempo (minutos)')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid(True)
plt.show()
