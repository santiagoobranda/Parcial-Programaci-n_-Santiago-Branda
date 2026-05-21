from lista_heroes import lista_heroe


def mostrar_heroe(heroe):  # Muestra todos los datos de un héroe usando sus índices
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


def ver_heroes(lista_heroe):  # Recorre la lista y muestra todos los héroes
    print('-- LISTA DE HEROES --')
    for i in range(len(lista_heroe)):  # Iteracion usando índice
        mostrar_heroe(lista_heroe[i])  # Muestro cada héroe


def agregar_elemento(lista, elemento):  # Función genérica
    lista.append(elemento)  


def agregar_heroe(lista_heroe):  # Agrega un nuevo héroe con validaciones

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
    while peso <= 0:  # Valido peso positivo
        print('ERROR. Peso invalido, debe ser mayor a 0')
        peso = int(input('ingrese peso (mayor a 0): '))

    genero = input('ingrese genero (M/F/NB): ')
    while genero.lower() != 'm' and genero.lower() != 'f' and genero.lower() != 'nb':  
        print('ERROR. Genero invalido, debe ser M, F o NB')
        genero = input('ingrese genero (M/F/NB): ')

    color_ojos = input('Ingrese color de ojos: ')  
    color_pelo = input('Ingrese color de pelo: ')  

    fuerza = int(input('Ingrese fuerza: '))
    while fuerza <= 0:  # Valido fuerza positiva
        print('ERROR. Fuerza invalida, debe ser mayor a 0')
        fuerza = int(input('Ingrese fuerza: '))

    inteligencia = input('ingrese nivel de inteligencia (low, average, good, high, genius): ')
    while inteligencia.lower() not in ['low', 'average', 'good', 'high', 'genius']:  
        print('ERROR. Nivel de inteligencia invalida')
        inteligencia = input('ingrese nivel de inteligencia (low, average, good, high, genius): ')


    heroe = [nombre, identidad, empresa, altura, peso, genero, color_ojos, color_pelo, fuerza, inteligencia]  # Creo estructura
    agregar_elemento(lista_heroe, heroe)  # Agrego a la lista
    print('Heroe agregado correctamente')
    ver_heroes(lista_heroe)  # Muestro lista actualizada


def eliminar_heroe(lista_heroe):  # Elimina un héroe por nombre
    nombre = input('\n -- Ingrese el nombre del heroe a borrar: \n').lower() 

    encontrado = False  # Bandera de control

    for i in range(len(lista_heroe)):  # Recorro la lista
        if lista_heroe[i][0].lower() == nombre:  # Comparo nombres
            mostrar_heroe(lista_heroe[i])  # Muestro el heroe antes de borrar
            lista_heroe.pop(i)  # Elimino por índice
            print('Heroe eliminado')
            encontrado = True
            break  # Corto el bucle

    if encontrado == False:  
        print('Heroe no encontrado')


def ordenar_alfabeticamente(lista_heroe): # Ordena la lista por nombre (índice 0)

    for i in range(len(lista_heroe) - 1): # Primer recorrido
        for j in range(len(lista_heroe) - 1 - i): # Comparo con los siguientes

            if lista_heroe[j][0].lower() > lista_heroe[j + 1][0].lower(): # Comparo los nombres (posición 0)

            # Intercambio de posiciones
                aux = lista_heroe[j]
                lista_heroe[j] = lista_heroe[j + 1]
                lista_heroe[j + 1] = aux

    print('\nLista ordenada\n')
    ver_heroes(lista_heroe)  # Muestro la lista ordenada



def ver_heroe_alto(lista_heroe):  # Muestra el/los héroes más altos

    altura = lista_heroe[0][3]  # Valor inicial de referencia

    for i in range(len(lista_heroe)):  # Busco máximo
        if lista_heroe[i][3] > altura:
            altura = lista_heroe[i][3]

    print('\n -- El/los heroe/s mas alto/s es/son:')
    for i in range(len(lista_heroe)):  # Muestro coincidencias
        if lista_heroe[i][3] == altura:
            mostrar_heroe(lista_heroe[i])




def ver_heroe_fuerte(lista_heroe):  # Muestra el/los héroes más fuertes

    fuerza = lista_heroe[0][8]  # Valor inicial

    for i in range(len(lista_heroe)):  # Busco máximo
        if lista_heroe[i][8] > fuerza:
            fuerza = lista_heroe[i][8]

    print('\n -- El/los heroe/s mas fuerte/s es/son:')
    for i in range(len(lista_heroe)):  # Muestro coincidencias
        if lista_heroe[i][8] == fuerza:
            mostrar_heroe(lista_heroe[i])




def ver_heroe_delgado(lista_heroe):  # Muestra el/los héroes con menor peso

    peso = lista_heroe[0][4]  # Valor inicial

    for i in range(len(lista_heroe)):  # Busco mínimo
        if lista_heroe[i][4] < peso:
            peso = lista_heroe[i][4]

    print('\n -- El/los heroe/s mas delgado/s es/son:')
    for i in range(len(lista_heroe)):  # Muestro coincidencias
        if lista_heroe[i][4] == peso:
            mostrar_heroe(lista_heroe[i])


def menu():  # Menú principal del programa

    bandera = True  # Bandera que controla el bucle

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
            bandera = False  # Finaliza el programa
            print('Saliendo del menu')

        else:
            print('Opcion no valida')


menu()  # Llamada inicial