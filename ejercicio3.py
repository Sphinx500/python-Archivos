"""
Escribir un programa que pida los datos de “n” cantidad de alumnos (nombre completo, número de identificación del alumno, carrera y promedio). Se deben  guardar en un archivo estos datos, para que posteriormente se lean a través de una función, la cual creará un archivo con los datos de los alumnos aprobados y otro archivo con los datos de los alumnos reprobados, mostrar el contenido de dichos archivos por pantalla. (El archivo deberá contener los datos separados por “|” o “;”)

"""

n = int(input("Escribe el numero de registros a agregar: "))
archivo = "alumnos.txt"

for i in range(n):
    nombre = input("Escribe el nombre del alumno: ")
    ID = int(input("Escribe el ID del alumno: "))
    carrera = input("Nombre de carrera: ")
    cali = float(input("Escriba la calificacion del alumno: "))

try: 
    f = open(archivo, 'a')
except FileNotFoundError:
    print('¡El fichero ' + archivo + ' no existe!\n')
else:
    f.write(nombre + '|' + str(ID) + '|' + carrera + '|' + str(cali) + '\n')
    f.close()
    print('El contacto se ha añadido.\n')



def calificacion():
    try:
        f = open(archivo, 'r')
    except FileNotFoundError:
        print('El fichero no existe.')
    lineas = f.read()

    if cali >= 8:
        try:
            aprobados = "aprobados.txt"
            a = open(aprobados, 'a')
        except FileNotFoundError:
            print('¡El fichero ' + archivo + ' no existe!\n')
        else:
            a.write(nombre + '|' + str(ID) + '|' + carrera + '|' + str(cali) + '\n')
            a.close()
            print('alumnos aprobados\n')

    else:
        try:
            reprobados = "reprobados.txt"
            b = open(reprobados, 'a')
        except FileNotFoundError:
            print('¡El fichero ' + archivo + ' no existe!\n')
        else:
            b.write(nombre + '|' + str(ID) + '|' + carrera + '|' + str(cali) + '\n')
            b.close()
            print('alumnos reprobados\n')

calificacion()
