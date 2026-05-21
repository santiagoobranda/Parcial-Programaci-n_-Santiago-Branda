from muestreo import *

from heroes import *


def ordenar_alfabeticamente(lista_heroes):
    """
    Brief:
        Ordena los heroes alfabeticamente por el nombre (indice 0) aplicando el algoritmo bubble sort.
        Hace el intercambio de posiciones usando una variable auxiliar.
    Parametros:
        lista_heroe : Lista que se va a ordenar de forma interna.
    Retorno:
        None
    """
    for i in range(len(lista_heroes) - 1): 
        for j in range(len(lista_heroes) - 1 - i): 

            if lista_heroes[j][0].lower() > lista_heroes[j + 1][0].lower(): 

                aux = lista_heroes[j]
                lista_heroes[j] = lista_heroes[j + 1]
                lista_heroes[j + 1] = aux

    print('\nLista ordenada\n')
    ver_heroes(lista_heroes) 

def ver_condicion (lista_heroes, indice, mensaje, modo):
    """
    Brief:
        Busca el valor (maximo o minimo) en una posicion del indice especifico de la lista de los heroes
        y muestra todos los que coincidan con ese valor.

    Parametros:
        lista_heroe : Lista de heroes
        indice : Posicion del elemento a comparar
        modo: 'max' para maximo o 'min' para minimo
       

    Retorno:
        None
    """

    condicion = lista_heroes[0][indice]

    for i in range(len(lista_heroes)):
        if modo == 'max':
            if lista_heroes[i][indice] > condicion:
                condicion = lista_heroes[i][indice]

        elif modo == 'min':
            if lista_heroes[i][indice] < condicion:
                condicion = lista_heroes[i][indice]

    print (mensaje)

    for i in range(len(lista_heroes)):
        if lista_heroes[i][indice] == condicion:
            mostrar_heroe(lista_heroes[i])