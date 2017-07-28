
array =[]
histogram =[]
import sys

def readInput ():

    first =True
    #f = open ("rectangle.txt", 'r')
    f=open (sys.argv[1],'r')
    for line in f:
        row = list (map(int, line.split()))

        array.append(row)

        if (first):
            hisrow =[1]* len(array[0])
            histogram.append(hisrow)
            first =False
        else:
            hisrow = list()
            for i in range(len(row)):
                if (row[i] == array[len(array) - 2][i]):
                    hisrow.append(histogram[len(histogram)- 1][i] + 1)
                else:
                    hisrow.append(1)
            histogram.append(hisrow)



    #if the stack is not emptz AND pop index is smaller than itterate index


def calculatelargest(input, currentmaxsizes, row, column):

    stack = []
    i =0
    while (i< len(input)):
        value = input [i]
        #if stack is empty or the iterrate element is bigger or equal to top of stack
        if (len (stack) ==0 or value >= input [stack [len(stack) -1]]):
            stack.append(i)
            i+=1
            #print("appended")
            #print(stack)
        else:
            top = stack.pop()
            heigh = input [top]

            if (len(stack) != 0):
                width = i - stack[len(stack)-1] - 1
                area = heigh * width
            else:
                width =i
                area = input[top] * width

                # check weather is the area bigger or not
            #print("area: %d heigh: %d width: %d column: %d row: %d" % (area, heigh,width,column -len(input) +i-1, row))
            if (area > currentmaxsizes[4]):
                #print("column: %d i: %d delka %d"%(column,i, len(input)))
                currentmaxsizes [0]= column -len(input) +i
                currentmaxsizes [1] = row
                currentmaxsizes [2] = heigh
                currentmaxsizes [3] = width
                currentmaxsizes [4]  =area

    while (len(stack) != 0):

        top = stack.pop()
        heigh = input[top]

        if (len(stack) != 0):
            width = i - stack[len(stack) - 1] - 1
            area = heigh * width
        else:
            width = i
            area = input[top] * width
        # check weather is the area bigger or not
        #print("area: %d heigh: %d width: %d column: %d row: %d" % (area, heigh, width, column - len(input) + i - 1, row))
        if (area > currentmaxsizes[4]):
            #print("column: %d i: %d delka %d" % (column, i, len(input)))
            currentmaxsizes[0] = column - len(input) + i
            currentmaxsizes[1] = row
            currentmaxsizes[2] = heigh
            currentmaxsizes[3] = width
            currentmaxsizes[4] = area
    return currentmaxsizes

#sizes =calculatelargest([3,2,1],0)
#print("maxarea is: %d"%sizes [3])

def andnowdothemagic ():

    #row column heigh, width, area
    maxsizes = [0,0,0,0,0]

    for i in range(len(array)):

        follow = array[0] [0]
        hisinput = []
        for j in range (len(array[i])):
            if (array [i] [j] ==follow):
                hisinput.append(histogram [i] [j])
            else:

                if (len(hisinput) > 1):
                    #print("hisinput: ",end="")
                    #print(hisinput)
                    maxsizes = calculatelargest(hisinput, maxsizes, i,j-1)


                hisinput.clear()
                follow = array[i][j]
                hisinput.append(histogram [i] [j])

        maxsizes = calculatelargest(hisinput, maxsizes, i,j)


    print("%d %d" % (maxsizes[1]-maxsizes[2]+1, maxsizes[0]-maxsizes[3]+1))
    print ("%d %d" %(maxsizes[1], maxsizes[0]))
    #for i in maxsizes:
        #print(i)




readInput()
"""for row in histogram:
    print(row)"""

andnowdothemagic()
