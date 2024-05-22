#!/usr/bin/env python3
import sys
import json


def lire_fichier(fichier):
    with open(fichier, "r") as file:
        dataJson = file.read()        
        #data = json.loads(dataJson)
    
    return dataJson

def pattern_particulier_mot_fichier(mot, fichier):
    chaine = lire_fichier(fichier)
    lst = []
    dic = {}
    taille_mot = len(mot)
    if taille_mot == 0:
        for pos,char in enumerate(chaine):
            dic = {"file": fichier, "pattern": mot, "offset": pos}
            lst.append(dic)
    else:      
        i = 0
        while chaine[i:].find(mot) >= 0:
            i += chaine[i:].find(mot)
            dic = {"file": fichier, "pattern": mot, "offset": i}
            lst.append(dic)
            i+= taille_mot
    return lst
        



def pattern_particulier_mots_fichiers(mots, fichiers):
    lst = []
    for mot in mots:
        for fichier in fichiers:
            lst += pattern_particulier_mot_fichier(mot, fichier)
    print(json.dumps(lst, indent=4))


   
def main():
    argvs = sys.argv[1:]
    list_de_chemins_fichiers = []
    list_des_mots = []
    i = 0
    while i < len(argvs):
        if argvs[i] == '-e':
            i +=1
            if argvs[i] != '-e':
                if argvs[i].rfind('.txt') > 0:
                    list_de_chemins_fichiers.append(argvs[i])   
                else:
                    list_des_mots.append(argvs[i])
            else:
                i-=1
            
            
        elif argvs[i].rfind('.txt') > 0:
            list_de_chemins_fichiers.append(argvs[i])
        i +=1
    pattern_particulier_mots_fichiers(list_des_mots, list_de_chemins_fichiers)
    
    

if __name__ == '__main__':
    main()
