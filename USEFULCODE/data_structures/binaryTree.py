class BinaryTree:
    def __init__(self, data, left = None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.data)

def seachinorder(root):
#postorder, pre order -- just different position of print statement
    if root.left is not None:
        seachinorder(root.left)
    print(root, end=" ")
    if root.right is not None:
        seachinorder(root.right)

t=BinaryTree('*',BinaryTree("+",BinaryTree(7),BinaryTree(3)),BinaryTree("-",BinaryTree(5),BinaryTree(2)))
seachinorder(t)
print()




class Node:
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
    def __repr__(self):
        return str(self.key)
    def __gt__(self, other):
        return True if self.key > other.key else False
    def __lt__(self, other):
        return True if self.key < other.key else False

class BinarySeachTree:

    def __init__ (self,):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __contains__(self, item):
        def isThere (self, node, item): #helper reccurent function
            if node:
                if node.key == item:
                    return True
                elif node.key > item:
                    return isThere(self, node.left, item)
                elif node.key < item:
                    return isThere(self, node.right, item)
            return False

        return True if isThere (self,self.root,item) else False

    """"def __repr__(self):
        def printTree (self, node, string):
            leftpart=""
            rightpart =""
            if node.left:
                leftpart = printTree(self,node.left, string)
            if node.right:
                rightpart =printTree(self, node.right, string)
            return string+leftpart+("%s " %(str (node)))+rightpart

        return printTree(self, self.root, "") if self.root else ""  """

    def __repr__(self):
        string =""
        def printTree (self, node):
            nonlocal string
            if node.left:
                printTree(self,node.left)
            string +=("%s " %(str (node)))
            if node.right:
                printTree(self, node.right)
        printTree(self,self.root)
        return string



    def treefromArray(self, array):
        def build (self, array):
            if len (array) == 0:
                return None
            elif len (array) == 1:
                return Node (array[0])
            else:
                middle = len(array)//2
                node = Node(array[middle])
                node.left = build(self, array[:middle])
                node.right = build(self, array[middle+1:])
                return node
        array = sorted(array)
        print(array)
        self.root = build(self, array)

    #LESS EQUAL/ GREATER OR EQUAL IF YOU WANT TO ALLOW DUPLICATES
    def add (self, value):
        def _add (self, node, value):
            if node.key >=value:
                if node.left:
                    _add(self, node.left, value)
                else:
                    node.left = Node (value)
            elif node.key <= value:
                if node.right:
                     _add(self, node.right, value)
                else:
                    node.right = Node(value)
        if self.root:
            _add(self,self.root,value)
        else:
            self.root = Node (value)
        self.size +=1



    def delete (self, value):
        def rightmost_node (self, node):
            while node.right:
                node = node.right
            return node

        def _delete (self, node, value):
            if node.key > value:
                node.left = _delete (self, node.left,value)
            elif node.key < value:
                node.right = _delete(self, node.right, value)
            else: #uzel nalezen
                if node.left is None and node.right is None:
                    return None
                elif node.left and node.right is None:
                    return node.left
                elif node.right and node.left is None:
                    return  node.right
                else: #substitue with maximum of left tree
                    rightmost = rightmost_node(self, node.left)
                    node.key = rightmost.key
                    node.left = _delete (self, node.left, rightmost.key)
            return node

        if self.__contains__(value):
            _delete(self, self.root, value)







bst = BinarySeachTree ()
bst.add(3)
bst.add(2)
bst.add(4)
print (bst)
bst.delete(3)
print (bst)
bst.treefromArray([2,4,5,67,8,4,1,3,5,5,5,8])
print ("Yes" if 8 in bst else "No")
print(bst)

for i in range (20):
    bst.add(i)
    print(bst)

print (bst)

