"""
HW04
ZADÁNÍ:
Napište program algebrogram.py, který øeší jednoøádkový algebrogram.
Algebrogram používá pouze sèítání a pouze na levé stranì rovnice.
Úkolem je najít takovou zámìnu písmen za cifry tak, 
aby žádná dvì písmena nemìla stejnou hodnotu a žádné èíslo nezaèínalo 0.
Algebrogram bude zadán na jednom øádku standardního vstupu, napø: send+more=money a výstupem Vašeho programu bude øešení tohoto algebrogramu ve formátu dosazených cifer: 9567+1085=10652
Algebrogram bude zadan bez mezer (tedy 'a+b=c', nikoliv 'a + b = c').
Sèítance se vyskytují pouze na levé stranì rovnice a jejich poèet není omezen.
Pokud má algebrogram více øešení, vytisknìte všechny (netisknìte ale vícekrát stejné øešení)

POZOR: Program je výpoèetnì nároènìjší, otestujte si nejdøíve Váš program na poèítaèi a pouze dùkladnì otestovaný program nahrávejte do odevzdávacího systému
"""

def findLetters (string):
   
    addfirst = True
    for char in string:
        if (char != '+' and char != '='):
            if (uniqueletters.count(char)==0):
                uniqueletters.append(char)
            if (addfirst):
                addfirst = False
                if (firstletters.count(char)==0):
                    firstletters.append(char)
                    
        
        else:          
            addfirst = True


def makeDictionary ():
    
    keys = firstletters.copy()
    for letter in uniqueletters:
        if (keys.count(letter)==0):
            keys.append(letter)
    
    
    dictionary = dict (zip(keys, [i for i in range (len(keys))]))
    return dictionary
        
        
    
    
    
def tryalgebrogram (solution):
    digits = text.split ('=')
    vysledek= digits [1]
    scitance = digits [0]
    scitance = scitance.split ('+') 
    scitancenum = [] 
    #print(vysledek)
    sum=0
    for i in range (0,len(vysledek)): 
            pointer = dictionary [vysledek [i]] 
            sum += solution [pointer]
            
            if (i != len(vysledek)-1):
                sum*=10
    
    vysledekT= sum
    #print (vysledekT)
    
    soucet = 0   
    for scitanec in scitance:      
        sum=0
        for i in range (0,len(scitanec)): 
            pointer = dictionary [scitanec [i]] 
            sum += solution [pointer]
            if (i != len(scitanec)-1):
                sum*=10
        scitancenum.append(sum)     
        soucet +=sum  
    #print (soucet) 
        
    if (vysledekT == soucet):
        #print("found")
        for i in range (len(scitancenum)-1):
            print (scitancenum[i] , end="")
            print ('+', end="")
        print (scitancenum[len(scitancenum)-1],end="")
        print ('=', end= "")
        print (vysledekT)
        #print (solution)
    #else:
        #print ("not correct")

def recurzion (depth, generationcounters):
    #print ("iterace %d" %depth)
    if (depth ==goaldepth):
        tryalgebrogram(solution) 
    else:
       
        for counter in generationcounters:
            possiblecounters =generationcounters.copy()
            
            if (depth+1== len(firstletters)):
                possiblecounters.append(0)
           
            possiblecounters.remove(counter)
            solution [depth] =counter   
            #print (possiblecounters)
            #print (solution)
            recurzion (depth+1, possiblecounters)
            
    #print ("nothing found")

uniqueletters = []
firstletters = []
#text="send+more=money"
text = input()
findLetters(text)
dictionary =  makeDictionary()
#print(dictionary)
#print (text)
#tryalgebrogram(text)

goaldepth = len(uniqueletters)
solution = [-1]*len (uniqueletters)
#print (solution)
startcounters = [i for i in range(1,10)]
#print(startcounters) 


recurzion(0, startcounters)
#print("end")