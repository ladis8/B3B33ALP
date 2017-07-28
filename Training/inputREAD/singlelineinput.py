import sys
import math
import numpy

#smerodatna odchylka
a = [1,2,3]
print(numpy.mean (a))
numpy.average



#singlerowinput
def readinput(path):
    f = open (path, 'r')
    line = f.readline().rstrip()
    #integer input
    inp = list (map(int, line.split()))
    #not integer input
    #inp = list (line.split())
    return inp

#multiplerowinput to 1D array
def readinput3(path):
    f = open (path, 'r')
    inp = []
    for line in f:
        line = line.rstrip()
        # integer input
        inp.append(int (line))
        #inp.append(list(line.split()))
    return inp

#multiplerowinput to 2D array
def readinput2(path):
    f = open (path, 'r')
    inp = list ()
    for line in f:
        line = line.rstrip()
        # integer input
        inp.append(list (map (int, line.split())))
        #inp.append(list(line.split()))
    return inp

print(max(readinput2("text.txt")[2]))