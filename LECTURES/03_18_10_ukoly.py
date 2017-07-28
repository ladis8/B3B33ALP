#num= int (input())
#num2= int (input())
def uk_3_delitel(num1,num2):
    
    ###second option
    a =num1
    b=num2
    pocetkroku =0
    
    while (a != b):      
        pocetkroku= pocetkroku +1
        if (a > b):
            a = a-b
        else:
            b= b-a
            
    print (pocetkroku)
    
    ###second option
    a =num1
    b=num2
    pocetkroku =0
    while (b != 0):
        pocetkroku= pocetkroku +1
        t =b
        b = a%b
        a=t
    
    print (pocetkroku)
        
    
#uk_3_delitel(num, num2)

def uk_4_Cesarovasifra (tex, posun):
    
    text = list(tex)
    output =list()
    
    
    for i in range(len(text)):
        x =ord(text[i])+posun
        
        if (ord(text[i]) == 32):
            output.append("")
        else:
            if (x< ord('a')):                
                output.append(chr(x+26))
            elif (x> ord('z')):                
                output.append(chr(x-26))
            else:
                output.append(chr(x))
                
    
    print (output)  
    
#uk_4_Cesarovasifra("abcdefgh svete", 10) 
    
    
def uk_2_soucetkrzychli():
       
    for x in range (1000,9999):
        maxa = int(pow(x, 1/3.) +0.1)
        counter =0
        
        for a in range (0,maxa):
            b = int (pow(x-a**3, 1/3.)+0.1)
            
            if (a <b and a**3 + b**3 ==x):
                counter+= 1
                if (counter==2):
                    return ("x=",x,"a=",a, "b=",b)
#print (uk_2_soucetkrzychli())


"""/////////////////////////////////////////////////////////////
                                STRINGS                           
/////////////////////////////////////////////////////////////"""
def uk_7_findString(text,word):
    
    #add last character for convenient purposes
    text +=" "      
    i = 0
    output =list()
    while (i < len(text)):     
        
        if (text[i]==word[0]):        
            index =i
            j =0                                     
            while (True):             
                if (text [i] != word[j]):
                    break
                else:
                    i +=1
                    if (j == len(word)-1):                       
                        output.append(index)
                        break
                    else:
                        j +=1   
        else:                                                     
            i=i+1                          
    return output
      
def uk_8_replaceString (word, replaceword, text):
    
    indexes = uk_7_findString (text, word)
    if (len(indexes)==0):
        print("There are no matches")
    else:
        for index in indexes:
            output = text [:index] +replaceword+text [index+len(replaceword):] 
            text=output

    print (text)

uk_8_replaceString("ah", "GG","bbaahoj svete, jak ahse masah" )  
    