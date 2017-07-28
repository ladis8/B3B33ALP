#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
HW05
ZAD�N�:
Napi�te program tttwinner.py, kter� na�te soubor zadan� na p��kazov� ��dce (argv[1]) a zkontroluje, kdo vyhr�l partii pi�kvorek.
Soubor (viz. p��klad ticktacktoe.txt) obsahuje dvourozm�rn� pole, ve kter�m jsou hodnoty 0 - nepou�it� pole, 1 - k��ek, 2 - kole�ko. Program vyhodnot�, zda pole obsahuje v �ad� �i �hlop���ce alespo� p�t stejn�ch hodnot r�zn�ch od 0.
Pokud v poli nen� alespo� p�t sousedn�ch hodnot 1 ani 2, program vytiskne 0
Pokud je v poli alespo� p�t sousedn�ch 1 ale nen� alespo� p�t sousedn�ch 2, pak vytiskne 1
Pokud je v poli alespo� p�t sousedn�ch 2 ale nen� alespo� p�t sousedn�ch 1, pak vytiskne 2
Pokud je v poli alespo� p�t sousedn�ch 1 i 2, nebo pole obsahuje i jin� hodnoty ne� 0,1,2, pak vytiskne ERROR
Program v souboru tttwinner.py odevzdejte pomoc� odevzd�vac�ho syst�mu (�loha HW05).
"""


import sys


def readInput ():
    pole = []
    filename = sys.argv[1]
    #filename ="ticktacktoe.txt"
    f = open(filename,'r')
    
    line = f.readline()
    
    firstrow = list(map(int, line.split()))
    firstrow.append(0)
    firstrow.insert(0, 0)
    
    size = len(firstrow)
    pole.append ([0]*size)
    pole.append(firstrow)
    
    for line in f:
    
            row = list(map(int, line.split()))
            row.append(0)
            row.insert(0, 0)
            pole.append(row)
            
    
    
    pole.append ([0]*size)
    f.close()
    
    return pole




def getWinner (array):
    
    winners = list()
    
    for x in range (len(array)):
        for y in range (len (array[x])):
            #print (array [x][y], end= " ")
          
            player = array [x][y]
            #print(player)
            
            if (player == 1 or player ==2):
                
                i=x
                j=y
                
                #leva dolni diagonala
                count =1                
                while (array[i-1][j-1] ==player):
                    i-=1
                    j-=1
                    count +=1
                    if (count ==5):
                        winners.append(player)
                
                i=x
                j=y   
                #dolu
                count =1
                while (array[i-1][j] ==player):
                    i-=1              
                    count +=1
                    if (count ==5):
                        winners.append(player)
                
                i=x
                j=y
               #prava dolni diagonala
                count =1
                while (array[i-1][j+1] ==player):
                    i-=1
                    j+=1
                    count +=1
                    if (count ==5):
                        winners.append(player)
                """
                i=x
                j=y
                #doleva
                count =1
                while (array[i][j-1] ==player):                    
                    j-=1
                    count +=1
                    if (count ==5):
                        winners.append(player)
                
                """
                i=x
                j=y
                
                #doprava
                count =1
                while (array[i][j+1] ==player):
                    
                    j+=1
                    count +=1
                    if (count ==5):
                        winners.append(player)
                i=x
                j=y
                """
                #leva horni diagonala
                count =1
                while (array[i+1][j-1] ==player):
                    i+=1
                    j-=1
                    count +=1
                    if (count ==5):
                        winners.append(player)
                
                i=x
                j=y
                """
                """
                #nahoru        
                count =1
                while (array[i+1][j] ==player):
                    i+=1
                    count +=1
                    if (count ==5):
                        winners.append(player)
                        
                i=x
                j=y
                """
                #prava horni diagonala
                """count =1
                while (array[i+1][j+1] ==player):
                    i+=1
                    j+=1
                    count +=1
                    if (count ==5):
                        winners.append(player)
                """
                        
            elif (player !=0):
                #print(player)
                winners.append(-1)
        #print ()          
    
    if (len(winners)==0):
        print("0")
    elif (len(winners)>1 or winners [0]==-1):
        if (sum(winners)/ len (winners) == winners [0]):
            print(winners [0])
        else:
            #print (winners [0])
            #print (winners [1])
            print("ERROR")
    else:
        print(winners [0])



pole = readInput()
#print(pole)
getWinner (pole)





def fileStuff(path):
    
    pole=[]
    f=open(path,'r')
    
    for line in f:
        pole.append(int(line))
    
    f=open(path,'r')
    line = f.readline()
    print (line.split())
    pole = list(map(int, line.split()))
    


