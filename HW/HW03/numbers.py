"""
HW03
ZADÁNÍ:
Vytvoøte program numbers.py pro úlohu HW03, kterı ze standardního vstupu pøeète øádku, 
která obsahuje bud èíslo v desítkové soustavì nebo èíslo zapsané slovy bez háèkù napø. dvestepadesatsedmtisictristasedmdesatpet a toto èíslo pøevede do opaèného zápisu. 
Pokud vstup neodpovídá ani jedné z tìchto moností, vytiskne 'ERROR' a skonèí.
Vstup dvestepadesatsedmtisictristasedmdesatpet vıstup 257375
Vstup 543210 vıstup petsetctyricettritisicedvestedeset
Všechny èísla jsou pouze celá èísla v rozsahu 1 a 999999.
Pro slovni cislo jsou pouity tyto slovni vyjadreni: 
jeden, dva, tri, ctyri, pet, sest, sedm, osm, devet, deset, jedenact, dvanact, trinact, ctrnact, patnact, sestnact, sedmnact, osmnact, devatenact, dvacet, tricet, ctyricet, padesat, sedesat, sedmdesat, osmdesat, devadesat, sto, dveste, trista, ctyrista, petset, sestset, sedmset, osmset, devetset, tisic, tisice.

Pozn.: V èeštinì je správnì “dvatisice”, ale lze napsat “stodvatisic” a “stodvatisice”. Po Vás poadujeme øešení ve tvaru “stodvatisice”.
"""

"""
MRDKA NEJÌTŠÍHO KALIBRU CO JDE!!!!
"""

cisla1 = ['jeden', 'dva', 'tri', 'ctyri', 'pet', 'sest', 'sedm', 'osm', 'devet']
cisla1num = [i for i in range(1,11)]
cisla11 =['deset','jedenact', 'dvanact','trinact', 'ctrnact', 'patnact', 'sestnact', 'sedmnact', 'osmnact', 'devatenact']
cisla11num =  [i for i in range(10,20)]
cisla10 = ['dvacet', 'tricet', 'ctyricet', 'padesat', 'sedesat', 'sedmdesat', 'osmdesat', 'devadesat']
cisla10num = [i for i in range (20,100,10)]
cisla100 =['sto', 'dveste', 'trista', 'ctyrista', 'petset', 'sestset', 'sedmset', 'osmset', 'devetset']
cisla100num= [i for i in range (100, 1000,100)]
cisla1000=['tisice', 'tisic']

itterable = [cisla100, cisla100num, cisla10, cisla10num, cisla11, cisla11num, cisla1, cisla1num]

def checklength (substring):
    if (len(substring)<2):
        return True
    else:
        return False

def iterateArray (array, substring):
    for num in array:
        if (substring.find(num) != -1):
            return array.index(num)

def addNum (index, arraynum,output):
    output +=arraynum [index]
    return output

def sliceString (index, array,substring):
    substring = substring[len(array[index]):]
    return substring
    
    
    
  

#print (iterateArray(cisla100,"dvestepadesat"))

def make100(vstup):
    
    substring = vstup
    output =0
    
    
    for i in range (0,8,2):
        index=iterateArray(itterable [i],substring)
        
        if not (index == None):
            output = addNum(index, itterable [i+1], output)
            substring =sliceString(index, itterable [i], substring)
        
        if (checklength(substring)):
            return output
        

     

def getDecimal(stringnum):
 #nalezne pozici 1000
    a = stringnum.find("tisic")
    output =0
    
    if (a != -1):
        
        preffix = make100(stringnum[:a])       
        if (preffix ==0):
            preffix =1
        
        suffix = make100(stringnum[a+5:]) 
        output = preffix * 1000 +suffix
        
    else:
        suffix = make100(stringnum) 
        output = output +suffix
    
    return (output)


