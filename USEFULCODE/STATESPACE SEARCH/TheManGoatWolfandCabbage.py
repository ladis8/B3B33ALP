class State:
    def __init__(self, l, r, path):
        self.l = l
        self.r = r
        self.path = path
        self.path.append (str(self))
    def isGoal(self):
        return True if len(self.l) ==0 and len (self.r) == 4 else False
    def __hash__(self):
        return hash (str (self.l) + str( self.r) )
    def isValid(self):
         if "M" in self.r:
             if ("C" in self.l and "G" in self.l ) or ("G" in self.l and "W" in self.l):
                 return False

         else:
             if ("C" in self.r and "G" in self.r) or ("G" in self.r and "W" in self.r):
                return False

         return True
    def __str__(self):
        out = ""
        for i in self.l:
            out+=i
        out+='|'
        for i in self.r:
            out+=i
        return out

    def __eq__(self, other):
        for item in self.l:
            if item not in other.l:
                return False
        for item in self.r:
            if item not in other.r:
                return False
        return True

def successors (s):
    succ = set()
    if "M" in s.l:
        for i in s.l:
            if State(s.l - {"M", i}, s.r | {"M", i}, s.path.copy()).isValid():
                succ.add(State(s.l - {"M", i}, s.r | {"M", i},s.path.copy()))
    else:
        for i in s.r:
            if State(s.l | {"M", i}, s.r - {"M", i}, s.path.copy()).isValid():
                succ.add(State(s.l | {"M", i}, s.r - {"M", i}, s.path.copy()))
    return succ

def doBFS ():

    initstate = State ({"G", "M", "W","C"}, set(), [])
    goalstate = State (set(), {"G", "M", "W","C"}, [])

    queue = []
    queue.append(initstate)
    visited = set()
    while len(queue)!=0:
        #print(stack)
        s = queue.pop(0)
        visited.add(s)

        if s == goalstate:
            print("SOLUTION")
            for i in s.path:
                print(i)
            break

        for s in successors(s):
            if s not in queue and s not in visited:
                queue.append(s)

doBFS()

""""s = State({"G", "M"}, {"W","C"}, None)
print(s)
a = successors(s)
for b in a:

    print(b)"""""