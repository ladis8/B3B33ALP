import sys

#3 + (-14 * 2 / 44 )^ 19
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
    #print(string)
    result =[]

    isnumbefore = False
    shouldwritebracket = 0

    counter=0
    while counter <len(string):
        chr = string [counter]

###########brackets##########
        if chr=='(':
            stack.push(chr)
            result +=chr

        elif chr==')':
            #stack.printstack()
            if stack.is_empty() or left[right.index(chr)]!=stack.pop():
                return "ERROR"
            result += chr

###########symbols##########
        elif chr in symbol:

            if chr == "-" or chr =="+":
               #so count also the first negative if there is
                counter -= 1
                negativecounter=0

                while not string [counter+1]in numbers and not string [counter+1] =='(':

                    if string [counter+1] == "-" or string [counter+1] == "+":
                        if string[counter+1] == "-" and not isnumbefore: #unar-
                            negativecounter+=1
                            result += "("
                            result += "0"
                            result += "-"
                        elif string[counter+1] == "-" and isnumbefore: #binar-
                            result +="-"
                            isnumbefore=False
                        elif string[counter+1] == "+" and isnumbefore: #binar+
                            result+="+"
                            isnumbefore=False
                        elif string[counter+1] == "+" and not isnumbefore: #unar-
                            pass
                    elif string [counter+1] in symbol:
                        return "ERROR"

                    counter += 1

                shouldwritebracket=negativecounter

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
                while counter+1 < len(string) and string [counter+1] in numbers:
                    num += string[counter+1]
                    counter+=1
                result.append(num)
                isnumbefore = True
                if (shouldwritebracket>0):
                    for i in range (shouldwritebracket):
                        result+=")"
                    shouldwritebracket=0

        counter +=1


    return result if (isnumbefore)else "ERROR"




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
    #print(postfix)
    for token in postfix:
        #print(token)

        if token[0] in numbers:
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
