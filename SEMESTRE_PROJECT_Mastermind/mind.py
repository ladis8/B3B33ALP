import sys
import time


class mind:

    def __init__(self):
        pass


    #init function for initializing the game
    def init (self, glob, count):
        self.n = count
        self.k = glob
        #creates a set of allguesses - set is better for removing operations than array
        self.allguess = self.generateallposibleguesses()
        #creates a set of all possible guesses
        self.possibleguess = self.allguess.copy()
        #take the initial guess - the first guess should remove most possibilities
        self.initialguess = (1,1,2,2) if self.n==4 else ((1,1,1,2,2) if self.n==5 else (1,1,2,2,3,3))
        self.first = True
        self.second = True
        self.third = True

        #all possible evaluations for particular play
        #precounted second guesses that should reduce most possiblitis for every evaluation of the inital guess
        self.EVALUATIONS1 = [
            (0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
            (1, 0), (1, 1), (1, 2), (1, 3),
            (2, 0), (2, 1), (2, 2),
            (3, 0), (4, 0)
        ]
        self.secondguess4 = [
            (0, 0, 3, 0),(2, 0, 5, 5),(2, 0, 0, 1),(4, 3, 1, 1), (2, 2, 1, 1),
            (3, 3, 5, 2),(1, 1, 0, 3),(3, 2, 1, 2),(1, 1, 2, 2),
            (0, 4, 1, 2),(2, 1, 5, 2),(1, 2, 2, 1),
            (1, 2, 2, 4),(1, 1, 2, 2)
        ]

        self.EVALUATIONS2 = [
            (0, 0),(0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
            (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
            (2, 0), (2, 1), (2, 2), (2, 3),
            (3, 0), (3, 1), (3, 2),
            (4, 0), (5, 0)
        ]
        self.secondguess5 = [
            (5, 6, 5, 4, 6), (0, 0, 2, 6, 5), (5, 1, 5, 0, 1), (2, 2, 6, 1, 4), (5, 2, 3, 4, 3),(4, 3, 0, 1, 5),
            (1, 5, 5, 0, 6), (2, 5, 3, 5, 2), (2, 1, 2, 2, 2), (2, 2, 1, 5, 1), (2, 1, 6, 1, 4),
            (4, 1, 4, 5, 5), (2, 2, 1, 0, 2), (1, 2, 1, 5, 1), (4, 3, 0, 1, 5),
            (1, 1, 1, 5, 0), (1, 1, 6, 2, 1), (2, 1, 1, 2, 1),
            (1, 3, 1, 1, 6), (1, 1, 1, 2, 1)]

        self.EVALUATIONS3 = [
            (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
            (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
            (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
            (3, 0), (3, 1), (3, 2), (3, 3),
            (4, 0), (4, 1), (4, 2),
            (5, 0), (6, 0)
        ]
        self.secondguess6 = [
            (3, 0, 0, 3, 7, 0),(5, 4, 2, 5, 6, 6),(3, 2, 3, 1, 0, 0),(5, 2, 0, 1, 1, 4),(1, 1, 2, 4, 1, 3),(2, 0, 2, 1, 4, 7),(2, 2, 2, 1, 1, 1),
            (1, 4, 3, 5, 3, 5),(1, 4, 4, 1, 6, 6),(5, 4, 2, 4, 2, 2),(2, 1, 1, 1, 1, 0),(1, 1, 2, 4, 1, 3),(0, 2, 2, 0, 2, 3),
            (3, 1, 5, 3, 2, 5), (0, 2, 2, 0, 2, 3), (1, 2, 2, 6, 2, 4),(1, 7, 2, 2, 1, 1),(1, 2, 0, 6, 3, 6),
            (5, 1, 3, 2, 4, 2),(1, 3, 1, 1, 1, 2),(6, 1, 2, 1, 2, 2),(0, 2, 2, 0, 2, 3),
            (2, 1, 2, 3, 2, 0),(2, 1, 2, 3, 2, 0),(1, 2, 0, 6, 3, 6),
            (3, 1, 2, 2, 2, 7),(1, 1, 1, 2, 2, 2)
       ]

        self.thirdguess4 = [
            (4, 4, 4, 1), (5, 3, 4, 4), (3, 3, 4, 4), (0, 5, 5, 2), (0, 5, 5, 2), (5, 4, 5, 0), (0, 4, 4, 3), (0, 5, 5, 2), (0, 5, 5, 2), (3, 3, 4, 4), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2),
            (4, 2, 5, 5), (3, 5, 4, 1), (5, 5, 1, 0), (0, 5, 5, 2), (0, 5, 5, 2), (0, 4, 5, 1), (2, 0, 0, 4), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 3), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2),
            (4, 2, 1, 4), (4, 2, 1, 4), (3, 3, 4, 4), (0, 5, 5, 2), (0, 5, 5, 2), (4, 3, 1, 1), (2, 3, 5, 1), (2, 5, 1, 3), (0, 5, 5, 2), (0, 5, 1, 1), (0, 2, 2, 4), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2),
            (4, 3, 1, 1), (4, 2, 1, 1), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2), (2, 2, 1, 3), (4, 2, 5, 5), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2),

(2, 2, 1, 1), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2), (2, 2, 1, 1), (0, 5, 5, 2), (0, 5, 5, 2),

