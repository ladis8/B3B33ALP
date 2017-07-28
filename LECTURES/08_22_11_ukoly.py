'''
Created on 22. 11. 2016

@author: stefk
'''
import os
import time

cards = [[0,'Q'], [2,'6'], [1,'K'], 
         [1,'8'], [2,'10'], [2,'4'], 
         [3,'4'], [0,'4'], [1,'3'], 
         [2,'5'], [0,'K'], [3,'A'], 
         [1,'J'], [0,'3'], [0,'9']]

cardvalstr = ['2', '3','4','5', '6','7','8', '9','10','J','Q', 'K', 'A']
cardvalnum = [ i for i in range (2,15)]
print (cardvalnum)

def uk1_radix_sort (array):
    
    
    print (array) 
    radix= 14
    
    for i in range (1,-1,-1):
        
        buckets = [list() for _ in range (radix+1)]
                     
        for card in cards:  
            try:
                index = int ( card [1])
                buckets [index].append(card)
            except:
                index = cardvalstr.index(card [1])
                buckets [index].append(card)
                        
        
        result = []
        
        for bucket in buckets:
              result +=bucket
        print (result)
    
    print (result)
       
uk1_radix_sort(cards) 


def uk2_message_decode (stringinput):
    
    stack = []
    
    for chr in stringinput:
        if chr == ' ':
            pass
        elif chr =='*':
            stack.pop()
        else:
            stack.append(chr)
        print (stack)
    
     
#uk2_message_decode("T E * A * Q Y S * * * S E U * * * * N I * O * * ")

def uk3_flood_fill(x, y, switch):
    m=[
[0,0,1,0,0,1,0,0,0,0],
[0,0,1,0,0,1,0,0,0,0],
[0,0,1,1,0,1,0,0,0,1],
[0,0,1,0,0,0,1,0,1,0],
[0,0,1,0,0,0,0,1,0,0],
[0,0,1,1,0,1,0,0,0,0],
[0,0,1,0,1,1,1,1,0,0],
[0,0,1,0,0,1,0,1,1,1],
[0,0,1,0,0,1,0,0,0,0],
[0,0,1,0,0,1,0,0,0,0] ]
    
  
    def is_member (x, y):
        if x >= 0 and x < len(m) and y >= 0 and y < len(m[0]):
            return True
        return False
        
    array = []
    array.append([x,y])
    
    while (len(array) != 0):
        
        if switch == "stack":           
            point = array.pop(0)
        elif switch =="queue":
            point = array.pop()
    
        i = point[0]
        j= point [1]
        if m [i] [j] ==0:
            m[i][j] =2                
            
            if (is_member(i+1, j) and m [i+1] [j] ==0):
                array.append([i+1,j])
            if (is_member(i-1, j) and m [i-1] [j] ==0):
                array.append([i-1,j])
            if (is_member(i, j+1) and m [i] [j+1] ==0):
                array.append([i,j+1])
            if (is_member(i, j-1) and m [i] [j-1] ==0):
                array.append([i,j-1])
     
       
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in m:
            print (row)
        
        time.sleep(1)           
            
           
            
uk3_flood_fill(4, 4, "stack")  
uk3_flood_fill(4, 4, "queue")  
#uk3_flood_fill(9, 9)  
      
        
    
    