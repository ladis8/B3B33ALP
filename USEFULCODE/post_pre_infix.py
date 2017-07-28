#common strings
left = "({["
right = ")}]"
symbol = "+-*/^"
priority = "11223"
numbers= "0123456789"


class Stack:
    def __init__(self):
        self.items = []
    def __str__(self):
        return str(self.items)
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


"""/////EVALUATING POSTFIX////"""
def evalpostfix (inp):
    stack = Stack()
    for char in inp:
        if char in numbers:
            stack.push(int (char))
        elif char in symbol:
            first = stack.pop()
            second = stack.pop()
            if char == '+':
                stack.push(first + second)
            elif char =='-':
                stack.push(second-first)
            elif char == '*':
                stack.push(first*second)
            elif char == '/':
                stack.push(second/first)
    return stack.pop()
print(evalpostfix("3 4 * 2 -"))


"""/////EVALUATING PREFIX////"""
def evalprefix (inp):
    stack = Stack()
    inp = reversed(inp)
    for char in inp:
        if char in numbers:
            stack.push(int (char))
        elif char in symbol:
            first = stack.pop()
            second = stack.pop()
            if char == '+':
                stack.push(first + second)
            elif char =='-':
                stack.push(first-second)
            elif char == '*':
                stack.push(first*second)
            elif char == '/':
                stack.push(first/second)
    return stack.pop()

print(evalprefix("**+1235"))



def infixtopostfix (string):
    #string =string.replace(" ", "")

    stack = Stack()
    for chr in string:
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
        elif chr in numbers:
            print(chr, end = "")
        elif chr== " ":
            print(chr, end = " ")


    while not stack.is_empty():
        print(stack.pop(), end=" ")



infixtopostfix("33 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3")
print ()

def infixtoprefix (string):
    pass
""""Algorithm ConvertInfixtoPrefix

Purpose: Convert an infix expression into a prefix expression. Begin
// Create operand and operator stacks as empty stacks.
Create OperandStack
Create OperatorStack

// While input expression still remains, read and process the next token.

while( not an empty input expression ) read next token from the input expression

    // Test if token is an operand or operator
    if ( token is an operand )
    // Push operand onto the operand stack.
        OperandStack.Push (token)
    endif

    // If it is a left parentheses or operator of higher precedence than the last, or the stack is empty,
    else if ( token is '(' or OperatorStack.IsEmpty() or OperatorHierarchy(token) > OperatorHierarchy(OperatorStack.Top()) )
    // push it to the operator stack
        OperatorStack.Push ( token )
    endif

    else if( token is ')' )
    // Continue to pop operator and operand stacks, building
    // prefix expressions until left parentheses is found.
    // Each prefix expression is push back onto the operand
    // stack as either a left or right operand for the next operator.
        while( OperatorStack.Top() not equal '(' )
            OperatorStack.Pop(operator)
            OperandStack.Pop(RightOperand)
            OperandStack.Pop(LeftOperand)
            operand = operator + LeftOperand + RightOperand
            OperandStack.Push(operand)
        endwhile

    // Pop the left parthenses from the operator stack.
    OperatorStack.Pop(operator)
    endif

    else if( operator hierarchy of token is less than or equal to hierarchy of top of the operator stack )
    // Continue to pop operator and operand stack, building prefix
    // expressions until the stack is empty or until an operator at
    // the top of the operator stack has a lower hierarchy than that
    // of the token.
        while( !OperatorStack.IsEmpty() and OperatorHierarchy(token) lessThen Or Equal to OperatorHierarchy(OperatorStack.Top()) )
            OperatorStack.Pop(operator)
            OperandStack.Pop(RightOperand)
            OperandStack.Pop(LeftOperand)
            operand = operator + LeftOperand + RightOperand
            OperandStack.Push(operand)
        endwhile
        // Push the lower precedence operator onto the stack
        OperatorStack.Push(token)
    endif
endwhile
// If the stack is not empty, continue to pop operator and operand stacks building
// prefix expressions until the operator stack is empty.
while( !OperatorStack.IsEmpty() ) OperatorStack.Pop(operator)
    OperandStack.Pop(RightOperand)
    OperandStack.Pop(LeftOperand)
    operand = operator + LeftOperand + RightOperand

    OperandStack.Push(operand)
endwhile

// Save the prefix expression at the top of the operand stack followed by popping // the operand stack.

print OperandStack.Top()

OperandStack.Pop()

End"""