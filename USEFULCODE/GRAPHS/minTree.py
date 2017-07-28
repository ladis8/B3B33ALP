import graphINPUT
import sys
class Node:
    def __init__(self,id):
        self.parent = None
        self.id = id
        self.rank =0

    def __eq__(self, other):
        return True if self.id == other.id else False
    def __str__(self):
        return str(self.id)
    def __hash__(self):
        return hash(self.id)

class DisjointSet:
    def __init__(self, n):
        """"make disjoint set by several singletons in range 0-n"""
        self.nodes = [Node(id) for id in range(n+1)]
        self.nodes[0] = None
    def __len__(self):
        return len(self.nodes)

    def __str__(self):
        rootnodes = []
        out = "{"
        for i in range(1,len(self.nodes)):
            rootNode = self.find(self.nodes[i].id)
            if rootNode not in rootnodes:
                rootnodes.append(rootNode)

        connectednodes = [{rootNode.id} for rootNode in rootnodes]

        for i in range(1, len(self.nodes)):
            index = rootnodes.index(self.find(self.nodes[i].id))
            connectednodes[index].add(self.nodes[i].id)
        out = "{"
        for m in connectednodes:
            out += str(m)
        out +="}"
        return out

    def find (self, v):
        """"find the representant of the node with id v"""
        #print(self.nodes[v])
        try:
            node = self.nodes [v]
            jumps = 0
            while node.parent:
                node = node.parent
                jumps +=1
            if jumps >1:
                self.repair (v, node.id)
            return node
        except IndexError:
            return Exception

    def union (self,x, y):
        """"merge the two components with id x and y"""
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return
        if xRoot.rank < yRoot.rank:
            xRoot.parent = yRoot
        elif xRoot.rank > yRoot.rank:
            yRoot.parent = xRoot
        else:
            yRoot.parent = xRoot
            xRoot.rank = xRoot.rank +1

    def repair (self, v, rootId):
        node = self.nodes[v]
        while node.id != rootId:
            tmp = node.parent
            node.parent = self.nodes [rootId]
            node.rank =0
            node = tmp


"""---------KRUSKAL GREEDY ALGORITM O (m log m)---------"""
        # TAKES LIST OF EDGES AS AN INPUT
def Kruskal(graph, n):

    graph = sorted(graph)
    L = []
    DS = DisjointSet(n)
    price= 0
    i = 0

    while len(DS) > 1 and i < len(graph):
        e,u,v = graph [i], graph[i].PV, graph[i].KV
        i+=1
        if DS.find(u) != DS.find(v):
            DS.union(u,v)
            L.append(e)
            price+=e.weight
    return L,price
"""---------KRUSKAL GREEDY ALGORITM O (m log m)---------"""



"""---------JARNIK-PRIME ALGORITM O (n^2)---------"""
    #TAKES METRICE OF EDGES AS AN INPUT
def JarnikPrime(graph):
    n = len(graph)
    g = graph[0].copy() #g... array of cheapest edges to first component
    g [0] =0
    e = [0 if g[i] !=sys.maxsize else None for i in range(n)]
    e[0] = None

    S = {0} #S... set of nodes in first component
    L = set()
    price = 0


    while len(S) != n:
        #this do the magic
        weight,v = min((val, idx) for (idx,val) in enumerate(g) if idx not in S)


        if weight == sys.maxsize:
            print("Graph is not connected")
            break

        S.add(v)
        L.add((e[v]+1,v+1)) #for indexing purposes
        price +=weight

        for w in range(n):
            if w not in S:
                if g[w] > graph [v][w]:#if there is cheaper edge cross v add it
                    g[w] = graph[v][w]
                    e[w] = v
    return L, price
"""---------JARNIK-PRIME ALGORITM O (n^2)---------"""






graph,n =graphINPUT.listofedges("graphinput.txt")
minTree, price =Kruskal(graph,n)
print("Kruskal:")
print(price,end = "     ")
for e in minTree:
    print(e, end = "   ")
print()
graph = graphINPUT.weightenedmatrice ("graphinput.txt",8)
print("Jarnik-Prime: ")
minTree, price =JarnikPrime(graph)
print(minTree)
print(price)




