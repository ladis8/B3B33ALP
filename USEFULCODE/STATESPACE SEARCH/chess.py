
size = 7

array = []
for _ in range(size):
    array.append([-1] * size)
def initStates():
    startx = int(input())
    starty = int(input())
    if move (startx, starty, 0):
        printsolution(array)

def move (x, y, depth):

    def getpossiblemoves ():
        directions = [(2,1),(2,-1), (-2,1),(-2,-1), (1,2),(1,-2),(-1,2),(-1,-2)]
        possiblemoves = set()
        for direct in directions:
            xx = direct[0] + x
            yy = direct[1] +y
            if xx <size and xx >=0 and yy <size and yy>=0 and array [xx][yy] ==-1:
                possiblemoves.add((xx,yy))
        return  possiblemoves

    #print(array)
    array [x][y] = depth
    if depth == size**2 -1:
        return True

    possiblemoves =getpossiblemoves()

    for m in possiblemoves:
        solution = move(m[0], m[1], depth + 1)
        if solution:
            return True

    array[x][y] = -1 #go back
    return False

def printsolution (array):
    for i in range (size):
        print(array[i])

initStates()


