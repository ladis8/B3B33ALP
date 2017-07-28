'''
Created on 20. 12. 2016

@author: stefk
'''

import random
random.seed =1
#else nastavi cas

seed = 19
m = 63
a =22
c= 4


x = seed
for _ in range (50):
    x = (a*x +c) %m
    print (x )
   
    

for i in range (20):
    print (random.random())


