import graphINPUT

def Topological (graph):
    n = len(graph)
    N = [False] * n
    Z = []
#FIRST STEP - DFS (graph) and memorizing time of leaving vertexes in Stack Z

    def dfs(r,graph,Z):
        N[r] = True
        for v in graph[r]:
            if not N[v]:
                Z = dfs(v, graph, Z)
            else:
                if Z is None or v not in Z:
                     return None
        Z.append(r)
        return Z

    for i in range(n):
        if not N[i]:
            Vr = dfs(i,graph, [])
            if Vr:
                Z.extend(Vr)
                print(list (reversed(Z)))
            else:
                print("cycle")
                break

graph = graphINPUT.adjectancylist ("graphinput2.txt", 5,True )
Topological(graph)