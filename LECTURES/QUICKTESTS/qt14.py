import sys

name1= sys.argv [1]
name2= sys.argv [2]
#name1 = "notdecoded.txt"
#name2= "decoded.txt"


def readinput (name1, name2):
    f1 = open (name1, 'r')
    f2 = open (name2, 'r')
    dict =[]
    decoded = []

    for line in f1:
        line = line.rstrip('\n').lower()
        dict.extend(line.split(" "))

    for line in f2:
        line= line.rstrip('\n').lower()
        decoded.append(line.split(" "))

    return dict,decoded


def tryCaesar(dict, decoded, posun):
   # print(decoded)

    for word in decoded:
        encoded = []
        #print(word)
        for char in word:
            if ord (char) + posun >122:
                newasci = 96 +(ord(char)+posun-122)
            else:
                newasci = ord (char) + posun
            encoded.append(chr (newasci))
        encoded = "".join(encoded)
        if not encoded in dict:

            return False
    return True



def doCeasar (dict, decoded):

    firstword = decoded [0]
    #print(firstword)

    for word in dict:
        if len(word) == len(firstword):
            posun = ord (word[0])- ord(firstword[0])
            if posun <0:
                posun = 26+posun
            #print(posun)
            if (tryCaesar (dict, decoded, posun)):
                print(posun)



dict=readinput(name1,name2)[0]
decodedlines = readinput(name1,name2)[1]
for i in range (len(decodedlines)):
    doCeasar(dict, decodedlines[i])



