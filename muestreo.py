from heroes import *

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


def ver_heroes(lista_heroes):
    """
    Brief:
        Recorre la lista principal mediante un bucle for e imprime cada heroe usando sus indices.
    Parametros:
        lista_heroe: Lista bidimensional que contiene a todos los heroes guardados.
    Retorno:
        None
    """
    print('-- LISTA DE HEROES --')
    for i in range(len(lista_heroes)):  
        mostrar_heroe(lista_heroes[i]) 