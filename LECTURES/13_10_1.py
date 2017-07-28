
#postfixovy zapis
#inp = input()
operants = '+-*/'
numbers = '0123456789'
def evaluateintput (input):
    i = 0
    stack = []
    while i < len(input):
        print(stack)
        if input [i] in operants:
            stack.append(input[i])
        elif input[i] in numbers:
            if stack [len(stack) -1] in numbers:
                num2 = int (stack.pop())
                num1 = int (input [i])
                oper = stack.pop()
                if oper == '+':
                    stack.append(str(num1+num2))
                elif oper == '-':
                    stack.append(str(num1-num2))
                elif oper == '*':
                    stack.append(str(num1*num2))
                elif oper == '/':
                    stack.append(str(num1/num2))
            else:
                stack.append(input[i])
        else:
            print("WRONG INPUT")
        i+=1

    return stack.pop()

#evaluateintput("**+1235")

#nejvetsi rostouci posloupnost

def biggestposloupnost (list):

    maxlength =maxsum =0
    first  = 0
    last = 1
    sum =list [first]
    length = 1

    while last < len(list):
        if list [last] > list [last-1]:
            sum+=list [last]
            length +=1
        else:
            if length > maxlength:
                maxlength = length
                maxsum = sum
            elif length == maxlength and sum > maxsum:
                maxsum = sum

            sum =list [last]
            first = last
            length =1
        last +=1

    if length > maxlength:
        maxlength = length
        maxsum = sum
    elif length == maxlength and sum > maxsum:
        maxsum = sum

    return maxsum, maxlength
print(biggestposloupnost([6,3,2,1,2,3,4,2,4,5,6]))




