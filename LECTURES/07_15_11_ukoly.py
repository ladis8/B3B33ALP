'''
Created on 15. 11. 2016

@author: stefk
'''

"""----------------RECURSION-------------------"""
def factorial (n):
    
    if n ==1:
        return 1
    else:
        return n* factorial(n-1)
    
print (factorial(5))

def binomal (n, k):
    
    if (k ==0 or k ==n):
        return 1
    elif (k==1 or k ==n-1):
        return n
    else:
        return binomal (n-1,k) + binomal(n-1,k-1)

print (binomal(5, 3))


def printArray (n, array):
    if (n < len(array)):
        print (array [n])
        printArray(n+1, array)
        
#printArray(0, [0,1,2,3,4,5])


def fibbonaci (n):
    
    fibbarray = [-1] * (n+1)
    fibbarray [0] =0
    fibbarray [1] = 1
    print (fibbarray)
    
    def recursion (n):

        if (fibbarray [n] != -1):

            return fibbarray[n]
        else:
            fibbarray [n] = recursion(n-1)+recursion(n-2)
            return fibbarray[n]
    
    recursion (n)
     
    print (fibbarray [n])
    print (fibbarray)
    
fibbonaci(8)


def hanoitower (n):
    
    start = list (range (n))
    temp =[]
    end= []
    
    
    def hanoi (n, start, temp, end):
        if (n>0):
            #premisteni n-1 ye startu do tempu             
            hanoi (n-1, start, end, temp)
            #premisti disk ze startu do endu
            end.append(start.pop())
            
            print ("start",start, "temp",temp, "end",end)
            
            #premisti n-1 disku z tempu do endu
            hanoi (n-1, temp, start, end)
    
    hanoi (len(start), start,temp, end)
            
hanoitower (3)
"""----------------RECURSION-------------------"""                 