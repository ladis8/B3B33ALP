'''
Created on 11. 11. 2016

@author: stefk
'''
print ("dobry vecer" [::-1])
print ([1,2,3,4,5] [::-1])


""""-----------------RECURSION-----------------"""

def reverse_recursive(s):
    """prida prvni symbol na konec retezce"""
    return "" if len (s) ==0 else reverse_recursive(s[1:])+s[0]

print(reverse_recursive("dobry vecer"))


def count_to_recursive2(n):
    def count_to_recursive_inner(i):
        if i<=n:
            print(i)
            count_to_recursive_inner(i+1)
    count_to_recursive_inner(1)

count_to_recursive2(5)

def zaplat(x):
    h=[50,20,10,5,2,1] 
    def doplat(x,m,i):

        if x==0:
            print ("platba")
        else:
            if x>=h[i]: 
                print ("doplat")
                doplat(x-h[i],m[:i]+[m[i]+1]+m[i+1:],i)
            if i<len(h)-1: 
                print ("doplat")
                doplat(x,m,i+1)
                
    doplat(x,len(h)*[0],0) 


zaplat(5)

def permutation (m, zacatek):  
    
    if (len (m) ==0):
        print(zacatek)
    else:
        for i in range (len ( m)):
            """vezme prvni cast a druhou cast a spoji ji dohromady"""
            permutation (m [:i] + m [i+1:], zacatek +m [i])
    
permutation(['a','b', 'c', 'd'], "")
    
""""-----------------RECURSION-----------------"""