'''
Created on 3. 1. 2017

@author: stefk
'''

import sys

def getdistance(point1, point2):
    return (point2[0] - point1[0])**2 + (point1 [1]-point2 [1])**2


f = open ("a.txt", 'r')
#f= open (sys.argv[1], 'r')
points = []
for line in f:
    points.append ((float(line.split(" ") [0]), float(line.split(" ") [1])))

minimum = sys.maxsize
minimum2 = 0
index1 = index2 = 0
sumx = 0
sumy = 0

for i in range (len(points)):
    distancefrom = getdistance((0,0), points[i])
    sumx += points[i] [0]
    sumy += points [i] [1]
    
    if distancefrom > minimum2:
        minimum2 = distancefrom
        point = points [i]
        
    for j in range (i+1, len(points)):
        distance = getdistance(points[i], points[j])
        
        if distance < minimum:
            minimum = distance
            index1, index2 =i,j
          
        
print (point [0]," ",point [1])     
print (index1, " ", index2)
print (sumx/len(points), " ", sumy/len(points))

    