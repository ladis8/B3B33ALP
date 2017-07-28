'''
Created on 11. 11. 2016

@author: stefk
'''

import sys


sys.path.append(r"C:\\Users\stefk\Desktop\IdeaProjects\CVIKO\USEFULCODE")
import strings  

str =["aa","a", "ba", "ca", "db"]
s = sorted(str)
print(s )




array = [3,4,6,5,8,5,45,41,55,66,8789,5,5,6]

def bubble_sort (array):
    "BUBBLE SORT O (n^2)"
    
    n =len(array)
    for i in range (n-1):
        for j in range (0,n-i-1):           
            if (array [j] < array [j+1]):
                temp = array [j]
                array [j] = array [j+1]
                array [j+1] = temp 
    return array    
        
print (bubble_sort(array))

def insertion_sort (array):
    "INSERTION SORT O (n^2)"
    n =len(array)
    
    for i in range (1,n):
        j=i
        val = array [i]
        
        while (array [j-1] < val and j >0):                         
            array [j] = array [j-1]
            j-=1
        array [j] = val
        
    return (array)
                
print (insertion_sort(array)) 

def selection_sort (array):
    "SELECTION SORT O (n^2)"
    n= len(array)
    for i in range (n-2):
        maxi = i
        for j in range (i+1,n):            
            if (array[maxi] > array [j]):
                maxi = j
        temp = array [maxi]
        array [maxi] = array [i]
        array [i] = temp  
    return (array)
                
print (selection_sort(array))    




def merge_sort(array):
    "MERGE SORT (n logn)"
    def join_arrays(left,right):

        result=[] # 
        i=0 # index do left
        j=0 # index do right
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                result+=[left[i]]
                i+=1
            else:
                result+=[right[j]]
                j+=1
        result+=left[i:] # doplnit zbytky
        result+=right[j:]
        return result
    
    #merge sort starts
    if len(array)<=1: 
        return array
    mid=len(array)//2 #get the middle index
    print (mid)
    left=merge_sort(array[:mid]) #do merge for left half
    right=merge_sort(array[mid:])#do merge sort for right half
    return join_arrays(left,right)#merge arrays
#print (merge_sort([5,6,1,4,3,2])) 



def mergesortQUEUE (array):

   def mergesort (queue):

       if len(queue) <=1:
           return array
       m = len(queue)//2
       left = []
       for i in range(m):
            left.append(queue.pop(0))
       left = mergesort(left)
       right = mergesort(queue)
       return join_queues (left, right)

   def join_queues (left, right):
       result = []
       while not len(left) == 0 and not len(right) ==0:
           result.append(left.pop(0)) if left [0] < right[0] else result.append(right.pop(0))

       while not len(left) ==0:
           result.append(left.pop(0))
       while not len (right) == 0:
           result.append(right.pop(0))
       return result


   return  mergesort(array)
print("MERGE SORT WITH QUEUES")
print(mergesortQUEUE([30,26,93,17,77,31,14,55,20]))








def quick_sort (array):
    result = []
    #print (array)
    if len(array) <= 1:
        return array
    else:
        pivot = array [0]
        index =1
        lpart = list()
        rpart = list()        
        while (index < len(array) ):
            if array [index ] < pivot:
                lpart.append(array [index])
            else:
                rpart.append(array [index])
            
            index+=1
        #print(lpart)
        #print(rpart)
     
       
    result += quick_sort(lpart)  
    result +=  [pivot ]    
    result += quick_sort(rpart)
    return result

print (quick_sort(array)) 

def quick_sort2 (array, first, last):
    
    def castecnesetrideni(array, first, right):
        pivot = array [first]
        left = first +1
        print ("first",first, "right", right)
        
        while True:
            
            print (right)
            while (left <= right and array [left] <= pivot):
                left +=1
                
            while (left <= right and array [right] >= pivot):
                right -=1
            
            #prohozeni pivota 
            if (left > right):
                temp = array [right]
                array [right] = array [first]
                array [first] = temp
                return right
            
            temp = array [right]
            array [right] = array [left]
            array [left] = temp
            
    if (first < last):
        boundry = castecnesetrideni(array, first, last)
        quick_sort2(array, first, boundry-1)
        print (array)
        quick_sort2(array, boundry+1, last) 
        print (array)
    
    return array       
                
print (quick_sort2([30,26,93,17,77,31,14,55,20], 0, 8))


def quicksortSTACK (array):

    def partioning (first, last):
        nonlocal  array
        pivot = array [first]
        right = last
        left = first+1

        while True:
            while left <= right and array [left] <= pivot:
                left+=1
            while left<= right and array [right] >= pivot:
                right -=1
            if left > right:
                array [first], array [right] = array[right], array[first]
                return right
            else:
                array [left], array [right] = array[right] , array[left]

    stack = []
    stack.append ((0, len(array)-1))

    while len(stack):
        (first,last) = stack.pop()
        boundry = partioning(first, last)
        #print(array)
        if first < boundry:
            stack.append((first, boundry-1))
        if last > boundry:
            stack.append((boundry+1,last))

    print(array)
quicksortSTACK([5, 1, 7, 6, 4, 3])
