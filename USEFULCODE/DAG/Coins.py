coins = [50,25,10,5,1]
supply =[ 2, 1, 2,4,2]
import sys
from sys import stdin
maximum = 7490

def init ():
    #table = initializemintablelimited()
    table =initializealltable()
    print (table)
    for line in stdin:
        try:
            print (findcombinations(int(line), table))
            #print (minnumberlimited(int(line)))
        except EOFError:
            break





""""FIND THE MINIMUM NUMBER OF COINS TO PAY A GIVEN VALUE"""
def initializemintable():
        coins.reverse()
        table = [i for i in range(0, maximum)]
        for i in range(1, len(coins)):
            coin = coins[i]
            table[coin] = 1
            for j in range(coin + 1, maximum):
                table[j] = min(table[j], table[j - coin] + 1)
        #print(table)
        return table

""""FIND THE MINIMUM NUMBER OF COINS TO PAY A GIVEN VALUE RECURSIVELY"""
dagtable = [None] * maximum
for coin in coins:
    dagtable [coin] = 1

dagtable [0] = 0
def minnumber (x):
    def count (x):
        if dagtable [x]:
            return dagtable [x]
        minimum = sys.maxsize
        for coin in coins:
            if x-coin >= 0:
                minimum = min (minimum, count(x-coin)+1)
                dagtable [x] = minimum
        return minimum

    return dagtable [x] if dagtable[x] is not None else count(x)



""""FIND THE MINIMUM NUMBER OF COINS TO PAY A GIVEN VALUE WITH LIMITED SUPPLY"""
def initializemintablelimited():
    table = [sys.maxsize] * maximum
    table [0] =0
    coins.reverse()
    supply.reverse()
    partialsum = 0
    for i in range(len(coins)):
        print(partialsum)
        partialsum =(coins[i]* supply[i])+partialsum if partialsum<=maximum else partialsum

        for j in range (coins[i], partialsum+1):
            table[j] = min (table[j], table [j-coins [i]]+1)
    return table






""""FIND THE MAXIMUM NUMBER OF COMBINATIONS TO PAY A GIVEN VALUE"""
def initializealltable():
    coins.reverse()
    table = [0 for _ in range (0,maximum)]
    for i in range(0, len(coins)):
        coin = coins[i]
        table[coin] +=1
        for j in range(coin + 1, maximum):
            table[j] = table [j] + table[j-coin]
    return table



def findcombinations (x, table):
    return table [x]
init()