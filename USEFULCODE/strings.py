'''
Created on 18. 11. 2016

@author: stefk
'''
"""/////////////////////////////////////////////////////////////
                               
                                STRINGS   
                                        
-module for convenient work with strings, finding and replacing 
               
/////////////////////////////////////////////////////////////"""

def findstring(text,word):
    "Function that finds all indexes of a given substring" 
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
      
def replacestring(word, replaceword, text):
    "Function thath replace ALL substrings in a text"
    
    indexes = findstring (text, word)
    if (len(indexes)!=0):
        for index in indexes:
            output = text [:index] +replaceword+text [index+len(replaceword):] 
            text=output

    return text