# base_de_datos.json
import json
# lista_estudiantes = []

try:
    with open("base_de_datos.json", "r") as archivo_db:
        print("Leyendo base de datos...")
        lista_estudiantes = json.load(archivo_db)
        print("Base de datos cargada exitosamente")
except:
    print("Creando nueva base de datos...")
    lista_estudiantes = [estudiante]
    

def calcular_promedio(lista_notas_estudiante):
    total_suma = 0
    # sumar todas las notas
    for nota in lista_notas_estudiante:
        total_suma = total_suma + nota
    # obtener cantidad de notas
    cantidad_notas = len(lista_notas_estudiante)
    # calcular promedio
    promedio = total_suma / cantidad_notas,
    # retornar el promedio
    return promedio

def calcular_cursos(lista_cursos_estudiante):
    tot_cursos = 0

    for curso in lista_cursos_estudiante:
        tot_cursos = tot_cursos + 1
    # obtener cantidad de cursos

    return tot_cursos

def calculo_cursos_aprobados(lista_cursosaprobados):
    tot_cursos_aprobados = 0

    for curso_apro in lista_cursosaprobados:
        if curso_apro >= 61:
            tot_cursos_aprobados = tot_cursos_aprobados + 1

    return tot_cursos_aprobados




def ingresar_nuevo_estudiante():
    # pedir datos de estudiante
    nombre = input("Ingrese nombre: ")
    carnet = input("Ingrese carnet: ")
    # agregar notas
    lista_notas = []
    lista_cursos = []
    lista_cursos_aprobados = []
    opcion_notas = input("Desea ingresar una nota? (y / n): ")
    while opcion_notas == 'y' or opcion_notas == 'Y':
        nueva_nota = input("Ingrese la nota: ")
        # convertir en entero
        nueva_nota = int(nueva_nota)
        lista_notas.append(nueva_nota)
        opcion_notas = input("Desea ingresar otra nota? (y / n): ")
        nuevo_curso = int(nueva_nota)
        lista_cursos.append(nueva_nota)
        nuevo_curso_aprobado = int(nueva_nota)
        lista_cursos_aprobados.append(nueva_nota)
    
    # llamar al calculo de promedio
    promedio_estudiante = calcular_promedio(lista_notas)
    cursos_asignados = calcular_cursos(lista_cursos)
    cursos_aprobados = calculo_cursos_aprobados(lista_cursos_aprobados)
    # crear al nuevo estudiante
    estudiante = {
        'nombre': nombre,
        'carnet': carnet,
        'notas': lista_notas,
        'promedio': promedio_estudiante,
        'Cursos asignados': cursos_asignados,
        'Cursos aprobados': cursos_aprobados
        
    }

    # agregar el nuevo estudiante a la lista
    lista_estudiantes.append(estudiante)
    return


def mostrar_lista_estudiantes():
    print(lista_estudiantes)
    return

def mostrar_cantidad_estudiantes():
    cantidad = len(lista_estudiantes)
    print(f'Hay {cantidad} cantidad de estudiantes')
    return

def mostrar_menu():
    mensaje_menu = """Ingrese la opcion deseada\n

    1. Ingresar un nuevo estudiante\n
    2. Ver lista de estudiantes\n
    3. Mostrar cantidad de estudiantes\n
    4. Buscar estudiante\n
    0. Salir\n
    > 
    """
    opcion = input(mensaje_menu)
    opcion = int(opcion)
    if opcion == 1:
        # ingresar un nuevo estudiante
        ingresar_nuevo_estudiante()
    if opcion == 2:
        # mostrar lista estudiantes
        mostrar_lista_estudiantes()
    if opcion == 3:
        # mostrar cantidad de estudiante
        mostrar_cantidad_estudiantes()
    if opcion == 4:
        # mostrar cantidad de estudiante
        buscar_estudiantes()
     


    if opcion == 0:
        # salir
        with open("base_de_datos.json", "w") as archivo_db:
            print("Guardando base de datos...")
            json.dump(lista_estudiantes, archivo_db)
        return
    mostrar_menu()
    return


mostrar_menu()
