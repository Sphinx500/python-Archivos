"""
Crear un programa que hará uso del archivo creado en el ejercicio 2, el cual debe tener las opciones de agregar, eliminar o mostrar la información de una persona, si no existe el nombre dentro del archivo, mostrar un mensaje que indique que los datos de la persona no están registrados dentro del archivo.

"""

class Datos():

    def agregaDatos(self):
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

    def mostrarDatos(self):
        archivo = "datos-personas.txt"
        persona = input("nombre de la persona a buscar: ")
        with open(archivo) as f:
            datafile = f.readlines()
        for line in datafile:
            if persona in line:
                return line
        return "No se encuentra"
                
    


misDatos = Datos()

while True:
    try:
        op=int(input("Elija la operacion a realizar: "))
        print("-------------------")
        print("1.Añadir Datos")
        print("2.Buscar Datos")
        print("3.Salir")
        print("-------------------")

        if op == 1:
            misDatos.agregaDatos()
        elif op == 2:
            print(misDatos.mostrarDatos())
        elif op == 3:
            break
        else:
            print("Por favor elige una opcion")
            op=int(input("Elija la operacion a realizar: "))

    except ValueError:
        print("Solo se aceptan numeros del 1 al 4")



#misDatos.agregaDatos()

#print(misDatos.mostrarDatos())

#misDatos.eliminarDatos()