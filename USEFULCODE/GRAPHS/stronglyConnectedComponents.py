class Stack:
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def is_empty(self):
        return self.size()==0
    def push(self, item):
        self.items+=[item]
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def remove (self, v):
        self.items.remove(v)
    def __str__(self):
        return str(self.items)






""""------------Kosaraju-Sharrir O (m + n)------------"""
    #TAKES ADJECTANCY LIST AS AN INPUT
def Kosaraju_Sharrir (graph):
    n = len(graph)

#FIRST STEP - DFS (graph) and memorizing time of leaving vertexes in Stack Z
    N = [False] * n
    Z = Stack()

    def dfs(r,graph,Vr):
        N[r] = True
        Vr.add(r)
        for v in graph[r]:
            if not N[v]:
                Vr =dfs(v, graph, Vr)
        Z.push(r)
        return Vr

    for i in range(n):
        if not N[i]:
            dfs(i,graph, set())
    #print(Z)

#SECOND STEP - CREATING reversed graph
    graphop = createGop(graph)

#THIRD STEP - DFS (reversed graph), getting the roots from top of Z
    components = []
    N = [False] * n
    while not Z.is_empty():
        if not N[Z.peek()]:
            COM = set()
            COM = dfs (Z.peek(), graphop, COM)
            components.append(COM)
        else:
            Z.pop()
    return components
#OUTPUT strongly connected components
# oriented accesible vertexes in reversed graph from root r from top of Z are strongly connected components in graph

def createGop(graph):
    graphop = [[] for i in range (len(graph))]
    for u in range (len(graph)):
        for v in graph[u]:
            graphop[v].append(u)
    return graphop
""""------------Kosaraju-Sharrir O (m + n)------------"""



g =[ [1,2,3],[2],[3,4],[4],[1],[4,6,7],[4,7],[6]]
print(Kosaraju_Sharrir(g))