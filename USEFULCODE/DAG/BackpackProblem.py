""""BAGPACK PROBLEM"""

def readinput ():
    line = input()
    S = int (line.split()[0])
    n = int (line.split()[1])
    weights = []
    prices = []

    for i in range (n):
        line = input().split()
        weights.append(int(line [0]))
        prices.append(int(line [1]))
    return S,weights, prices


def backpack (S, weights, prices):

    table = [[-1] *(S+1) for i in range (len(weights)+1)]

    #first row - 0. row
    table [0] [0] = 0
    #add things 1- n
    maximum = 0
    for i in range (len(weights)):
        w = weights[i]
        p = prices[i]
        for j in range (S):
            #add ith item for first time
            if table [i] [j] != -1:
                # neprida predmet
                if table[i + 1][j] < table[i][j]:
                    table[i + 1][j] = table[i][j]
                # prida predmet k ostatnim
                addedprice = table[i][j] + p
                if j + w <= S and table[i + 1][j + w] < addedprice:
                    table[i + 1][j + w] = addedprice
                    maximum = max(maximum, addedprice)
    return maximum

S, weights, prices = readinput()
print(backpack(S, weights, prices))


""""def backpack (S, weights, prices):

    table = [[0] *(S+1) for i in range (len(weights)+1)]

    #first row - 0. row
    table [0] [weights [0]] = prices [0]
    #add things 1- n
    maximum = 0
    for i in range (len(weights)-1):
        w = weights[i+1]
        p = prices[i+1]
        for j in range (S):
            #add ith item for first time
            if j== w and table [i+1] [w] < p:
                table [i+1] [w] = p
                maximum = max(maximum,p)

            if table [i] [j] != 0:

                #neprida predmet
                if table [i+1] [j] < table [i][j]:
                    table[i + 1][j] = table[i][j]
                #prida predmet k ostatnim
                addedprice = table [i] [j] + p
                if j+w <= S and table[i + 1][j+w] < addedprice :
                   table[i + 1][j+w] = addedprice
                   maximum = max(maximum,addedprice)
        #print(table)
    return maximum

S, weights, prices = readinput()
print(backpack(S, weights, prices))
"""""