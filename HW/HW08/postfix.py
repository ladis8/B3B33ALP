
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
    result =[]
    isnumbefore = False

    i=0
    while i <len(string):
        chr = string [i]

        if chr in left:
            stack.push(chr)
            result +=chr

        elif chr in right:

            if stack.is_empty() or left[right.index(chr)]!=stack.pop():
                return "ERROR"
            result += chr
        elif chr in symbol:

            if not isnumbefore:
                return "ERROR"
            else:
                isnumbefore = False
                result += chr
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

        i +=1
    #print(result)
    if (isnumbefore):
        return result
    else:
        return "ERROR"




def converter (string):

    stack = Stack()
    for chr in string:

        #print()
        #print("char: %c stack:" %chr, end="")
        #stack.printstack()

        #symbol
        if chr in symbol:

            if not stack.is_empty() and stack.peek() in symbol:
                priorityIN = int(priority[symbol.index(chr)])
                priorityTOP = int(priority[symbol.index(stack.peek())])

                while priorityTOP >=priorityIN:
                    print(stack.pop(), end=" ")
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
                print(stack.pop(), end=" ")
            stack.pop()
        else:
            print(chr, end=" ")


    while not stack.is_empty():
        print(stack.pop(), end=" ")


#string ="3 + 4 * 2 / ( 1 - 5 )"
string =input ()
string = string.replace (" ","")
erc=errorchecker(string)
if erc=="ERROR":
    print("ERROR")
else:
    converter(erc)

