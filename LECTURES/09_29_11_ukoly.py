'''
Created on 29. 11. 2016

@author: stefk
'''
def skip_comment(line):
    
    state=0   
    i=-1       
    for chr in line:
        i+=1
        print() 
        print (state) 
        print (chr)
        
        
        if state==0:  #ischarbut not "" or '' 
            if chr=="#": 
                state=1
            elif chr=="\'":
                state=2
                print(chr,end="")
            elif chr =="\"":
                state =4
                print(chr,end="")
            else:
                print(chr,end="")
        
        elif state==1: #just found comment
            continue
        
        elif state ==2:
            if chr == "\'":
                print ("THIS IS WHAT: %c" %line [i-1])
                state = 0
                print (chr, end= "")
            elif chr == "\\":
                state =3
            else:
                print (chr, end="")
        
        elif state ==4:
            if chr == "\"":
                state ==0
                print (chr, end="")
            elif chr =="\\":
                state =5
            else:
                print (chr, end="")
        elif state ==3:
            if chr== "\'":
                state =2
                print (chr, end= "")
            else:
                print ("\\")
                print(chr, end ="")
        
        elif state ==5:
            if chr== "\"":
                state =4
                print (chr, end= "")
            else:
                print ("\\")
                print(chr, end ="")
                
            
                
                
            
 
a="'b\'c#d' #e"
b= "if c=="#":"
#skip_comment (a)
print ()





def isfloat(string):
    state = 0
    numbers = "0123456789"
    
    for chr in string:
        
        if state ==0: #BEGGINING
            if chr=='.': # isDot
                state = 1
            elif chr in numbers and chr != '0': #isDigit
                state =2
            else:
                state = 7
        elif state ==1: #HAVE DOT
            if chr in numbers:
                state =3
            else:
                state =7
        elif state ==2: #PREFIX NUMBERS
            if chr in numbers: #isDigit
                continue
            elif chr =='.': #isDot
                state =2
            elif chr == 'e' or chr == 'E': #havemultiplier
                state = 4
            else:
                state =7
                
        elif state ==3: #SUFFIX NUMBERS
            if chr in numbers: #isDigit
                continue
            elif chr == 'e' or chr =='E': #havemultiplier
                state =4
            else:
                state =7
        elif state ==4: #HAVE SIGN
            if chr=='+' or chr=='-': #havesign
                state =5
            elif chr in numbers : #isDigit
                state =6
            else:
                state =7
        elif state ==5: #HAVE NUMBERS AFTER SIGN
            if chr in numbers:  #isDigit           
                state =6
            else:
                state =7
        elif state ==6: #MULTIPLIER NUMBERS
            if chr in numbers: #isDigit
                continue
            else:
                state = 7
        elif state ==7: #ERROR STATE
            return False
        
    if state ==2 or state ==3 or state ==6:
        return True
    else:
        return False

print (isfloat("3.14"))
print (isfloat("3.14e-25"))




"""--------------------BRACKETS-------------------CV09"""
def brackets (inp):
    stack = []
    rbrackets = "})]"
    lbrackets = "{(["
    i = 0
    while i < len (inp):

        if inp [i] in lbrackets:
            stack.append(inp [i])
        elif inp[i] in rbrackets:
            lbracket = stack.pop()
            if chr (ord (inp[i]) -1)== lbracket or chr (ord (inp[i])-2)==lbracket:
                j = i-1
                while inp [j] != lbracket:
                    j-=1

                print("%c%c %s" % (lbracket, inp[i], inp [j+1:i]))
                inp = inp [:j] +(inp [i+1:])
                i=j-1
        i+=1

brackets ("aa[bb(cc)dd(ee)fff[gggg]]hhh")
        
        
            
    
    

