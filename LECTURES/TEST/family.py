import sys
class Person:
    def __init__(self, name):
        self.name = name
        self.children = set()
        self.parents = set () # parents of this node
        self.partner = None  # partner (=husbad/wife of this node)
    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return True if self.name == other.name else False

    def addChild(self, node):
        self.children.add(node)

    def addParent(self, node):
        self.parents.add(node)

    def setPartner(self, node):
        if self.partner == None:
            self.partner = node
        else:
            "ERROR"

    def __repr__(self):

        return self.name

def init (path):
        f = open(path, 'r')
        tree = set()
        for line in f:
            line = line.rstrip().split()
            if len(line) == 0:
                continue
            elif len(line) == 2:
                parent = Person(line[0])
                child = Person(line[1])
                tree.add(parent)
                tree.add(child)
                for p in tree:
                    if p ==parent:
                        p.children.add(child)
                    if p ==child:
                        p.parents.add (parent)
                        if len(p.parents) >2:
                            return "ERROR"
            else:
                return "ERROR"
        return tree

def findgrandpar(person, tree):
    parents = person.parents
    granparents = set()

    for person  in tree:
        if person in parents:
            for p in person.parents:
                granparents.add(p)

    return granparents
def findgreatchld(person, tree):
        children = person.children
        grandchildren = set()
        for person in tree:
            if person in children:
                for p in person.children:
                    grandchildren.add(p)
        return grandchildren
def findcousin (person, tree):
    granparents = findgrandpar(person, tree)
    uncles = set()
    for p in granparents:
        pass

#tree = init("test.txt")
tree = init (sys.argv[1])
name = input()
if tree == "ERROR":
    print("ERROR")
else:

    for p in tree:
        person = None
        if p.name == name:
            person = p
            break
    g = findgrandpar(person, tree)
    e = findgreatchld(person,tree)
    for p in g:
        print(p.name, end= " ")
    print()
    for p in e:
        print(p.name, end=" ")












