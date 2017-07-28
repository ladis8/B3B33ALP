import sys
base = []
sample = []


def readInput ():


    f = open (sys.argv [1] , 'r')
    for line in f:
        row = list (map(int, line.split()))
        base.append(row)

    f = open (sys.argv [2] , 'r')
    for line in f:
        row = list (map(int, line.split()))
        sample.append(row)


def findsubmatrix ():

    minsum = sys.maxsize
    edge = [0,0]
    if (len (sample) > len(base) or len(sample[0]) > len(base [0])):
        print("-1 -1")
    else:
        for i in range (len(base)-len (sample)+1):
            for j in range (len(base[0])- len(sample[0])+1):
                    sum =0
                    for k in range (len(sample)):
                        for l in range (len(sample[0])):
                            sum += abs(sample [k] [l] - base [i+k] [j+l])

                    if (sum < minsum):
                        minsum = sum
                        edge [0] =i
                        edge [1] =j

        print("%d %d" %(edge [0],edge[1]))


readInput()
findsubmatrix()