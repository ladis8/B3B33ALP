'''
Created on 13. 12. 2016

@author: stefk
'''
class heap ():
    
    heap =[]
    
    def __init__ (self, source):
        self.heap = source
    
    def getChildren (self, index):
        
        return [2* index +1, 2* index+2]
    
    def getParent (self, index):
        return (index-1)//2
    
    
    def top (self):
        n = len(self.heap)
        if  n==0:
            return
        if n==1:
            return self.heap.pop()
        
        top = self.heap[0]
        self.heap [0] = self.heap.pop()
        index =0
        
        children = self.heap.getchildren()
        child = children[0]
        
        if children [1] < len(self.heap) and self.heap [children [1]] < self.heap [children [0]]:
            child = children[1] #it is right
        
       # if (self.heap [child] < self.heap [index])
        
            
        
    
    def addnum (self, num):
    
    
        index = len(self.heap)

        self.heap.append(num)
        
        parent = self.getParent(index)
        
        print (self.heap[parent])   
        while index >0 and self.heap [parent] > num:      
            self.heap [index]= self.heap [parent]
            self.heap [parent] = num
            index = parent
            parent = self.getChildren(index)
            print (parent)

a = [1,2,3,4]
c = [i for i in range (10)]
print (c)

h = heap (a)
h.addnum (1)
print (h.heap)



"""--------------------ROMANNUMBERS-------------------CV11"""
conv = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
romannumber = "MCMXCIX"
romannumber = "MMMDCXCIX"

def romannumerconventor(romannumber):
    romannumber = list(reversed(romannumber))
    print(list(romannumber))
    i = 1
    sum = conv.get(romannumber[0])
    previousnumber = sum
    while i < len(romannumber):
        num = conv.get(romannumber[i])
        if num >= previousnumber:
            previousnumber = num
            sum += num
            i += 1
        else:
            j = i
            minus = 0
            while j < len(romannumber) and conv.get(romannumber[j]) < previousnumber:
                minus += conv.get(romannumber[j])
                j += 1
            sum -= minus
            i = j
    print(sum)


romannumerconventor(romannumber)