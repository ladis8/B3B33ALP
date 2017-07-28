from stack import Stack

import re
class Queue:
    def __init__(self):
        self.inp = Stack()
        self.out = Stack()
    def is_empty(self):
        return self.size()==0
    def enqueue(self, item):
        self.inp.push(item)
    def dequeue(self):
        if self.out.is_empty():
            while not self.inp.is_empty():
                self.out.push(self.inp.pop())
        return self.out.pop()
    def size(self):
        return self.inp.size() + self.out.size()
    

a= [1,2,3]
if re.compile(r'[a-z]*').fullmatch ("ahoj"):
    print("OK")
else:
    print ("BAD")