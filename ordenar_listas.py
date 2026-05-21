from muestreo import *

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
