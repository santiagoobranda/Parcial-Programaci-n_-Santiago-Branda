from muestreo import *


def agregar_elemento(lista, elemento):
    """
    Brief:
        Agrega un elemento al final de la lista utilizando el metodo append.
    Parametros:
        lista : La lista en la que se va a guardar el dato.
        elemento (any): El dato o la sublista que se quiere agregar.
    Retorno:
        None
    """
    lista.append(elemento)  


def agregar_heroe(lista_heroe):
    """
    Brief:
        Pide los datos de un nuevo heroe por consola, los valida uno por uno con bucles while 
        y, si esta todo bien, arma una sublista y la agrega a la lista principal.
    Parametros:
        lista_heroe : Lista principal donde se va a guardar el nuevo heroe creado.
    Retorno:
        None
    """
    nombre = input('ingrese nombre del heroe: ') 
    while nombre == '':
        print('ERROR. Nombre vacio')
        nombre = input('Ingrese nombre: ')
        
    identidad = input('ingrese identidad: ') 
    while nombre == '':
        print('ERROR. Nombre vacio')
        identidad = input('Ingrese identidad: ')
         
    empresa = input('ingrese empresa (DC Comics / Marvel Comics): ')
    while empresa.lower() != 'dc comics' and empresa.lower() != 'marvel comics': 
        print('ERROR. Empresa invalida')
        empresa = input('ingrese empresa (DC Comics o Marvel Comics): ')

    altura = float(input('ingrese altura (mayor a 0): '))
    while altura <= 0:  
        print('ERROR. Altura invalida, debe ser mayor a 0')
        altura = float(input('ingrese altura (mayor a 0): '))

    peso = int(input('ingrese peso (mayor a 0): '))
    while peso <= 0:  
        print('ERROR. Peso invalido, debe ser mayor a 0')
        peso = int(input('ingrese peso (mayor a 0): '))

    genero = input('ingrese genero (M/F/NB): ')
    while genero.lower() != 'm' and genero.lower() != 'f' and genero.lower() != 'nb':  
        print('ERROR. Genero invalido, debe ser M, F o NB')
        genero = input('ingrese genero (M/F/NB): ')

    color_ojos = input('Ingrese color de ojos: ')  
    color_pelo = input('Ingrese color de pelo: ')  

    fuerza = int(input('Ingrese fuerza: '))
    while fuerza <= 0:  
        print('ERROR. Fuerza invalida, debe ser mayor a 0')
        fuerza = int(input('Ingrese fuerza: '))

    inteligencia = input('ingrese nivel de inteligencia (low, average, good, high, genius): ')
    
    while (inteligencia.lower() != 'low' and 
           inteligencia.lower() != 'average' and 
           inteligencia.lower() != 'good' and 
           inteligencia.lower() != 'high' and 
           inteligencia.lower() != 'genius'):  
        print('ERROR. Nivel de inteligencia invalida')
        inteligencia = input('ingrese nivel de inteligencia (low, average, good, high, genius): ')

    heroe = [nombre, identidad, empresa, altura, peso, genero, color_ojos, color_pelo, fuerza, inteligencia]  
    agregar_elemento(lista_heroe, heroe)  
    print('Heroe agregado correctamente')
    ver_heroes(lista_heroe)  


def eliminar_heroe(lista_heroe):
    """
    Brief:
        Busca un heroe por su nombre (indice 0). Si lo encuentra, muestra sus datos, 
        lo borra usando pop con su indice y rompe el bucle for con un break.
    Parametros:
        lista_heroe : Lista de la cual se va a eliminar el heroe si coincide el nombre.
    Retorno:
        None
    """
    nombre = input('\n -- Ingrese el nombre del heroe a borrar: \n').lower() 

    encontrado = False  # Bandera de control

    for i in range(len(lista_heroe)):  
        if lista_heroe[i][0].lower() == nombre:  
            mostrar_heroe(lista_heroe[i])  
            lista_heroe.pop(i)  
            print('Heroe eliminado')
            encontrado = True
            break  

    if encontrado == False:  
        print('Heroe no encontrado')
