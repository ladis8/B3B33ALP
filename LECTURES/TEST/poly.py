import sys

def readinput1(path):
    f = open (path, 'r')
    koef = map (float, f.readline().split())

    return list (koef)

def readinput2(path):
    try:
        f = open(path, 'r')
        inp = []
        for line in f:
            line = line.rstrip()
            # integer input
            inp.append(float(line))
            # inp.append(list(line.split()))
        return inp
        # print (minnumberlimited(int(line)))
    except (Exception):
        return "ERROR"


def derivate (koef):
    newkoef= []

    for i in range (1, len(koef)):
        newkoef.append(i * koef[i])
    return newkoef



def countderivation (numbers, koef):
    minimum = sys.maxsize
    mini = -1
    for index,num in enumerate(numbers):
        d=0
        for i in range(len(koef)):
            d +=koef[i] * num**i
        if d < minimum:
            minimum=d
            mini = index
    return mini


polynom = readinput1(sys.argv[1])
num = readinput2(sys.argv[2])

if num == "ERROR":
    print("ERROR")
else:
    koef = derivate(polynom)
    for i in koef:
        print(i, end=" ")
    print()
    print(countderivation(num,polynom))
