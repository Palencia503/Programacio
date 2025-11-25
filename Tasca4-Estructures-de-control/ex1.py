# Autor: Jose Palencia
# Fecha: 25/11/2025
# Descripcion:
# Este ejercicio consiste en crear una funcion que clasifique una nota numerica
# segun la escala: Suspes, Aprovat, Notable o Excelent.
# La nota puede ser decimal y se redondea a un decimal antes de clasificarla.
# Condiciones: Suspes < 5, Aprovat >= 5 y < 7, Notable >= 7 y < 9, Excelent >= 9.


def main():
    def clasificador(x):
        if x >= 9:
            print('Exelent')
            return x
        elif x >= 7:
            print('Notable')
            return x
        if x >= 5:
            print('Aprovat')
            return x
        else:
            print('Suspes')

    nota = float(input('Ingresa la nota: '))
    print('Clasificacio: ')
    clasificador(nota)
   

if __name__ == "__main__":
    main()