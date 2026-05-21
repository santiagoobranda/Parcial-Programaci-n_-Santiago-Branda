from heroes import lista_heroes

from muestreo import *

from modificar_listas import *

from ordenar_listas import *



def menu():
    """
    Brief:
        Muestra un menu en la consola usando un bucle while controlado por una bandera. 
        Segun la opcion ingresada, llama a la funcion correspondiente pasandole la lista.
    Parametros:
        None
    Retorno:
        None
    """
    bandera = True  

    while bandera:

        print('''
MENU DE OPCIONES

1 - Ver todos los Heroes
2 - Agregar Heroe
3 - Eliminar Heroe
4 - Ordenar alfabéticamente
5 - Ver Heroe mas alto
6 - Ver Heroe más fuerte
7 - Ver heroe mas delgado
0 - Salir
''')

        opcion = input('Ingrese una opción: ')

        if opcion == '1':
            ver_heroes(lista_heroes)

        elif opcion == '2':
            agregar_heroe(lista_heroes)

        elif opcion == '3':
            eliminar_heroe(lista_heroes)

        elif opcion == '4':
            ordenar_alfabeticamente(lista_heroes)

        elif opcion == '5':
            ver_condicion(lista_heroes, 3, '\n -- El/los heroe/s mas alto/s es/son:', 'max')

        elif opcion == '6':
            ver_condicion(lista_heroes, 8, '\n -- El/los heroe/s mas fuerte/s es/son:', 'max')

        elif opcion == '7':
            ver_condicion(lista_heroes, 4, '\n -- El/los heroe/s mas delgado/s es/son:', 'min')

        elif opcion == '0':
            bandera = False  
            print('Saliendo del menu')

        else:
            print('Opcion no valida')


menu()  