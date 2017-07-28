import sys
import numpy
import random



""""domaci ukol cviceni 3"""
def delitelnost (k):
    def gcd (m, n):
        while n is not 0:
            t = n
            n = m %n
            m = t
        return m

    for i in range (1,k+1):
        for j in range (1, k+1):
           if gcd (i,j) ==1 :
               print('.', end= "")
           else:
               print('x', end = "")
        print()

#delitelnost (10)

"""""domaci ukol cviceni 4"""

def readinput(path):
    f = open (path, 'r')
    inp = []
    for line in f:
        line = line.rstrip()
        inp.append(int (line))
    return inp

def findvalue(array, value):

    def findinner (a, b, depth):
        if a > b:
            return False
        c = (a+b)//2
        if array [c] == value:
            return True, depth
        elif value < array [c]:
            return findinner(a, c-1, depth+1)
        elif value > array [c]:
            return findinner(c+1, b, depth+1)
    return findinner(0, len(array)-1,0)

#print(findvalue(readinput("array.txt"),  8834497))



"""""domaci ukol cviceni 5"""
def readinput2(path):
    f = open (path, 'r')
    inp = list ()
    for line in f:
        line = line.rstrip()
        inp.append(list (map (lambda x : float(x), line.split())))
    return inp

def isThereSaddle(matrix):
    minimumrow = []
    maximumrow = []
    minimumcolumn = []
    maximumcolumn=[]
    for row in matrix:
        minimumrow.append(min(row))
        maximumrow.append(max(row))
    matrix = numpy.transpose(matrix)

    for row in matrix:
        minimumcolumn.append(min(row))
        maximumcolumn.append(max(row))

    for row,number in enumerate (maximumrow):
        for column, number2 in enumerate(minimumcolumn):
            if number == number2:
                print (row, column, number)

    for row,number in enumerate (minimumrow):
        for column, number2 in enumerate(maximumcolumn):
            if number == number2:
                print (row, column, number)

#isThereSaddle(readinput2("matrix.txt"))

"""""domaci ukol cviceni 5"""
def readinput3(path):
    f = open (path, 'r')
    inp = list ()
    for line in f:
        line = line.rstrip()
        inp.append(list (map (lambda x : int(x), line.split())))
    return inp


def getabsofsmallone(path):
    f = open (path, 'r')
    sum =m=n=0
    for line in f:
        m+=1
        for index,number in enumerate(line.split()):
            sum+=abs (int(number))
        n = index
    return m,n+1,sum

#print (getabsofsmallone("small.txt"))

def findthesame (m, n, value, array):

    def count (i, j):
        sum = 0
        for x in range (i, i+n):
            for y in range (j, j + m):
                sum+= abs (array [x] [y])
        return sum


    minimum = sys.maxsize
    outx =outy=0
    for i in range (len(array)):
        if i+n < len(array):
            for j in range(len(array[0])):
                if j+m <len(array[0]):
                    if abs (count(i, j) - value) < minimum:
                        minimum = count(i,j)
                        outx = i
                        outy = j
                else:
                    break
        else:
            break
    print(outx, " ", outy)

(m, n , sum) = getabsofsmallone("small.txt")
findthesame(m ,n ,sum,readinput3("image.txt"))



""""CARDS COMPARISION"""
cards = [[0, 'Q'], [2, '6'], [1, 'K'],
         [1, '8'], [2, '10'], [2, '4'],
         [3, '4'], [0, '4'], [1, '3'],
         [2, '5'], [0, 'K'], [3, 'A'],
         [1, 'J'], [0, '3'], [0, '9']]

throws = {'J' : 11, 'Q' : 12, 'K' : 13, 'A' :14}


cards = sorted (sorted(list (map (lambda x : [x [0], throws [x [1]]] if x[1] in throws else [x [0], int (x[1])], cards)), key = lambda x : x[1]), key = lambda x :x[0])
print(cards)


""""determinant of matrix"""
def countdeterminant (matrix):

    def reducedmatrix (matrix, column):
        #print ( [matrix[i][:column] + matrix[i][column + 1:] for i in range(1, len(matrix))])
        return [ matrix [i][:column] + matrix [i][column+1:] for i in range (1, len(matrix))]

    def _determinant (matrix):
        if len(matrix [0]) ==1:
            return matrix [0][0]
        else:
            sum = 0
            for i in range(len(matrix [0])):
                sum+=(-1)**i * matrix [0][i] * _determinant(reducedmatrix(matrix, i))
            return sum

    return _determinant(matrix)
print(countdeterminant([[1, 2,3], [50,2, 4],[50,1,4]]))


""""Lagrange polynom"""

def lagrangepolynom (n, x):

    lagrangearray = [-1] * (n+1)
    lagrangearray[0] = 1.
    lagrangearray[1] = float(x)

    def _lagrange(n):
        nonlocal lagrangearray
        if lagrangearray[n] == -1:
            lagrangearray [n] = ((2 * n - 1) / n * x * _lagrange(n - 1)) - ((n - 1) / n * _lagrange(n - 2))
        return lagrangearray[n]

    return _lagrange(n)

print("%.1f" %lagrangepolynom(5, 2))


"""""DICE THROWING"""

def dicethrow (n):
    throws = {}
    for i in range (2,13):
        throws [i] = 0
    for i in range (n):
        throw = random.randrange(1,7)+random.randrange(1,7)
        throws[throw] +=1
    for throw in throws:
        throws [throw] /=n
    return  throws
print ("Dice throwing problem",dicethrow(100000))



""""COLLECTOR PROBLEM"""
def collectorproblem (n):
    set = {i for i in range (n)}
    counter = 0
    while len(set) > 0:
        counter+=1
        rand = random.randrange(n)
        if rand in set:
            set.remove(rand)
    return counter
print("Collector problem: ",collectorproblem(50))





















