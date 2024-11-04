from multiprocessing import Process, Pipe

def proceso_hijo(conn):
    # el hijo recibe el mensaje y lo modifica
    mensaje = conn.recv()
    conn.send(mensaje.upper())
    conn.close()

def enviar_mensaje():
    #Crear el pipe y el proceso hijo
    padre_conn, hijo_conn = Pipe()
    proceso = Process(target=proceso_hijo, args=(hijo_conn,))
    proceso.start()

    # Enviar un mensaje desde el padre
    mensaje = input("Ingresa un mensaje para el proceso hijo: ")
    padre_conn.send(mensaje)

    # Recibir el mensaje modificado del proceso hijo
    mensaje_modificado = padre_conn.recv()
    print("Mensaje del hijo:", mensaje_modificado)

    # Esperar a que el proceso hijo termine
    proceso.join()

def contar_lineas_palabras(conn):
     # Proceso hijo para 2.2: recibe el contenido del archivo y cuenta líneas y palabras
    contenido = conn.recv()
    lineas = contenido.count('\n')
    palabras = len(contenido.split())
    conn.send((lineas, palabras))
    conn.close()

def envio_archivo():
    padre_conn, hijo_conn = Pipe()
    proceso = Process(target=contar_lineas_palabras, args=(hijo_conn,))
    proceso.start()

    # leer el contenido del archivo y enviar al hijo
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
            padre_conn.send(contenido)

        # Recibir el conteo de líneas y palabras del proceso hijo
        lineas, palabras = padre_conn.recv()
        print(f"Líneas: {lineas}, Palabras: {palabras}")

    except FileNotFoundError:
        print("Archivo no encontrado. Asegúrate de que el archivo existe y está en la misma carpeta.")

    # Esperar a que el proceso hijo termine
    proceso.join()


if __name__ == '__main__':
    print("Opciones disponibles:")
    print("1 - Enviar mensaje")
    print("2 - Enviar archivo")

    opcion = input("Seleccione una opción (1 o 2): ")
    if opcion == '1':
        enviar_mensaje()
    elif opcion == '2':
        envio_archivo()
    else:
        print("Opción no válida.")
