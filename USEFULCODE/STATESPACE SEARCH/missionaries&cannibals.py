maxdepth = 25
people =0
boat = 0




def init ():
    global people,boat
    people = int (input ())
    boat = int (input())

    initstate = State (people, people, 0, 0 , 0, None,0)
    queue = []
    queue.append(initstate)
    explored = set()

    while len(queue) != 0:
        # print(stack)
        #print(queue)
        state = queue.pop(0)
        explored.add(state)

        if state.isGoal():
            print("SOLUTION")
            print(state.depth)
            path = []
            path.append(state)
            while state.parent:
                print(state.parent)
                path.append (state.parent)
                state = state.parent
            for p in path:
                print(p, end = " ")

            break

        if state.depth < maxdepth:
            for s in getSuccessors(state):
                # print(getnextstates(boatsize,state))
                #print(s)
                if s not in queue and s not in explored:
                    queue.append(s)

class State:
    def __init__(self,ml, cl, mr, cr, boat, parent, depth):
        self.cl = cl
        self.cr = cr
        self.ml = ml
        self.mr = mr
        self.boatplace = boat
        self. parent = parent
        self.depth = depth

    def isGoal (self):

        if self.cr ==people and self.mr ==people:
            return True
        else:
            return False

    def isValid (self):
        if (self.ml>= self.cl or self.ml == 0) and (self.mr >= self.cr or self.mr == 0):
            if self.ml != people or self.cl != people:
                return True
        else:
            return False
    def __eq__(self, other):

        return True if self.cr == other.cr and self.cl ==other.cl and self.mr == other.mr and self.ml == other.ml and self.boatplace ==other.boatplace else False
    def __str__(self):
        return "[%d, %d, %d, %d, %d]" %(self.ml, self.cl, self.mr, self.cr,self.boatplace)
    def __hash__(self):
        return hash((self.ml, self.cl, self.mr, self.cr))

def getSuccessors (state):
    children = []

    if state.boatplace ==0:
        filling = fillboat(state.ml, state.cl)
        for fill in filling:
            newstate = State (state.ml - fill[0], state.cl - fill[1], state.mr + fill[0], state.cr + fill[1], 1, state, state.depth +1)
            if newstate.isValid():
                children.append(newstate)

    elif state.boatplace == 1:
        filling = fillboat(state.mr, state.cr)
        for fill in filling:
            newstate = State(state.ml + fill[0], state.cl + fill[1], state.mr - fill[0], state.cr - fill[1], 0, state, state.depth+1)
            if newstate.isValid():
                children.append(newstate)
    return children


def fillboat(m,c):
    possiblenextstates = set()

    for i in range(m + 1):
        for j in range(c + 1):
            if i + j > boat:
                break
            elif (j <= i or i == 0) and (i != 0 or j != 0):
                possiblenextstates.add((i, j))
    return possiblenextstates












# state [missionaries LEFT] [cannibals LEFT] [missionaries RIGHT] [cannibals RIGHT] [boat]

def do (boatsize, people):

    initstate = [people, people, 0, 0, 0]
    queue = []
    queue.append([initstate,0, ""])

    while len(queue)!=0:
        #print(stack)
        [state,depth,path] = queue.pop(0)
        if state[2] == people and state[3] == people:
            print("SOLUTION")
            print(path)
            break


        if depth < maxdepth:
            for s in getnextstates(boatsize, state):
                #print(getnextstates(boatsize,state))
                queue.append([s,depth +1, path+str(s)])




def getnextstates (boatsize, state):

    nextstates = []

    if state[4] == 0:
        filling = filltheboat(boatsize, state [0], state[1])
        for fill in filling:
            newstate = [state[0]-fill[0], state[1] -fill[1], state[2]+fill[0], state[3]+fill[1], 1]
            if controlstate(newstate):
                nextstates.append(newstate)

    elif state [4]==1:
        filling = filltheboat(boatsize, state [2],state[3])
        for fill in filling:
            newstate = [state[0] + fill[0], state[1] + fill[1], state[2] - fill[0], state[3] - fill[1], 0]
            if controlstate(newstate):
                nextstates.append(newstate)

    return nextstates
def filltheboat(boatsize,m,c ):
    possiblenextstates = set()

    for i in range (m+1):
        for j in range (c+1):
            if i +j > boatsize:
                break
            elif  (j <=i or i==0) and (i!=0 or j !=0) :
                possiblenextstates.add((i,j))
    return possiblenextstates


def controlstate(state):

    if (state [0] >= state [1] or state [0] ==0) and (state[2] >= state[3] or state [2] ==0):
        if state [0] !=people or state [1] !=people:
            return True
    else:
        return False

print (filltheboat(2,2,2))
print (getnextstates(2,[2,0,0,2,1]))
init()