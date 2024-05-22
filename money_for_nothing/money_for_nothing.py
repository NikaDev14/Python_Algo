#!/usr/bin/env python3
import sys
import json

def money_for_nothing(list):
    index = 0
    result = []
    taille = len(list)
    achat = True
    if taille > 1:
        if list[index] < list[index+1]:
            #acheter
            result.append(index)
            achat = False

        index = index+1
        while index < (taille - 1):
            #acheter
            if list[index-1] >= list[index] < list[index+1] and achat:
                result.append(index)
                achat = False
            #Vendre
            if  list[index-1] <= list[index] > list[index+1] and not achat:
                result.append(index)
                achat = True
            index+=1
        if not achat:
            if list[taille-1] >= list[taille-2]:
                #Vendre
                result.append(taille-1)
            else:
                #Vendre
                result.append(taille-2)
    result_formatJson = json.dumps(result)
    print(result_formatJson)
          
    
def main():
    dataJson = sys.argv[1]
    data = json.loads(dataJson)
    money_for_nothing(data)
    

if __name__ == '__main__':
    main()
    
    




