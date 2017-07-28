class heap:

    def __init__(self, array=None):
        self.heap = []
        self.values = []

    def __repr__(self):
        return str(self.heap)

    def is_empty(self):
        return self.size() == 0

    def size (self):
        return len(self.heap)

    def pop (self):

        if self.is_empty():
            return None

        #min = self.heap [0]
        self.heap[0] = self.heap [-1]
        value = self.heap.pop()

        min = self.values [0]
        self.values[0] = self.values[-1]
        valstr = self.values.pop()

        index = 0

        while 2*index+1 < len(self.heap):

            keychild = 2*index+1
            if keychild+1 < len(self.heap) and self.heap [keychild+1] > self.heap[keychild]:
              keychild+=1

            if self.heap [keychild]> value:
                self.heap [index] =self.heap [keychild]
                self.heap [keychild] = value

                self.values[index] = self.values[keychild]
                self.values [keychild] = valstr

                index = keychild
            else:
                break

        return min

    def insert (self, value, str):
        index = len(self.heap)
        self.heap.append(value)
        self.values.append(str)

        while (index-1)//2 >=0:
            parent = (index-1)//2
            if self.heap [parent] < self.heap [index]:
                self.heap [index] = self.heap [parent]
                self.heap [parent]= value
                self.values [index] = self.values [parent]
                self.values [parent] = str

                index = parent
            else:
                break



h = heap()
while True:
    try:
        if h.size()==10:
            print(h.pop())
        line = input ().rstrip('\r\n')
        h.insert(int (line.split(" ") [0]), line.split(" ") [1])

    except (EOFError):
        break

while h.size() > 0:
        print(h.pop())
    #print(h)



