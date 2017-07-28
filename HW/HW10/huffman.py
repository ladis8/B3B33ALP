import sys

#f = open (sys.argv [1], 'r')
f = open ("huffman.txt", 'r')
#nameoffile = sys.argv [2]
nameoffile = "out.txt"


class heap:

    def __init__(self, array=None):
        self.heap = []
    def __repr__(self):
        return str(self.heap)
    def is_empty(self):
        return self.size() == 0
    def size (self):
        return len(self.heap)

    def pop (self):
        if self.is_empty():
            return None
        min = self.heap [0]
        self.heap[0] = self.heap [-1]
        value = self.heap.pop()
        index = 0

        while 2*index+1 < len(self.heap):
            keychild = 2*index+1
            if keychild+1 < len(self.heap) and self.heap [keychild+1] < self.heap[keychild]:
              keychild+=1

            if self.heap [keychild]< value:
                self.heap [index] =self.heap [keychild]
                self.heap [keychild] = value
                index = keychild
            else:
                break

        return min

    def insert (self, value):
        index = len(self.heap)
        self.heap.append(value)

        while (index-1)//2 >=0:
            parent = (index-1)//2
            if self.heap [parent] > self.heap [index]:
                self.heap [index] = self.heap [parent]
                self.heap [parent]= value
                index = parent
            else:
                break



class Node:
    def __init__(self, frequency, char,name = None, left = None, right=None, top=None, ):
        self.left = left
        self.right = right
        self.top = top
        self.char = str(char)
        self.frequency = frequency
        self.name = name

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __gt__(self, other):
        return self.frequency > other.frequency
    def __repr__(self):
        #return "Node: %s %s freq %d" %(self.name, self.char, self.frequency)
        return "%s %s\n" %(self.name, self.char)


def histogram (file):

    chars = []
    values = []
    sum = 0

    for line in file:
        line = line.replace (" ","").rstrip ('\n')

        for char in line:
            if char in chars:
                values [chars.index(char)] +=1
                sum+=1
            else:
                chars.append(char)
                values.append(1)
                sum+=1

    return chars,values

def createhuffmantree(chars, values):
    h = heap()
    for i in range (len(values)):
        n = Node (values [i], "", chars [i])
        h.insert(n)


    while h.size() >1:
        n1 = h.pop()
        n2 = h.pop()
        n = Node(n1.frequency+n2.frequency, "","", n2,n1, None)
        n1.top=n
        n2.top = n
        h.insert(n)

    rootnode = h.pop()
    putbit(rootnode)

    f = open(nameoffile, 'w')
    writeoutput(f, rootnode)

def putbit (node):
    if not node.left == None:
        node.left.char += node.char
        node.right.char += node.char
        node.left.char +='0'
        node.right.char += '1'
        putbit(node.left)
        putbit(node.right)
    else:
        print(node)

def writeoutput (file,rootnode):
    if not rootnode.left == None:
        writeoutput(file, rootnode.left)
        writeoutput(file, rootnode.right)
    else:
        file.writelines(str(rootnode))



hist = histogram(f)
createhuffmantree(hist[0], hist [1])

