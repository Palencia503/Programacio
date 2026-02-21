#Autor: José Palencia
#Data: 21/02/2025

import os

def generar_estadisticas_txt():
    #funcion para generar estadisticas a partir de jugadors.csv
    jugadors_path = 'data/jugadors.csv'
    estadistiques_path = 'data/estadistiques.txt'
    
    if not os.path.exists(jugadors_path):
        print("Error: El archivo " + jugadors_path + " no se ha encontrado.")
        return
    
    try:
        with open(jugadors_path, 'r', encoding='utf-8') as file_in:
            lineas = file_in.readlines()
            
        with open(estadistiques_path, 'w', encoding='utf-8') as file_out:
            for linea in lineas:
                linea = linea.strip()
                if not linea: 
                    continue
                parts = linea.split(',')
                if len(parts) >= 4:
                    nom = parts[0]
                    #comprobamos si son digitos con isdigit
                    if parts[1].isdigit() and parts[2].isdigit() and parts[3].isdigit():
                        partides = int(parts[1])
                        victories = int(parts[2])
                        derrotes = int(parts[3])
                        
                        if partides > 0:
                            percentatge = (victories / partides) * 100
                        else:
                            percentatge = 0.0
                            
                        #nom, partides, victories, derrotes, porcentagee
                        linea_out = nom + ", " + str(partides) + ", " + str(victories) + ", " + str(derrotes) + ", " + str(round(percentatge, 2)) + "%\n"
                        file_out.write(linea_out)
        print("Estadisticas generadas en " + estadistiques_path)
    except:
        print("Error al generar estadisticas.")
