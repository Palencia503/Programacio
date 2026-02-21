#Autor: José Palencia
#Data: 21/02/2025

import utilitats
import estadistiques
import os

def actualizar_estadisticas_partida(nom, punts, total_preguntes): 
    jugadors_path = 'data/jugadors.csv'
    jugadors = []
    jugador_trobat = False

    #lee los jugadores existentes
    if os.path.exists(jugadors_path):
        try:
            with open(jugadors_path, 'r', encoding='utf-8') as f:
                for linea in f:
                    linea = linea.strip()
                    if not linea: 
                        continue

                    parts = linea.split(',')
                    if len(parts) >= 4:
                        nom_j = parts[0]
                        if parts[1] == "partides":
                            jugadors.append(linea)
                            continue
                        
                        #comprobamos con isdigit 
                        if parts[1].isdigit() and parts[2].isdigit() and parts[3].isdigit():
                            partides = int(parts[1])
                            victories = int(parts[2])
                            derrotes = int(parts[3])

                            if nom_j == nom:
                                jugador_trobat = True
                                partides += 1
                                victories += punts
                                #asumiendo que errores = preguntas totales - aciertos
                                derrotes += (total_preguntes - punts)
                            jugadors.append(nom_j + "," + str(partides) + "," + str(victories) + "," + str(derrotes))
        except:
            print("Error leyendo " + jugadors_path)

    #si no se ha encontrado el jugador, lo añadimos
    if not jugador_trobat:
        derrotes = total_preguntes - punts
        jugadors.append(nom + ",1," + str(punts) + "," + str(derrotes))

    #guardamos todos los jugadores actualizados
    try:
        with open(jugadors_path, 'w', encoding='utf-8') as f:
            for j in jugadors:
                f.write(j + '\n')
    except:
        print("Error escribiendo en " + jugadors_path)


def main():
    print("Bienvenido al Juego de Preguntas y Puntuaciones!")
    nom = input("Introduce tu nombre: ").strip()
    
    #comprobamos si el nombre esta vacio
    if not nom:
        nom = "Anonimo"

    print("\nSelecciona la dificultad:")
    print("1. facil")
    print("2. media")
    print("3. dificil")
    
    dificultad = input("Opcion  (1/2/3): ").strip()

    path = ""
    es_csv = False

    if dificultad == '1' or dificultad.lower() == 'facil':
        path = 'data/preguntes_facil.txt'

    elif dificultad == '2' or dificultad.lower() == 'media':
        path = 'data/preguntes_mitja.txt'

    elif dificultad == '3' or dificultad.lower() == 'dificil':
        path = 'data/preguntes_dificil.csv'
        es_csv = True
    else:
        print("Opcion no valida. Se aplicara dificultad facil por defecto.")
        path = 'data/preguntes_facil.txt'

    #carga las preguntas
    print("\nCargando preguntas...")
    if es_csv == True:
        preguntes = utilitats.carregar_preguntes_csv(path)
    else:
        preguntes = utilitats.carregar_preguntes_txt(path)

    if not preguntes:
        print("No se han podido cargar preguntas.")
        return

    #guarda los puntos y el total de preguntas
    punts = utilitats.fer_preguntes(preguntes)
    total_preguntes = len(preguntes)

    print("\nPartida terminada! Has conseguido " + str(punts) + " punto(s) de " + str(total_preguntes) + " posibles.")

    #Guarda el resultado en el ranquing
    ranking_path = 'data/ranking.csv'
    utilitats.afegir_ranking(ranking_path, nom, punts)

    #Mostra el ranquing ordenado
    ranking = utilitats.llegir_ranking(ranking_path)
    utilitats.mostrar_ranking_ordenat(ranking)

    #Actualitza estadisticas de jugador al CSV
    actualizar_estadisticas_partida(nom, punts, total_preguntes)

    #Ejecuta el calculo de estadisticas
    estadistiques.generar_estadisticas_txt()


if __name__ == "__main__":
    main()