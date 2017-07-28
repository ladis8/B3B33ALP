'''
Created on 23. 10. 2016

@author: stefk
'''
x=int(input())

sum1=0

for k in range(1,x+1,1):
    sum1+=k**3

sum2= int ((x*(x+1)/2)**2)
print(sum1)
print(sum2)