#!/usr/bin/env python3
import sys
import json

def schools_out(list_plannings):
    nb_planings = len(list_plannings)
    # tri des intervalles par valeurs croissantes d'heures de dèbut
    list_plannings = sorted(list_plannings, key=lambda horaire_start: horaire_start["start"])
    # tri des intervalles par valeurs croissantes d'heures de fin
    list_plannings = sorted(list_plannings, key=lambda horaire_end: horaire_end["end"])
    
    j = 0
    # le nombre de salles
    conteur=0
    if nb_planings > 0:
        conteur = 1
        for i in range(1,nb_planings):
            if list_plannings[i]["start"] >= list_plannings[j]["end"]:
                j += 1
            else:
                conteur += 1
    result_formatJson = json.dumps(conteur)
    print(result_formatJson)
          
    
def main():
    fichier = sys.argv[1]
    with open(fichier, "r") as file:
        dataJson = file.read()
        data = json.loads(dataJson)
    schools_out(data)
    

if __name__ == '__main__':
    main()
    
    




