import subprocess
import time


def ejecutar_sincrono():
    print("Ejecutando Notepad de forma síncrona (bloqueante)...")
    inicio = time.time()
    proceso = subprocess.Popen(["notepad.exe"])
    tiempo_apertura = time.time() - inicio
    print(f"Tiempo de apertura de Notepad (síncrono): {tiempo_apertura:.2f} segundos")

    # Esperar a que el proceso termine
    proceso.wait()


def ejecutar_asincrono():
    print("Ejecutando Notepad de forma asíncrona (no bloqueante)...")
    inicio = time.time()
    proceso = subprocess.Popen(["notepad.exe"])  # No espera a que el Bloc de notas se cierre
    tiempo_apertura = time.time() - inicio
    print(f"Tiempo de apertura de Notepad (asíncrono): {tiempo_apertura:.2f} segundos")
    proceso.terminate()


# Bloque principal para ejecutar las funciones
if __name__ == '__main__':
    print("Opciones disponibles:")
    print("1 - Ejecutar Notepad de forma síncrona")
    print("2 - Ejecutar Notepad de forma asíncrona")

    opcion = input("Seleccione una opción (1 o 2): ")
    if opcion == '1':
        ejecutar_sincrono()
    elif opcion == '2':
        proceso = ejecutar_asincrono()
    else:
        print("Opción no válida.")
