# Autor: Jose Palencia
# Fecha: 25/11/2025
# Descripcion:
# Este ejercicio analiza una lista y comprueba que numeros coinciden con su posicion (indice).
# Ejemplo: en la lista [3,4,2,0,2,3,6], el 2 coincide con la posicion 2 y el 6 con la posicion 6.
# El programa debe mostrar las posiciones que coinciden, no solo el numero total de coincidencias.


def main():

    def comprabador(x):
        posiciones = []
        for i, valor in enumerate(x):
            if i == valor:
                posiciones.append(i)
        return posiciones

    lista = [3, 4, 2, 0, 2, 3, 6]
    pos = comprabador(lista)
    print('Coinciden: ', len(pos))
    print('Pocisiones que coinciden: ', pos)
   

if __name__ == "__main__":
    main()