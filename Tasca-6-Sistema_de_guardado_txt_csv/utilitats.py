#Autor: José Palencia
#Data: 21/02/2025

import os
import csv

def carregar_preguntes_txt(path):
    preguntes = []
    if not os.path.exists(path):
        pass
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for linea in file:
                linea = linea.strip()
                if not linea: 
                    continue
                parts = linea.split(',')
                if len(parts) >= 2:
                    preguntes.append((parts[0], parts[1]))
    except:
        print("Error: El archivo " + path + " no se ha encontrado.")
    return preguntes

def carregar_preguntes_csv(path):
    preguntes = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            r = csv.reader(file)
            cabecera = True
            for parts in r:
                if not parts: 
                    continue
                if cabecera == True:
                    cabecera = False
                    continue
                if len(parts) >= 2:
                    preguntes.append((parts[0], parts[1]))
    except:
        print("Error: El archivo " + path + " no se ha encontrado.")
    return preguntes
#hace las preguntas y cuenta las correctas
def fer_preguntes(preguntes):
    punts = 0
    for pregunta, resposta_correcta in preguntes:
        print(pregunta)
        resposta = input("Respuesta: ").strip()
        if resposta.lower() == resposta_correcta.lower():
            print("Correcto!")
            punts += 1
        else:
            print("Incorrecto. La respuesta era: " + resposta_correcta)
    return punts
#añade el ranking
def afegir_ranking(path, nom, punts):
    fitxer_existeix = os.path.exists(path)
    try:
        with open(path, 'a', encoding='utf-8') as file:
            if not fitxer_existeix:
                file.write("nom, punts\n")
            file.write(nom + "," + str(punts) + "\n")
    except:
        print("Error al guardar el ranking.")
#lee el ranking
def llegir_ranking(path):
    ranking = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cabecera = True
            for linea in file:
                linea = linea.strip()
                if not linea: continue
                if cabecera == True:
                    cabecera = False
                    continue

                parts = linea.split(',')
                if len(parts) >= 2:
                    nom = parts[0]
                    if parts[1].isdigit():
                        punts = int(parts[1])
                        ranking.append((nom, punts))
    except:
        print("Todavia no hay ningun ranking en " + path + ".")

    return ranking

def mostrar_ranking_ordenat(ranking):
    print("\n- RANKING -")
    if not ranking:
        print("El ranking esta vacio.")
        return
    
    def obtener_puntos(elemento):
        return elemento[1]
    ranking_ordenado = sorted(ranking, key = obtener_puntos, reverse = True)

    contador = 1
    for nom, punts in ranking_ordenado:
        print(str(contador) + ". " + nom + " - " + str(punts) + " puntos")
        contador += 1
    print("----------------\n")
