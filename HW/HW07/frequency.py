
import sys

def readInput():
    "GET just the words from input"
    source = []
   # f = open("text.txt", 'r')
    f= open (sys.argv [1], 'r')

    for line in f:
        word = []
        for i in range (len(line)):

            if (ord(line [i]) >= 97 and ord(line [i]) <= 122):
                word.append(line [i])
            elif (ord(line [i]) >= 65 and ord(line [i]) <= 90):
                word.append(chr (ord (line [i]) + ord ('a')-ord('A')))
            elif (len(word) != 0):
                source.append(word)
                word = []
    return source


def getMaxLength (array):
    maxlength =0
    for string in array:
        if len(string)> maxlength:
            maxlength = len(string)
    return maxlength

def getbucket(word, itteration):
    "Help function that returns the position of bucket in which the string will be added"
    if (itteration+1 > len(word)):
        return 0
    else:
        return (ord (word [itteration])-ord('a')+1)


def radixsort(source, k):
    "SORTING ALGORITHM for string"

    RADIX = 27
    for iterration in range (k-1, -1,-1):

        # declare and initialize buckets
        buckets = [list() for _ in range(RADIX)]

        # split source between lists according to k charackter
        for word in source:
            bucketindex = getbucket(word, iterration)
            buckets[bucketindex].append(word)

        # empty lists into source array
        i = 0
        for bucket in buckets:
            for word in bucket:
                source[i] = word
                i += 1

    return source


def createHistogram(source):
    "MAKING an OUTPUT"

    preffix = 14
    starcount =50

    output = []
    density = []
    maxdensity = 1

    if (len(source) >0):
        output.append(source [0])
        density.append(1)
        previousword = source[0]

    for i in range (1,len(source)):
        if (source [i] == previousword):
            density [len(density)-1] +=1
            if density [len(density)-1]> maxdensity:
                maxdensity = density [len(density)-1]
        else:
            output.append(source [i])
            density.append(1)
            previousword = source[i]

    #printing the output
    for i in range (len(output)):
        print((preffix -len(output [i])) * ' ', end="")
        for chr in output [i]:
            print(chr, end="")
        print(":", end="")
        count = starcount*density [i]//maxdensity
        if count > starcount:
            count =starcount
        print (count * '*')


#array = ["aa", "aba", "caa", "ba", "bd", "ba", "bs", "ba", "cac", "a", "c", "ya", "z","fafdsfsdfsdafsda", "aa", "ba"]
array = readInput()
#print(radixsort(array,getMaxLength(array)))
createHistogram(radixsort(array,getMaxLength(array)))


