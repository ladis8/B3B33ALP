"""
HW01
ZADÁNÍ:
Vytvořte program která ze standardního vstupu přečte jednu řádku, 
která obsahuje posloupnost celých čísel x1,…,xnx1,…,xn 
a v této posloupnosti najde nejdelší neklesající posloupnost xi≤xi+1≤…≤xi+jxi≤xi+1≤…≤xi+j 
a na výstup vytiskne její délku a na další řádek její součet.
Pokud je v posloupnosti čísel více stejně dlouhých neklesajících posloupností, 
pak program hledá tu s největším součtem
"""

nums = list(map(int, input().split()))
previous = nums [0]
suma = previous
maxsum = previous
counter =1
maxcounter =1



for i in range (1, len(nums)):
    
    if (previous <= nums [i]):
        suma += nums [i]
        counter += 1                      
        if (counter > maxcounter):
            maxsum = suma
            maxcounter = counter;
                
        elif (counter == maxcounter and maxsum < sum):
            maxsum = suma                                                                           
            
    else:
        counter =1
        suma =nums [i]
                       
    previous = nums [i];
    
print(maxcounter)
print(maxsum)

