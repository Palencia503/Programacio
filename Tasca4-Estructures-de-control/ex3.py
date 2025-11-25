# Autor: Jose Palencia
# Fecha: 25/11/2025
# Descripcion:
# Este ejercicio pide el nombre del usuario y un numero.
# Si el numero es 0 muestra un error.
# Si es positivo repite el nombre tantas veces como indique el numero, separado por comas.
# Si es negativo muestra un aviso pero igualmente repite el nombre el numero de veces indicado.


def main():
    def mostrar_nombre(nom, numero):
        if numero == 0:
            print("¡Error! El numero no puede ser 0.")
        else:
            if numero < 0:
                numero = abs(numero)

            for i in range(numero):
                if i == numero - 1:
                    print(nom, end="")  
                else:
                    print(nom, end=", ")
            print()

    nom = input("Ingresa tu nombre: ")
    numero = int(input("Ingresa un numero: "))
    mostrar_nombre(nom, numero)


if __name__ == "__main__":
    main()
