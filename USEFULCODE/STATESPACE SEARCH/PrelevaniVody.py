from sys import stdin

maxa= maxb=goal=-1


""""--------------------VERSION FOR UVA SITUATED PROBLEM--------------------"""
class State:
    def __init__(self, a, b,path,depth):
        self.state = [[a, maxa], [b, maxb], ]
        self.path = path
        self.depth = depth
    def __str__(self):
        return "[%s,%s]" %(self.state[0][0], self.state[1][0])
    def __hash__(self):
        return hash((self.state[0][0], self.state[1][0]))
    def __eq__(self, other):
        return True if self.state[0][0]==other.state [0][0] and self.state[1][0]==other.state [1][0] else False
    def isGoal (self):
        return True if self.state[0][0]==goal or self.state[1][0]==goal else False

def N (s, nadoba):
    if s.state [nadoba] [0] < s.state[nadoba] [1]:
        newstate = State(s.state [0][0], s.state [1][0],s.path + ("-fill %d" %nadoba),s.depth+1)
        newstate.state [nadoba] [0] = s.state[nadoba] [1]
        return newstate

def V (s, nadoba):
    if s.state [nadoba] [0] !=0:
        newstate = State(s.state [0][0], s.state [1][0], s.path+ ("-empty %d" %nadoba),s.depth+1)
        newstate.state [nadoba] [0] = 0
        return newstate
def P (s, n1, n2):
    if s.state[n1][0] != 0 and s.state[n2][0] != s.state[n2][1] and n1!=n2:
        if s.state[n1][0] <= (s.state[n2][1]-s.state[n2][0]):
            newstate = State(s.state[0][0], s.state[1][0],s.path+ ("-pour %d %d" %(n1,n2)),s.depth +1)
            newstate.state[n1][0]=0
            newstate.state[n2][0]= s.state[n2][0]+s.state[n1][0]
            return newstate
        else:
            newstate = State(s.state[0][0], s.state[1][0], s.path+ ("-pour %d %d" %(n1,n2)),s.depth +1)
            newstate.state[n1][0] = s.state[n1][0] - (s.state[n2][1]-s.state[n2][0])
            newstate.state[n2][0] = s.state[n2][1] #maximum
            return newstate

def successors (s):
    nextstates = set()
    for i in range (2):
        if N(s, i):
            nextstates.add(N(s, i))
        if V(s, i):
            nextstates.add(V(s, i))
        for j in range(2):
            if P (s, i, j):
                nextstates.add(P(s,i,j))
    return nextstates

def doBFS ():
    queue = []
    initstate = State(0,0,"",0)
    queue.append(initstate)
    visited = set()
    while len(queue) !=0:
        s = queue.pop(0)
        visited.add(s)
        if s.isGoal():
            a = s.path.split('-')
            for i in range (1,len(a)):
                b = a[i].replace ('0','A')
                b = b.replace('1', 'B')
                print(b)
            print("success")
            break


        succ = successors(s)
        for n in succ:
            if n not in queue and n not in visited:
                queue.append(n)

def init ():
    for line in stdin:
        try:
            global maxa, maxb,goal
            [maxa, maxb, goal] = map (int, line.split())
            doBFS()

        except EOFError:
            break


init()
""""--------------------VERSION FOR UVA SITUATED PROBLEM--------------------"""


""""--------------------VERSION FOR SCHOOL TEST--------------------"""
""""class State:
    def __init__(self, a, b, c, previous,path,depth):
        self.state = [[a, maxa], [b, maxb], [c, maxc]]
        self.previous = previous
        self.path = path
        self.depth = depth
    def __str__(self):
        return "[%s,%s,%s]" %(self.state[0][0], self.state[1][0],self.state[2][0])
    def __hash__(self):
        return hash((self.state[0][0], self.state[1][0],self.state[2][0]))
    def __eq__(self, other):
        return True if self.state[0][0]==other.state [0][0] and self.state[1][0]==other.state [1][0]and self.state[2][0]==other.state[2][0] else False
    def isGoal (self):
        return True if self.state[0][0]==goal or self.state[1][0]==goal or self.state[2][0]==goal else False

def N (s, nadoba):
    if s.state [nadoba] [0] < s.state[nadoba] [1]:
        newstate = State(s.state [0][0], s.state [1][0], s.state[2][0], s,s.path + (" N%d" %nadoba),s.depth+1)
        newstate.state [nadoba] [0] = s.state[nadoba] [1]
        return newstate

def V (s, nadoba):
    if s.state [nadoba] [0] !=0:
        newstate = State(s.state [0][0], s.state [1][0], s.state[2][0], s, s.path+ (" V%d" %nadoba),s.depth+1)
        newstate.state [nadoba] [0] = 0
        return newstate
def P (s, n1, n2):
    if s.state[n1][0] != 0 and s.state[n2][0] != s.state[n2][1] and n1!=n2:
        if s.state[n1][0] <= (s.state[n2][1]-s.state[n2][0]):
            newstate = State(s.state[0][0], s.state[1][0], s.state[2][0], s,s.path+ (" %dP%d" %(n1,n2)),s.depth +1)
            newstate.state[n1][0]=0
            newstate.state[n2][0]= s.state[n2][0]+s.state[n1][0]
            return newstate
        else:
            newstate = State(s.state[0][0], s.state[1][0], s.state[2][0], s, s.path+(" %dP%d" %(n1,n2)), s.depth+1)
            newstate.state[n1][0] = s.state[n1][0] - (s.state[n2][1]-s.state[n2][0])
            newstate.state[n2][0] = s.state[n2][1] #maximum
            return newstate

def successors (s):
    nextstates = set()
    for i in range (3):
        if N(s, i):
            nextstates.add(N(s, i))
        if V(s, i):
            nextstates.add(V(s, i))
        for j in range(3):
            if P (s, i, j):
                nextstates.add(P(s,i,j))
    return nextstates

def doBFS (maxdepth):
    queue = []
    initstate = State(0,0,0,None,"",0)
    queue.append(initstate)
    visited = set()
    while len(queue) !=0:
        s = queue.pop(0)
        visited.add(s)
        if s.isGoal():
            print("Solution")
            a = s.path.split()
            for i in a:
                print(i)

        succ = successors(s)
        for n in succ:
            if n not in queue and n not in visited and n.depth < maxdepth:
                queue.append(n)

def init ():
    global maxa, maxb,maxc,goal
    [maxa, maxb,maxc] = map (int, input().split())
    goal = int(input())
    doBFS(10)

init()"""
""""--------------------VERSION FOR SCHOOL TEST--------------------"""




