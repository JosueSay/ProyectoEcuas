import time

def carga_cpu(tiempo_segundos):
    tiempo_inicio = time.time()
    contador = 0

    while time.time() - tiempo_inicio < tiempo_segundos:
        # Realiza operaciones poco complejas para mantener activa la CPU
        contador += 1
        if contador == 1**10:
            print("\tRestaure el contador...")
            contador = 0

# Establecer el tiempo de ejecución en segundos
tiempo_total_segundos = 30 * 60

print("Inicio - 0 minutos")
# Ejecutar la carga de la CPU
carga_cpu(tiempo_total_segundos)
print("Finalizado - 30 minutos")