def getWord (num):
    num = int(num)
    output = ''
    digits =[]

    
    for i in range (6):       
        digits.append(int(num%10))
        num=int(num/10)
        
        

    if (digits[0] != 0):
        output=cisla1[digits[0]-1]
    
        
    if (digits[1] != 0):
        
        if (digits [1] ==1) :  
            output =cisla11[digits[0]]
        
        else:
            output = cisla10[digits[1]-2]+output
    
     
    if(digits[2] != 0):
        output = cisla100[digits[2]-1]+output
    
    
    if (digits[3] != 0):
        
        
        if (digits [4] ==0 and digits [5] ==0):
            #2000 3000
            if (digits [3]==2 or digits [3]==3 or digits [3]==4):
                output = cisla1[digits[3]-1]+"tisice"+output
                #5000
            else:
                output = cisla1[digits[3]-1]+"tisic"+output
        #11000,513000   
        elif (digits[4] == 1):
            output =cisla11[digits[3]]+"tisic"+output
            
        elif (digits [4]==0):
            if (digits [3]==2 or digits [3]==3 or digits [3]==4):
                output = cisla1[digits[3]-1]+"tisice"+output
                #5000
            else:
                output = cisla1[digits[3]-1]+"tisic"+output
            
        
        else:
            #53000,136000
            
            if (digits [3]==2 or digits [3]==3 or digits [3]==4):
                output = cisla10[digits[4]-2]+ (cisla1[digits[3]-1]+"tisice"+output)
                #5000
            else:
                output = cisla10[digits[4]-2]+ (cisla1[digits[3]-1]+"tisic"+output)              
           
    
    elif (digits [3]== 0):
        
        
        if (digits[4] == 1):
            output ="desettisic"+output
            
        elif (digits[4]!= 0):
            output = cisla10[digits[4]-2]+"tisic"+output
        
               
       
    if(digits[5] != 0):
        
        if (digits [4]==0 and digits[3]==0):
       
            output = cisla100[digits[5]-1]+ "tisic"+output
            
        else:
            output = cisla100[digits[5]-1]+ output  
   
    return output         

 

"""
print(getWord(900000))print( getDecimal("dvestepadesatsedmtisictristasedmdesatpet"))
print( getDecimal("petsetctyricettritisicedvestedeset"))
print( getDecimal("dvatisicepetsetdevet"))
print( getDecimal("tisicsedmset" )) """

    
vstup = input()
isNumber =False
isAllowed = True


asci =ord(vstup[0])
if ((asci >= 48 and asci <=57)):
    isNumber = True  
    
for i in range (1,len(vstup)):
    asci =ord(vstup[i])
    if (isNumber):
        
        if not(asci >= 48 and asci <=57):
            isAllowed = False
            break
       
    else:
        if not (asci >= 97 and asci <=122):
            isAllowed =False
            break


if not (isNumber):
    substring = vstup
    for i in range (0,8,1):
        #every array must be itterate 2 times
        if (i%2 ==1):
            i -= 1
        index=iterateArray(itterable [i],substring)
        if (index != None):
            ind =substring.find (itterable [i][index])
            substring = substring[:ind] + substring [ind + len(itterable[i] [index]):]
            
  
    if ((len(substring)== 0 or substring =="tisic"or substring =="tisice")and (isAllowed)):
        print(getDecimal(vstup))
    else:        
        print("ERROR")
   
elif (isAllowed):
    print(getWord(vstup))
else:        
    print("ERROR")
        


        
            

cisla1 = {
    'jeden': 1, 
    'dva': 2, 
    'tri': 3, 
    'ctyri': 4, 
    'pet': 5, 
    'sest': 6, 
    'sedm': 7, 
    'osm': 8, 
    'devet': 9}
cisla10 ={
    'deset': 10, 
    'jedenact': 11, 
    'dvanact': 12, 
    'trinact': 13, 
    'ctrnact': 14, 
    'patnact': 15, 
    'sestnact': 16, 
   'sedmnact': 17, 
    'osmnact': 18, 
    'devatenact': 19,
    'dvacet': 20, 
    'tricet': 30, 
    'ctyricet': 40, 
    'padesat': 50, 
    'sedesat': 60, 
    'sedmdesat': 70, 
    'osmdesat': 80, 
    'devadesat': 90}
cisla100 ={
    'sto': 100, 
    'dveste': 200, 
    'trista': 300, 
    'ctyrista': 400, 
    'petset': 500, 
    'sestset': 600, 
    'sedmset': 700, 
    'osmset': 800, 
    'devetset': 900}
cisla1000={
    'tisic': 1000, 
    'tisice': 1000}





    



