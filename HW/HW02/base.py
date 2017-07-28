"""
HW02
ZADÁNÍ:
Vytvořte program base.py, která ze standardního vstupu přečte řádku, 
která obsahuje desetinné číslo a druhou řádku, která obsahuje základ soustavy čísla z první řádky.
Základ soustavy je v rozmezí 2 .. 36
Pro soustavy o základu menším nebo rovno 10, obsahuje desetinné číslo pouze čísla od 0 .. základ soustavy - 1 a znak .
Pro soustavy o základu větším než 10, obsahuje desetinné číslo čísla 0,..,9 a písmena 'a', .. , 'z', ale hodnota ord(znak)−odr(′a′)<zaklad_soustavy−10ord(znak)−odr(′a′)<zaklad_soustavy−10.
Desetinné binární číslo 101.0101=1∗22+0∗21+1∗20+0∗2−1+1∗2−2+0∗2−3+1∗2−4=5.3125101.0101=1∗22+0∗21+1∗20+0∗2−1+1∗2−2+0∗2−3+1∗2−4=5.3125.
Výstupem programu je zadané číslo převedené do desítkové soustavy (tedy pro vstup 101.0101 bude výstup 5.3125)
Pokud je na vstupu špatně zadané číslo (obsahuje jiné znaky než povolené cifry a znak '.', případně obsahuje znak '.' vícekrát), pak vytiskne na výstup slovo “ERROR”
Správnost vstupu základu soustavy nemusíte testovat.
"""

def checkinput(input, base):
    
    inputlist = list(input)
    dot = False
    
    for i in range (len(inputlist)):
        letter = ord (inputlist [i])     
        #check whether the char is dot
        if (inputlist [i] == '.'):
            #check whether there is more than one dot
            if (dot ==False):       
                dot = True
                dotpointer = i
            else:
                return "ERROR"
        else:
            
            #check whether the letter is allowed
            if (letter < 48 or letter >122 or (letter > 57 and letter < 97)):
                #print ("invalid letter")
                return "ERROR"
            
            #check whether the letter is not greater or equal to base
            if (letter >= 97 and letter - 97 >= base -10):
                #print ("invalid base - a")
                return "ERROR"
            elif ((letter >= 48 and letter <= 57) and letter - 48 >= base):
                #print ("invalid base - 0")
                return "ERROR"
        
    #check whether there is at least one dot    
    if (dot):
        return dotpointer
    else:
        return "ERROR"
 
def createlists (number, dotpointer):
    input = list(number)
    nums = list ()
    indexes = list()
    index = dotpointer-1
    for i in range (len(input)):
        
        if (input [i] != '.'):
            
            if (ord(input[i]) >= 97):                
                nums.append(ord(input [i]) -97 +10)
            else:
                nums.append(ord (input [i]) -48)
            
            indexes.append(index)
            index = index -1
  
    return nums, indexes
         
def count (base, nums, indexes):
    
    suma=0
    
    for i in range (len (nums)):
        
       # print (suma)
        #print((base **indexes[i] ))
        
        suma = suma + nums[i]*(base**indexes[i])
    
    return suma   



inp = input()
base = int (input())
check=checkinput(inp, base)

if (check != "ERROR"):
    nums, indexes = createlists(inp, check)
    #print (nums)
    #print(indexes)
    print (count (base,nums, indexes))
else:
    print(check)