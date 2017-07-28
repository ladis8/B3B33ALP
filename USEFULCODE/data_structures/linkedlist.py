
class Node: # uzel
    def __init__(self,data):
        self.data = data
        self.next = None # odkaz na další uzel
    def __repr__(self):
        return (str(self.data)+" "+str (self.next))

""""LINKED LIST AS A STACK"""
class ListStack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    #double sided pointers
    def push(self,item):
        node=Node(item)
        node.next=self.head
        self.head=node
    #remove always the head of the list (first element)
    def pop(self):
        item=self.head.data
        self.head=self.head.next
        return item
    def peek(self):
        return self.head.data

""""LINKED LIST AS A QUEUE"""
#NODE HEAD IS NODE WHERE YOU DEQUE
#NODE TAIL IS NODE WHERE YOU ENQUE

class ListQueue(ListStack): # zdědíme ListStack

    def __init__(self):
        self.head = None
        self.last = None # last item
        self.count = 0

    def dequeue(self): # odeber ze začátku

        item=self.head.data
        self.head=self.head.next

        if self.head is None:
            self.last=None
            self.count-=1
        return item

    def push(self, data): # přidej na začátek
        node=Node(data)
        node.next=self.head
        if self.head is None:
            self.last=node
            self.head=node
            self.count+=1

    def enqueue(self, data): # přidej na konec
        node=Node(data)
        if self.head is None: # seznam je prázdný
            self.head=node
            self.last=node
        else:
            self.last.next=node
            self.last=node
            self.count+=1

    def iter(self, f):
        """ execute f(x) for all elements ’x’ in the queue """
        node = self.head
        while node is not None:
            f(node.data)
            node = node.next

    def to_array(self):
        a = []
        self.iter(lambda x: a.append(x))
        return a

    def array_to_queue(self, a):
        for x in a:
            self.enqueue(x)

    def __contains__(self, item):
        node = self.head
        while node.next is not None:
            if node.next.data == item:
                return True
            else:
                node = node.next
        return False

    def delete (self, item):
        node = self.head
        print(node)
        if node.data == item:
            self.head =node.next #you delete HEAD
        else:
            while node.next is not None:
                if node.next.data ==item:
                    if node.next.next is not None:
                        node.next = node.next.next
                    else:
                        node.next = None    #you delete LAST
                        self.last = node
                else:
                    node = node.next

    def addlisttolist (self, list):
        if list.last is None: #list is empty
            return
        if self.last is None: #base list is empty
            self.head =list.head
        else:
            print (list.last)
            print(list.head)
            print(self.last)
            self.last.next = list.head #add list to the end
        self.last = list.last
        self.count += list.count
        #smaze jinak dochazi k zacykleni
        list.last = None
        list.head = None

    def insertnodeAFTER (self, pointer, data):
        self.count +=1
        newnode = Node(data)
        newnode.next = pointer.next
        pointer.next = newnode

    def insertnodeBEFORE (self, pointer, data):
        #prohodi jako kdyby prohazoval za, akorat vymeni obsah dat
        self.insertnodeAFTER(pointer, pointer.data)
        pointer.data = data

    def deletenodeBEFORE (self, pointer):
        #pointer ukazuje na predchudce ruseneho uzlu
        #nesmi to byt last node - ten nelze odstranit!!!!!!!!!!!!!
        q = pointer.next #ten chci smazat
        if q is not None:
            self.count -= 1
            pointer.next = q.next


q=ListQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(2)
q.enqueue(3)

print (q.to_array())
q.delete(3)
print (q.last)
print (q.to_array())
q.insertnodeAFTER(q.head, 55)
print(q.to_array())
q.insertnodeBEFORE(q.head, 66)

print(q.to_array())

if 2 in q:
    print("YES")
else:
    print ("NO")

q=ListQueue()
q.array_to_queue([1,2,3])
r=ListQueue()
r.array_to_queue([4,5])
print ("ADDING ELEMENTS")

q.addlisttolist(r)
print(q.to_array())
print (r.to_array())
print (q.head)
print( q.last)
print (r.last)
print(r.head)








