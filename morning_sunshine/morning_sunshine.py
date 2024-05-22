#!/usr/bin/python3
import sys
import json
import math


def benefice_un_batiment(batiment, pourcentage):
    benefice = 0
    for appartement in batiment:
        orientations = appartement["orientations"]
        if "E" in orientations:
            benefice += math.ceil(appartement["monthly_rent"] * pourcentage)
            
    return benefice



def benefice_des_batiments(list):
    benefice_total = 0
    pourcentage = 0.05
    index_next= 1
    height_max = 0
    taille = len(list)
    index = taille-1
    
    if taille > 0: 
        height_max = list[index]["height"]
        floor_layout = list[index]["floor_layout"]
        benefice_provisoir = benefice_un_batiment(floor_layout, pourcentage)
        benefice_total = benefice_provisoir*height_max 
        
        index_2 = index-1
        
        while index_2 >= 0:
            height = list[index_2]["height"]
            
            if height > height_max:
                floor_layout = list[index_2]["floor_layout"]
                benefice_provisoir = benefice_un_batiment(floor_layout, pourcentage)
                benefice_provisoir *=(height - height_max)
                benefice_total += benefice_provisoir
                height_max = height
            
            index_2 -=1     
            
        benefice_total *= 12
    benefice_total_formatJson = json.dumps(benefice_total)
    print(benefice_total_formatJson)

    
def main():
    dataJson = sys.argv[1]
    data = json.loads(dataJson)
    benefice_des_batiments(data)
    

if __name__ == '__main__':
    main()
    
