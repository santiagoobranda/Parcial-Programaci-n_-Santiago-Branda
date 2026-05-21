from lista_heroes import lista_heroe


def mostrar_heroe(heroe):
    """
    Brief:
        Muestra en la consola los datos formateados de un heroe accediendo a los indices de su lista.
    Parametros:
        heroe: Sublista con los datos del personaje posicionados por indice (0:Nombre, 1:Identidad, 
                      2:Empresa, 3:Altura, 4:Peso, 5:Genero, 6:Ojos, 7:Pelo, 8:Fuerza, 9:Inteligencia).
    Retorno:
        None
    """
    print(f'Nombre: {heroe[0]}\n'
          f'Identidad: {heroe[1]}\n'
          f'Empresa: {heroe[2]}\n'
          f'Altura: {heroe[3]} cm \n'
          f'Peso: {heroe[4]} Kilos \n'
          f'Género: {heroe[5]}\n'
          f'Ojos: {heroe[6]}\n'
          f'Pelo: {heroe[7]}\n'
          f'Fuerza: {heroe[8]}\n'
          f'Inteligencia: {heroe[9]}\n'
          f'--------------------------'
    )


def ver_heroes(lista_heroe):
    """
    Brief:
        Recorre la lista principal mediante un bucle for e imprime cada heroe usando sus indices.
    Parametros:
        lista_heroe: Lista bidimensional que contiene a todos los heroes guardados.
    Retorno:
        None
    """
    print('-- LISTA DE HEROES --')
    for i in range(len(lista_heroe)):  
        mostrar_heroe(lista_heroe[i])  


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


def ordenar_alfabeticamente(lista_heroe):
    """
    Brief:
        Ordena los heroes alfabeticamente por el nombre (indice 0) aplicando el algoritmo de Burbuja.
        Hace el intercambio de posiciones usando una variable auxiliar.
    Parametros:
        lista_heroe : Lista que se va a ordenar de forma interna.
    Retorno:
        None
    """
    for i in range(len(lista_heroe) - 1): 
        for j in range(len(lista_heroe) - 1 - i): 

            if lista_heroe[j][0].lower() > lista_heroe[j + 1][0].lower(): # Comparo los nombres (posición 0)

            # Intercambio de posiciones
                aux = lista_heroe[j]
                lista_heroe[j] = lista_heroe[j + 1]
                lista_heroe[j + 1] = aux

    print('\nLista ordenada\n')
    ver_heroes(lista_heroe) 


def ver_heroe_alto(lista_heroe):
    """
    Brief:
        Busca el valor maximo en el indice 3 (Altura) recorriendo la lista. Luego, hace otra 
        pasada para imprimir todos los heroes que tengan esa misma altura maxima.
    Parametros:
        lista_heroe : Lista donde se va a buscar el maximo de altura.
    Retorno:
        None
    """
    altura = lista_heroe[0][3]  

    for i in range(len(lista_heroe)): 
        if lista_heroe[i][3] > altura:
            altura = lista_heroe[i][3]

    print('\n -- El/los heroe/s mas alto/s es/son:')
    for i in range(len(lista_heroe)):  
        if lista_heroe[i][3] == altura:
            mostrar_heroe(lista_heroe[i])


def ver_heroe_fuerte(lista_heroe):
    """
    Brief:
        Busca el valor maximo en el indice 8 (Fuerza) recorriendo la lista. Despues, vuelve 
        a recorrer para mostrar todos los personajes que empaten en esa fuerza maxima.
    Parametros:
        lista_heroe: Lista donde se va a buscar el maximo de fuerza.
    Retorno:
        None
    """
    fuerza = lista_heroe[0][8]  

    for i in range(len(lista_heroe)):  
        if lista_heroe[i][8] > fuerza:
            fuerza = lista_heroe[i][8]

    print('\n -- El/los heroe/s mas fuerte/s es/son:')
    for i in range(len(lista_heroe)):  
        if lista_heroe[i][8] == fuerza:
            mostrar_heroe(lista_heroe[i])


def ver_heroe_delgado(lista_heroe):
    """
    Brief:
        Busca el valor minimo en el indice 4 (Peso) mediante un recorrido. Luego, hace un 
        segundo bucle para imprimir los datos de los heroes que tengan ese peso minimo.
    Parametros:
        lista_heroe: Lista donde se va a buscar el minimo de peso.
    Retorno:
        None
    """
    peso = lista_heroe[0][4] 

    for i in range(len(lista_heroe)):  
        if lista_heroe[i][4] < peso:
            peso = lista_heroe[i][4]

    print('\n -- El/los heroe/s mas delgado/s es/son:')
    for i in range(len(lista_heroe)): 
        if lista_heroe[i][4] == peso:
            mostrar_heroe(lista_heroe[i])


def menu():
    """
    Brief:
        Muestra un menu interactivo en la consola usando un bucle while controlado por una bandera. 
        Segun la opcion ingresada, llama a la funcion correspondiente pasandole la lista.
    Parametros:
        None
    Retorno:
        None
    """
    bandera = True  

    while bandera:

        print('''
MENU DE HEROES

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
            ver_heroes(lista_heroe)

        elif opcion == '2':
            agregar_heroe(lista_heroe)

        elif opcion == '3':
            eliminar_heroe(lista_heroe)

        elif opcion == '4':
            ordenar_alfabeticamente(lista_heroe)

        elif opcion == '5':
            ver_heroe_alto(lista_heroe)

        elif opcion == '6':
            ver_heroe_fuerte(lista_heroe)

        elif opcion == '7':
            ver_heroe_delgado(lista_heroe)

        elif opcion == '0':
            bandera = False  
            print('Saliendo del menu')

        else:
            print('Opcion no valida')


menu()  