# Autor: Jose Palencia
# Fecha: 25/11/2025
# Descripcion:
# Este ejercicio comprueba si una lista es simetrica.
# Una lista es simetrica si se lee igual de izquierda a derecha que de derecha a izquierda.
# Si es simetrica muestra cuantos elementos tiene.
# En todos los casos muestra tambien la lista invertida.


def main():
    def es_simetrica(lista):
        return lista == lista[::-1]
    
    def lista_invertida(lista):
        return lista[::-1]

    lista_simetrica = [1, 2, 3, 2, 1]
    l = es_simetrica(lista_simetrica)
    n = lista_invertida(lista_simetrica)

    if l == True:
        print('La lista es simetrica.')
        print('La lista tiene', len(lista_simetrica), 'elementos.')
    else:
        print('La lista NO es simetrica.')
    print('Lista INVERTIDA:', n)

if __name__ == "__main__":
    main()
