'''
Created on 16. 11. 2016

@author: stefk
'''

def pascal (n):
    
    pascal = [[1], [1,1]]
    

    for i in range (2,n):
        
        
        pascal += [ [1] 
                   + [pascal [i-1][k]+ pascal [i-1][k+1] for k in range (1, i-1)]
                   +[1]]
        
    return pascal  

print (pascal (4))