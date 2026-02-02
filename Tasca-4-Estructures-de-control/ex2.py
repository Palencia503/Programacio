# Autor: Jose Palencia
# Fecha: 25/11/2025
# Descripcion:
# Este ejercicio pide dos numeros y compara cual es mayor o si son iguales.
# Se debe comprobar que las entradas sean numericas, en caso contrario mostrar un error.


def main():
    def clasificado_numeros(n1, n2):
        if n1 > n2:
            print('Numero 1 es mayor')
        elif n2 > n1:
            print('Numero 2 es mayor')
        else:
            print('Los numeros son iguales')
            
    try:
        n1 = int(input('Ingresa el primer numero: '))
        n2 = int(input('Ingresa el segundo numero: '))

        print('Clasificacio: ')
        clasificado_numeros(n1, n2)
    except ValueError:
        print('¡Error!. Has introducido letras o caracteres. El programa solo permite numero.')
   

if __name__ == "__main__":
    main()