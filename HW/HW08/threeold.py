import sys
class Stack:
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def is_empty(self):
        return self.size()==0
    def push(self, item):
        self.items+=[item]
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def printstack(self):
        print(self.items)


#common strings
left = "({["
right = ")}]"
symbol = "+-*/^"
priority = "11223"
numbers= "0123456789"


def errorchecker (string):
    stack = Stack()
    string = string.replace(" ", "")
    print(string)
    result =[]
    
    i=0
    while  (i < len(string)):
        chr = string [i]
        
        if chr == '-' or '+':
            negativecounter=0
        
            while (string [i+1] =='+' or '-'):
                if string [i+1] =='-':
                    negativecounter+=1
                i+=1
                
            if negativecounter%2==1:
                
                index = i
                
                while 
                
                
                
                
            else :
                result.append("+")
                
            
        
        
        

    isnumbefore = False
    shouldwritebracket = False

    i=0
    while i <len(string):
        print(string[i])
        print(result)
        chr = string [i]

###########brackets##########
        if chr in left:
            stack.push(chr)
            result +=chr

        elif chr in right:
            stack.printstack()
            if stack.is_empty() or left[right.index(chr)]!=stack.pop():

                return "ERROR"
            result += chr

###########symbols##########
        elif chr in symbol:

            if chr == "-" or chr =="+":
               #so count also the first negative if there is
                negativecounter=0
                i-=1
                #print (string [i])
                while not string [i+1]in numbers:

                    if string [i+1] == "-" or string [i+1] == "+":
                        if string[i + 1] == "-":
                            negativecounter+=1
                    elif string [i+1] in symbol:
                        return "ERROR"

                    elif string [i+1] in left:
                        stack.push(string [i+1])
                        result +=string [i+1]

                    i+=1

                if not isnumbefore:
                    if negativecounter%2 ==1:
                        result+="(0"
                        result+="-"
                        shouldwritebracket=True


                else:
                    if negativecounter%2==1:
                        result+="-"
                    else:
                        result+="+"
                    isnumbefore = False



            else:
                if not isnumbefore:
                    return "ERROR"
                else:
                    isnumbefore = False
                    result += chr

##########numbers##########
        elif chr in numbers:
            if isnumbefore:
                return "ERROR"
            else:
                num = chr
                while i+1 < len(string) and string [i+1] in numbers:
                    num += string[i+1]
                    i+=1
                result.append(num)
                isnumbefore = True
                if (shouldwritebracket):
                    result+=")"
                    shouldwritebracket =False

        i +=1
    #print(result)
    if (isnumbefore):
        print(result)
        return result
    else:
        return "ERROR"




def postfixconverter (string):

    stack = Stack()
    result = []
    for chr in string:

        #symbol
        if chr in symbol:

            if not stack.is_empty() and stack.peek() in symbol:
                priorityIN = int(priority[symbol.index(chr)])
                priorityTOP = int(priority[symbol.index(stack.peek())])

                while priorityTOP >=priorityIN:
                    result.append(stack.pop())
                    if not stack.is_empty() and stack.peek() in symbol:
                        priorityTOP = int(priority[symbol.index(stack.peek())])
                    else:
                        break

            stack.push(chr)


        #bracket left
        elif chr in left:
            stack.push(chr)
        #bracket right
        elif chr in right:
            while (stack.peek() != left[right.index(chr)]):
                result.append(stack.pop())
            stack.pop()
        else:
            result.append(chr)


    while not stack.is_empty():
        result.append(stack.pop())
    return result

def threeconverter (inp):
    stack = Stack()
    counter=1
    postfix = postfixconverter(inp)
    print(postfix)
    for token in postfix:
        #print(token)

        if token in numbers:
            stack.push(token)

        elif token in symbol:
            t2= stack.pop()
            t1= stack.pop()
            print("t%d:=%s%s%s" %(counter, t1, token, t2 ))
            x = "t%d" %counter
            stack.push(x)
            counter+=1










#string ="3 + 4 * 2 / ( 1 - 5 )"
string =input ()
erc=errorchecker(string)
if erc=="ERROR":
    print("ERROR")
else:
    threeconverter(erc)
