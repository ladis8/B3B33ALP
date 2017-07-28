import heapq

""""---------------FLOYD-WARSHALL ALGORITHM O (n^3)---------------"""
                    #findall shortest paths
def Floyd_Warshall (matrixofdistances):
    minimumdistances = [row.copy() for row in matrixofdistances]
    size = len(minimumdistances)
    for i in range (size):
        minimumdistances [i] [i] =0

    for k in range (size):
        for i in range (size):
            for j in range (size):
                #cesta z i do j pres k
                if minimumdistances [i] [j] > minimumdistances [i] [k] + minimumdistances [k] [j]:
                    minimumdistances [i] [j] = minimumdistances [i] [k] + minimumdistances [k] [j]

    return minimumdistances
""""---------------FLOYD-WARSHALL ALGORITHM O (n^3)---------------"""


""""---------------DIJKSTRA ALGORITHM O (E log V)---------------"""
    #find given shortest path for all paths O (E V log V)
def Dijkstra (matrixofdistances, start):

    vertexnum = len(matrixofdistances)
    for i in range (vertexnum):
        matrixofdistances [i] [i] =0

    processed = [False]* vertexnum
    distances = [INF] * vertexnum
    distances [start] = 0
    predeccesors = [None] * vertexnum
    queue = []
    heapq.heappush (queue, (0.,start ))

    while len(queue) > 0:
        nextnode = heapq.heappop(queue)[1]
        #print(nextnode)
        if processed [nextnode]:
            continue
        processed [nextnode] = True

        for index,edge  in enumerate(matrixofdistances [nextnode]):
            newdistance = distances [nextnode] + edge

            if newdistance  < distances [index]:
                distances [index] = newdistance
                predeccesors [index] = nextnode
                heapq.heappush(queue, (newdistance, index))

    return distances, predeccesors
""""---------------DIJKSTRA ALGORITHM O (E log V)---------------"""


def recontuatepath (predessors, goal):

    nextnode = predessors [goal]
    path = []
    path.append(goal)
    while nextnode is not None:
        path.append(nextnode)
        nextnode = predessors [nextnode]
    path = list (reversed (path))
    print("shortest path:", "".join(map(lambda x: str(x)+ "-->", path)))
    print ("shortest path:","-->".join(map (lambda x : str (x), path)))


def bfs(graph, start, target):
    vertexnum = len(graph)
    queue = []
    visited = [False] * vertexnum
    parent = [None] * vertexnum

    queue.append(start)

    while len(queue) > 0:
        current = queue.pop(0)
        if current == target:
            break

        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = current
                queue.append(neighbor)



INF = float ("inf")
g=[[INF, 5, INF, INF, INF, 2], [INF, INF, 4, INF, INF, INF],
[INF, INF, INF, 9, INF, INF], [INF, INF, INF, INF, 7, 3],
[1, INF, INF, INF, INF, INF], [INF, INF, 1, INF, 8, INF]]

print("FLOYD WARSHALLL:")
floyd = Floyd_Warshall(g)
for i in range (len(floyd)):
    print(floyd [i])

print("DIJKSTRA:")
for i in range (len(g)):
    print(Dijkstra(g, i)[0])

recontuatepath((Dijkstra(g,0)[1]), 2)

