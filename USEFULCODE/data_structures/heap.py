class heap:
    def __init__(self, array=None):
        self.heap = []

    def __repr__(self):
        return str(self.heap)

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.heap)

    def heapify(self, array):
        #treba zkopirovat, ne priradit x jinak se zacykli
        self.heap = array.copy()
        for i in range((len(array) - 1) // 2, -1, -1):
            self.bubbledown(i, array [i])


    def bubbleup(self, index, value):
        while (index - 1) // 2 >= 0:
            parent = (index - 1) // 2
            if self.heap[parent] > self.heap[index]:
                self.heap[index] = self.heap[parent]
                self.heap[parent] = value
                index = parent
            else:
                break

    def bubbledown(self, index, value):
        while 2 * index + 1 < len(self.heap):
            keychild = 2 * index + 1
            if keychild + 1 < len(self.heap) and self.heap[keychild + 1] < self.heap[keychild]:
                keychild += 1

            if self.heap[keychild] < value:
                self.heap[index] = self.heap[keychild]
                self.heap[keychild] = value
                index = keychild
            else:
                break

    def pop(self):
        if self.is_empty():
            return None
        min = self.heap[0]
        self.heap[0] = self.heap[-1]
        value = self.heap.pop()
        index = 0
        self.bubbledown(index, value)
        return min

    def insert(self, value):
        index = len(self.heap)
        self.heap.append(value)
        self.bubbleup(index, value)

    def delete(self, index):
        if not self.is_empty() and index < self.size():
            value = self.heap[-1]
            self.heap[index] = value
            self.heap.pop()

            if (index - 1) // 2 >=0 and self.heap[(index - 1) // 2] > value:
                self.bubbleup(index, value)
            elif  (2*index +1 < self.size() and self.heap [2*index+1] < value) or (2*index +2 < self.size() and self.heap [2*index+2] < value) :
                self.bubbledown(index, value)







a = [5,6,7,2,3,4,5]
h = heap()
h.heapify(a)
print(h)


for num in a:
    h.insert(num)
    print(h)
h.delete(2)
h.delete(5)
print (h)
for _ in range (len(a)+1):
    h.pop()
    print(h)


