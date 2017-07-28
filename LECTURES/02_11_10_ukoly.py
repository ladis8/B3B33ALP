presnost = 0.00000001
num= int (input())

def uk8_newtononovametoda(xi):
   
    xi1= 1/3*(2*xi + num/(xi**2))
    
    if (abs (xi1 - xi)> presnost):
        uk8_newtononovametoda(xi1)
    else:
        print(xi1)
    

###odhad
print ("Newtonova metoda: ")
uk8_newtononovametoda(1) 


##################################################################
def uk7_tretiodm ():

    x =0
    if (num > 0):
        puleni (x, num)
    else :
        puleni (num, x)
    
    
def puleni(start, end):
  
    x = (start+end)/2 
    ##print ("start %f, end %f, delta %f" %(start, end, end-start)) 
    if (abs(start - end)> presnost):     
        
        mocnina = x**3
      
        if (mocnina - num > 0):         
            puleni (start, x)    
        elif(mocnina ==0):
            print (x)     
        else:
            puleni (x, end)
            
    else:
        
        print (x)
        


print ("Metoda puleni: ")
uk7_tretiodm()

####################################################
def uk5_tretiodm(num, step, value):    
    while ((value+step)**3 < num ):
        value += step
    
    if (step> presnost):
        uk5_tretiodm(num, step/10, value)
    
print ("Metoda kroku: ")
uk5_tretiodm(num, 1, 0)


####################################################  
def uk4_tisksach (n):
#smart idea by our lector
    for i in range (0, n):
        for j in range (0, n):
            if ((i+j)%2 ==0):                      
                print('O',end="")
            else:
                print('*',end="")
            
                        
        print ()
##uk4_tisksach(8)


####################################################
def uk_3brakloop():
    n =int(input())
    delitel = 2
    
    while not (n%delitel ==0):
        delitel+=1
    
    print (delitel)
        
def uk2_timefun ():
    seconds =int(input())
    dny = int (seconds/(3600*24))
    seconds = seconds - dny*3600*24
    hodiny =int(seconds/3600)
    seconds = seconds - hodiny*3600
    minuty = int (seconds/60)
    seconds = seconds - minuty*60
    
    
    print ("Time is: %d dny  %d  hodiny %d minuty %d seconds" % (dny,hodiny,minuty, seconds))