(1, 5, 4, 4), (0, 1, 3, 4), (0, 1, 4, 4), (3, 1, 5, 3), (0, 5, 5, 2), (0, 1, 5, 5), (0, 1, 5, 4), (0, 5, 5, 2), (0, 5, 5, 2), (0, 3, 5, 3), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2),

(5, 1, 4, 1), (3, 1, 1, 0), (4, 3, 1, 1), (1, 2, 2, 4), (0, 5, 5, 2), (1, 3, 4, 1), (5, 1, 4, 1), (1, 4, 3, 2), (0, 5, 5, 2), (4, 3, 1, 1), (3, 5, 0, 2), (0, 5, 5, 2), (4, 0, 2, 5), (0, 5, 5, 2),

(4, 2, 1, 2), (4, 2, 1, 2), (4, 2, 1, 2), (0, 5, 5, 2), (0, 5, 5, 2), (0, 2, 2, 2), (2, 1, 1, 4), (0, 2, 2, 4), (0, 5, 5, 2), (3, 2, 2, 2), (3, 1, 2, 0), (0, 5, 5, 2), (1, 2, 1, 4), (0, 5, 5, 2),

(0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2),

(2, 5, 5, 2), (3, 2, 2, 4), (1, 4, 4, 2), (0, 2, 2, 4), (0, 5, 5, 2), (2, 4, 2, 4), (0, 1, 5, 2), (1, 3, 0, 2), (0, 5, 5, 2), (0, 3, 5, 3), (3, 1, 2, 0), (0, 5, 5, 2), (0, 5, 5, 2), (0, 5, 5, 2),

(1, 2, 2, 4), (1, 2, 2, 4), (1, 2, 2, 4), (0, 5, 5, 2), (0, 5, 5, 2), (2, 1, 0, 2), (1, 5, 2, 1), (2, 1, 0, 4), (0, 5, 5, 2), (1, 5, 1, 2), (3, 1, 2, 0), (0, 5, 5, 2), (3, 1, 2, 0), (0, 5, 5, 2),

(1, 2, 2, 4), (1, 2, 1, 2), (1, 2, 1, 2), (0, 5, 5, 2), (0, 5, 5, 2), (1, 2, 1, 2), (1, 2, 2, 4), (1, 2, 2, 1), (0, 5, 5, 2), (1, 2, 1, 2), (2, 1, 2, 1), (2, 1, 2, 1), (1, 2, 2, 1), (0, 5, 5, 2),

(2, 2, 4, 2), (0, 2, 2, 4), (1, 2, 2, 4), (1, 1, 4, 2), (0, 5, 5, 2), (4, 1, 0, 0), (1, 3, 2, 2), (5, 1, 4, 1), (0, 5, 5, 2), (1, 1, 1, 2), (3, 1, 2, 0), (0, 5, 5, 2), (1, 2, 2, 2), (0, 5, 5, 2),

