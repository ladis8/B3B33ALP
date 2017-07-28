from cmath import sqrt
import sys


def a(x,y,z):
    return (x and y) or (not y and z)
 
def b(x,y,z):
    return x or z

print(a (True,True,False))
print(b (True,False,True))


###################################################
def uk_6_smerodatnaOdchylka(array):
    
    #find average 
    average =0.
    for num in array:
        average +=num
        
    average /=len(array)
    print(average) 
    
    suma =0
    for num in array:
        suma += (num -average)**2
        print (suma)
        
    odchylka = sqrt(suma/len(array))
    print (odchylka)
        
uk_6_smerodatnaOdchylka( [ 1, 1, 0, 1,2,1,0,0,1])
###################################################


"""/////////////////////////////////////////////////////////////
                                POLYNOMY                            
/////////////////////////////////////////////////////////////"""
def uk_7_printPoly( array):
    
    print (array [0], end=" ")

    for i in range (1,len(array)):
        koef = array[i]
        if (koef > 0):
            if (koef==1):
                print ("+ x^%d"%i, end=" ")
            else:
                print ("+ %d x^%d"%(koef,i), end=" ")
        elif (koef < 0):
            if (koef==1):
                print ("- x^%d"%i, end=" ")
            else:
                print ("- %d x^%d"%(abs(koef),i), end=" ")
    print("")           
uk_7_printPoly( [ 1, 1, 0, -2,10,5,-6,0,1])


def uk_8_valueofPoly(array, x):
#"HORNER kladkostroj na polynomy"      

    array.reverse()
    num = array [0]
    
    for i in range(1, len(array)):
        num *=x
        num +=array[i]
    
    print(num)
    
uk_8_valueofPoly( [ -6, 1, 1],2)  

def uk_9_polyMulti (pol1, pol2):
    output = [0]*( len(pol1) + len(pol2)-1)
    
    for i in range (len(pol1)):
        for j in range (len(pol2)):
            output [i+j] += (pol1[i]*pol2[j])
            
    uk_7_printPoly(output)
    
uk_9_polyMulti([1,2,1],[1,2,1])   

"""/////////////////////////////////////////////////////////////
                                POLYNOMY                            
/////////////////////////////////////////////////////////////"""
    