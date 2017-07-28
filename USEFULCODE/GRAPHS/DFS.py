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
    def __str__(self):
        return str(self.items)

def dfs (graph, r):
    """"Takes graph as a adjectancy list and the root node r"""
    n = len(graph)
    N = [False] * n
    P = [[False] * len(graph [i]) for i in range(n)]
    Vr = {r}
    Er = set()
    cyklus = False

    stack = Stack()
    stack.push(r)
    N[r] = True

    while not stack.is_empty():
        u = stack.peek()
        print(stack)
        for index, v in enumerate(graph [u]):
            if P [u][index]==False: #takes the edge e = {u,v}
                P [u][index] = True
                Er.add((u,v))
                print(v)

                if N[v] == False:
                    N[v] = True

                    Vr.add(v)
                    stack.push(v)
                else:
                    cyklus = True
                break
        stack.pop()
    return Vr,Er


print (dfs ([ [1,2,3],[2],[3,4],[4],[1],[4,6,7],[4,7],[6]],0)[0])


