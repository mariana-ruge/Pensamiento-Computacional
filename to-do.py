#importar date time, para comprender la fecha de agendamiento de la tarea
import datetime
import os
os.system('cls')

#Crear una lista para tareas
tareas = []

#Función para crear la nueva tarea
def nueva_tarea():
    nombre_tarea = input("Ingresa el nombre de la tarea")
    #La tarea se almacenará en un diccionario
    tarea = {"nombre": nombre_tarea, "completada": False, "Fecha": datetime.datetime.now().isoformat()}
    #Añadir la tarea (diccionario a la lista de  tareas)
    tareas.append(tarea)
    print("Tarea registrada correctamente")

#Función para ver las tareas
def ver_tarea():
    print("\n Lista de tareas")
    #Declaramos un ciclo for para recorrer la lista de tareas
    for i, tarea in enumerate(tareas, start=1):
        #Verificar el estado de cada tarea con un condicional
        estado = "Completada" if tarea["completada"] else "Pendiente"
        #Imprimir los datos de cada tarea
        print(f"{i}.{tarea['nombre']}({estado})")

#Función para marcar las tareas como completadas
def tarea_completada():
    #Imprime la lista de tareas
    ver_tarea()
    #Evitamos un error donde no exista la tarea
    try:
        #Marcamos la tarea como completada
        indice = int(input("Ingrese el número de la tarea completada: ")) - 1
        tareas[indice]["completada"] = True
        print("Tarea completada exitosamente")
    #Captar un erro de valor inválido o de índice no encontrado
    except (ValueError, IndexError):
        print("Tarea no encontrada")

def eliminar_tarea():
    #Imprimir la lista de tareas
    ver_tarea()
    #Evaluar si la tarea existe en la lista de tareas
    try:
        #Busar la tarea en la lista de tarea y eliminarla
        indice = int(indice("Ingrese el número de la tarea a eliminar: "))
        eliminar = tareas.pop(indice)
        print(f"La tarea '{eliminar['nombre']}' se ha eliminado exitosamente")
    except (ValueError, ImportError):
        print("Número de tarea no válido")

#Ciclo para generar un menú para el programa, mientras sea true, mostrará el menú
while True:
    print("Bienvenido al sistema de gestión de tareas")
    print("\nMenu Principal")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir del sistema")

    #Pedirle las opciones al usuario
    opcion = int(input("Escriba la opción deseada: "))

    #Evaluar las opciones en el sistema.
    if opcion == 1:
        nueva_tarea()
    elif opcion == 2:
        ver_tarea()
    elif opcion == 3:
        tarea_completada()
    elif opcion == 4:
        eliminar_tarea()
    elif opcion == 5:
        print("Saliendo...")
        break
    else:
        print("Opcion inválida")
