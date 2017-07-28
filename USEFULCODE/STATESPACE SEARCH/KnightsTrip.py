from _collections import deque

size = 8

def init():
    numoftestcases = int (input ())

    for i in range (numoftestcases):
        loc = input().split()
        start = (ord(loc[0][0])-97, int (loc[0][1])-1)
        goal = (ord(loc[1][0])-97, int (loc[1][1])-1)
        #print(start, goal)

        print(maketrip (start,goal))
        print()

def maketrip(start, goal):
    queue = deque()
    array =[[-1] * size for i in range (size)]
    array [start [0]] [start [1]] = 0

    queue.append (start)
    path = False
    directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

    while len(queue) != 0 and path != True:
        l = queue.popleft()
       # print (l)
        for direct in directions:
            xx = direct[0] + l [0]
            yy = direct[1] + l [1]
            if xx < size and xx >= 0 and yy < size and yy >= 0 and array[xx][yy] == -1:
                array [xx] [yy] = array [l[0]] [l[1]] +1
                if xx == goal [0] and yy == goal [1]:
                    return array [xx] [yy]
                if (xx,yy) not in queue:
                    queue.append((xx, yy))

    return -1

init()

