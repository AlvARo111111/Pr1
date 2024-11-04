import psutil

def listar_procesos(nombres_procesos):
    print(f"{'Proceso':<30}{'PID':<10}{'Memoria (MB)':<15}")
    print("-" * 55)
    for proceso in psutil.process_iter(['name', 'pid', 'memory_info']):
        try:
            nombre = proceso.info['name']
            pid = proceso.info['pid']
            memoria = proceso.info['memory_info'].rss / (1024 * 1024)  # Memoria en MB
            # Comprobar si el nombre introducido existe como un proceso
            if any(n in nombre.lower() for n in nombres_procesos):
                print(f"{nombre:<30}{pid:<10}{memoria:<15.2f}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            print(f"Acceso denegado o proceso inexistente para PID {proceso.info['pid']}.")


def finalizar_proceso(nombre_proceso):
    for proceso in psutil.process_iter(['name', 'pid']):
        try:
            if proceso.info['name'] and nombre_proceso.lower() in proceso.info['name'].lower():
                proceso.terminate()  # finalizar el proceso si se puede
                proceso.wait()  # esperar a que finalice
                print(f"Proceso '{nombre_proceso}' con PID {proceso.info['pid']} finalizado.")
                return
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            print(f"No se pudo finalizar el proceso '{nombre_proceso}'.")
    print(f"No se encontro un proceso con el nombre '{nombre_proceso}'.")


nombres_procesos = input("Ingrese nombres de procesos separados por coma: ").lower().split(",")
listar_procesos(nombres_procesos)

nombre_proceso = input("Ingrese el nombre del proceso a finalizar: ")
finalizar_proceso(nombre_proceso)