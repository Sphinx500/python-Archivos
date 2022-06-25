"""
Escribir un programa que pida los datos nombre, edad, correo y teléfono de una persona, y estos datos se deberán guardar en un archivo (datos-personas.txt). Cada vez que se ejecute el programa se deberá agregar los datos de una nueva persona a dicho archivo. (El archivo deberá contener los datos separados por “|” o “;”)

"""

def obtener_datos():
    nombre = input("Ingresa un nombre: ")
    edad = int(input("Ingresa la edad: "))
    correo = input("ingresa el correo: ")
    telefono = int(input("Ingresa un numero de telefono: "))
    archivo = "datos-personas.txt"
    try: 
        f = open(archivo, 'a')
    except FileNotFoundError:
        return('¡El fichero ' + archivo + ' no existe!\n')
    else:
        f.write(nombre + '|' + str(edad) + '|' + correo + '|' + str(telefono) + '\n')
        f.close()
        return('El contacto se ha añadido.\n')

obtener_datos()

