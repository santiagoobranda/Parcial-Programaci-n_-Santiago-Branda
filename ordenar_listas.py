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

            if lista_heroe[j][0].lower() > lista_heroe[j + 1][0].lower(): 

                aux = lista_heroe[j]
                lista_heroe[j] = lista_heroe[j + 1]
                lista_heroe[j + 1] = aux

    print('\nLista ordenada\n')
    ver_heroes(lista_heroe) 

def ver_condicion (lista_heroe, indice, mensaje, modo):
    """
    Brief:
        Busca el valor (maximo o minimo) en una posicion del indice especifico de la lista de los heroes
        y muestra todos los que coincidan con ese valor.

    Parametros:
        lista_heroe (list): Lista de heroes
        indice (int): Posicion del atributo a comparar
        modo (str): 'max' para maximo o 'min' para minimo
       

    Retorno:
        None
    """

    condicion = lista_heroe[0][indice]

    for i in range(len(lista_heroe)):
        if modo == 'max':
            if lista_heroe[i][indice] > condicion:
                condicion = lista_heroe[i][indice]

        elif modo == 'min':
            if lista_heroe[i][indice] < condicion:
                condicion = lista_heroe[i][indice]

    print (mensaje)

    for i in range(len(lista_heroe)):
        if lista_heroe[i][indice] == condicion:
            mostrar_heroe(lista_heroe[i])