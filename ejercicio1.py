
def pidenumero(numero,archivo):
    with open(archivo, 'w') as a:
        for i in range(1, 11):
            a.write(str(numero) + ' x ' + str(i) + ' = ' + str(numero * i) + '\n')

def imprimir(archivo,numero):
    try: 
        f = open(archivo, 'r')
    except FileNotFoundError:
        print('No existe el fichero con la tabla del', numero)
    else:
        print(f.read())
        f.close()

numero = int(input("Introduce un numero entero del 1 al 10: "))
archivo = 'tabla-' + str(numero) + '.txt'

pidenumero(numero,archivo)
imprimir(archivo,numero)
