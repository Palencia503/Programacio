# Autor: Jose Palencia
# Fecha: 25/11/2025
# Descripcion:
# Este ejercicio pide al usuario una lista de numeros separados por comas.
# El programa debe mostrar:
# - El numero total de elementos.
# - La media aritmetica de los valores.
# - Cuantos numeros son pares y cuantos son impares.


def main():
    def media(x):
        suma = 0
        for p in x:
            suma += int(p)
        media = suma / len(x)
        print(round(media, 2))

    def parell_imparells(x):
        parells = []
        imparells = []

        for p in x:
            numero = int(p)
            if numero % 2 == 0:
                parells.append(numero)
            else:
                imparells.append(numero)
        print("Numeros pares:", len(parells))
        print("Numeros impares:", len(imparells))
        
    entrada = input("Ingresa una lista de numeros separados por comas: ")
    partes = entrada.split(",")

    print('Numero de elementos: ', len(partes))
    media(partes)
    parell_imparells(partes)


if __name__ == "__main__":
    main()