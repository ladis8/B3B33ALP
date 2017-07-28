

class Person:
    
    
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex   
        self.children = []  
        self.parents = []   # parents of this node
        self.partner = None   # partner (=husbad/wife of this node)
    
    def __eq__ (self, other):
        return True if self.name ==other.name and self.sex ==other.sex else False


    def addChild(self, node):
        self.children.append(node)
 
    def addParent(self, node):
        self.parents.append(node)
 
    def setPartner(self, node):
        if self.partner == None:          
            self.partner = node
        else:
            "ERROR"
 
    def __repr__(self):
        s = "Female" if self.sex == 'F' else "Male" 
        return self.name + " " + s
    
class FamilyTree:
    
    members = []
    

    
    def __init__ (self, path):
         
        f = open (path, 'r')
        for line in f:
            parts = line.split()
            
            person1 = Person (parts [1], parts [3])
            person2 = Person (parts [2], parts [4]) 
            relation = parts [0]
            
            if person1 in self.members:
                person1 = self.members[self.members.index(person1)]
            else:
                self.addMember(person1)
            if person2 in self.members:
                person2 = self.members [self.members.index(person2)]
            else:
                self.addMember(person2)
            
            if relation == 'P':
                person1.addChild(person2)
                person2.addParent(person1)
            elif relation == 'M':
                person1.setPartner(person2)
                person2.setPartner(person1)    
            
            print (self.members) 
                  
    
    
    def addMember (self, member):
        self.members.append(member)
        
    def findgreatson (self, grandpa):
        for child in grandpa.children:
            for grandchild in child.children:
               if grandchild.sex =='M':
                    print (grandchild, end =" ")
        print ()
               
               
                        
    def findgreatdaughter (self, grandpa):
        for child in grandpa.children:
            for grandchild in child.children:
               if grandchild.sex =='F':
                    print (grandchild, end =" ")
            
        print ()
         
                        
    def findgrandma (self, person):
        for parent in person.parents:
            for grandparent in parent.parents:
                if grandparent.male =='F':
                    print (grandparent)
                    

  
  
if __name__=="__main__":
      tree = FamilyTree ("family.txt")  
      for member in tree.members:
          print (member)
          print ("his greatdaughters are: ")
          tree.findgreatdaughter(member)
          print ("his greatsons are: ")
          tree.findgreatson(member)