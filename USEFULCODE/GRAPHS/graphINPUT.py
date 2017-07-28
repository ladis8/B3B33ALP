import sys
class Edge:
    def __init__(self, PV, KV, weight):
        self.PV = PV
        self.KV = KV
        self.weight = weight

    def __gt__(self, other):
        return True if self.weight > other.weight else False
    def __lt__(self, other):
        return True if self.weight < other.weight else False
    def __ge__(self, other):
        return True if self.weight >= other.weight else False
    def __le__(self, other):
        return True if self.weight <= other.weight else False
    def __str__(self):
        return "(%d,%d) %d"%(self.PV,self.KV, self.weight)

def listofedges(path):
    f = open(path, 'r')
    graph = []
    n =0
    for line in f:
        s = line.split()
        PV = int(s[0])
        KV = int(s[1])
        n = max(PV,KV,n)
        weight = int(s[2])
        graph.append(Edge(PV,KV,weight))
    return graph, n

def weightenedmatrice(path, n, oriented=False):
    f = open(path, 'r')
    graph = [[sys.maxsize] * n for j in range(n)]
    for line in f:
        s = line.split()
        PV = int(s[0])-1
        KV = int(s[1])-1
        weight = int(s[2])
        graph[PV] [KV] = weight
        if not oriented:
            graph [KV] [PV] = weight
    return graph

def adjectancylist (path,n, oriented=False):
    f = open(path, 'r')
    graph = [[] * n for _ in range(n)]
    for line in f:
        s = line.split()
        PV = int(s[0]) - 1
        KV = int(s[1]) - 1
        graph[PV].append(KV)
        if not oriented:
            graph[KV].append(PV)
    return graph


#print (weightenedmatrice("graphinput.txt", 8, False))
#print (adjectancylist("graphinput.txt",8,False))