(1, 1, 2, 2), (1, 1, 2, 2), (1, 1, 2, 2), (0, 5, 5, 2), (1, 1, 2, 2), (1, 1, 2, 2), (0, 5, 5, 2), (1, 1, 2, 2), (0, 5, 5, 2), (0, 5, 5, 2), (1, 1, 2, 2), (1, 1, 2, 2), (0, 5, 5, 2), (1, 1, 2, 2),
]
        #take evaluations and secondguess for particular play
        self.EVALUATIONS = self.EVALUATIONS1 if self.n == 4 else (self.EVALUATIONS2 if self.n == 5 else self.EVALUATIONS3)
        self.secondguess = self.secondguess4 if self.n == 4 else (self.secondguess5 if self.n == 5 else self.secondguess6)
        self.black = 0
        self.white = 0
        self.firstblack = 0
        self.firstwhite = 0


    def guess (self):
        """function that returns the guess, initial and second guess are given,
        for the next guesses Knuth Algorithm and the worst case scenario is used"""


        if  len(self.possibleguess)==1:
            return self.possibleguess.pop()

        elif self.first:
            guess = self.initialguess
            self.first = False
            return guess
        elif self.second:
            self.second = False
            return self.secondguess [self.EVALUATIONS.index((self.black,self.white))]
        elif self.third:
            self.third = False
            a = self.EVALUATIONS.index((self.firstblack, self.firstwhite))
            b = self.EVALUATIONS.index((self.black, self.white))
            return self.thirdguess4 [a*len(self.EVALUATIONS) +b]
        else:
            guess= self.getbestguess()
            return guess

    def eval (self, g , black, white,):
        """function that save the master evaluation and removes guesses that are not possible """
        self.black = black
        self.white = white

        if self.second:
            self.firstblack = black
            self.firstwhite=white
        self.removenotpossible(black, white, g)
        #print (len(self.possibleguess))



    def score (self, guess, guessed, black, white):
        """my very basic implementation of score function that returns True weather one guess has same evaluation as another guess
        I tried more implementations with Python built-in functions, but this one is fastest"""

        #at first compares black
        blackcounter = 0
        temp1 = list(guess) #creates list - I use immutable tuples for guesses
        temp2 = list(guessed)

        for i in range(self.n):
            if guess[i] == guessed[i]:
                blackcounter += 1
                temp1[i] = -1 #use not possible value for place that was already counted as a black position
                temp2[i] = -1

        #if test does not pass in black colours, it skips counting white
        if blackcounter == black:
            whitecounter = 0
            for i in range(self.n):
                if temp1[i] != -1 and temp1[i] in temp2:
                    whitecounter += 1
                    temp2[temp2.index(temp1[i])] = -1

            if whitecounter == white:
                return True
        return False



    def removenotpossible(self, black, white, guessed):

        newpossible = set()

        for guess in self.possibleguess:
            if self.score(guess, guessed, black, white):
                newpossible.add(guess)
        self.possibleguess = newpossible

        print(len(self.possibleguess))




    def getbestguess(self):
        """ pick one guess - according to minMax - guess that removes most possiblities"""

        #calculate the minimum of possible guesses that would remain in our set
        minremained = sys.maxsize
        start = time.time()


        for guess in self.allguess: #it could be guess among all guesses  - not necesseirly possible guess

            #reduce time for counting - due to entropy of the problem, it finds guess that removes most possibilities quickly,
            #other guesses could remove the same number of possibilites but we don't need them
            if time.time() - start > 900:
               break

            # calculate the maximum of possible guesses that would remain in all evaluations in the worst scenario
            currentmax = 0

            for eval in self.EVALUATIONS:

                remainded = len(self.possibleguess)

                # take all guesses in possible guess
                for guess2 in self.possibleguess:
                    if not self.score(guess, guess2, eval[0], eval[1]): #pretends that the guess in possible guesses is the right one
                        remainded-=1
                    if remainded == currentmax: # if already found worse evaluation breaks
                        break

                if  remainded > currentmax:
                    currentmax = remainded
                    if currentmax > minremained: #if already found better guess breaks
                         break

            if currentmax <=  minremained:
                if currentmax == minremained:
                    if bestguess not in self.possibleguess and guess in self.possibleguess: #primairly take guess in possible guesses
                        bestguess = guess
                else:
                    #print("minremainded update",currentmax)
                    minremained = currentmax
                    bestguess = guess

        #print("minremained: ",minremained)
        return bestguess


    def generateallposibleguesses(self):
        "This function generates n-tuples from k elements"
        S = set()

        def _generate(t, depth):
            nonlocal S
            if depth < self.n:
                for i in range(self.k):
                    t[depth] = i
                    _generate(t, depth + 1)
            else:
                S.add(tuple(t))

        _generate([0 for _ in range(self.n)], 0)
        return S



EVALUATIONS1 = [
            (0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
            (1, 0), (1, 1), (1, 2), (1, 3),
            (2, 0), (2, 1), (2, 2),
            (3, 0), (4, 0)
        ]


EVALUATIONS2 = [
            (0, 0),(0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
            (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
            (2, 0), (2, 1), (2, 2), (2, 3),
            (3, 0), (3, 1), (3, 2),
            (4, 0), (5, 0)
        ]

EVALUATIONS3 = [
            (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
            (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
            (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
            (3, 0), (3, 1), (3, 2), (3, 3),
            (4, 0), (4, 1), (4, 2),
            (5, 0), (6, 0)
        ]
f = open ("out.txt", 'w')

""""for eval in EVALUATIONS1:
    f.write("for evaluation: " + str(eval))
    f.write('\n')
    print(eval)
    for eval2 in EVALUATIONS1:
        m = mind()
        m.init(6, 4)
        start = time.time()
        m.removenotpossible(eval[0], eval[1], (1, 1, 2, 2))
        print(eval2)
        print(m.secondguess4[EVALUATIONS1.index(eval2)])
        m.removenotpossible(eval2[0], eval2[1], m.secondguess4[EVALUATIONS1.index(eval2)])
        a =m.getbestguess()
        print(a)
        f.write(str(a)+", ")
        end = time.time()
        print ("Time", end-start)
    f.write('\n')"""""



