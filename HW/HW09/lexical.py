

import keyword
import sys

##useful strings
digits = "0123456789"
hexadecimaldigits = "abcdefABCDEF"
octadigits= "01234567"
operatorsunar =["+","-", "*", "/", "%",  "&", "|", "^", "~", "<", ">"]
operatorsbinar=["**","//","<<", ">>","<=", ">=", "==", "!="]
separatorsunar = ['(',')','[',']','{','}',',',':','.',';','@','=']
separatorsbinar=['->','+=','-=','*=','/=','%=','@=','&=', '|=','^=']
separatorstrenar=['>>=','<<=','**=','//=']



temp =""
state =0
counter=0


def printTERM():
    global temp, state
    if state == 3 or state == 6 or state == 7 or state == 8:
        print("Int: ", end="")
    elif state == 4 or state == 5:
        print("Rea: ", end="")
    elif state == 9:
        if keyword.iskeyword(temp):
            print("Key: ", end="")
        else:
            print("Var: ", end="")
    print(temp)
    temp = ""
    state=0

def updateVariables(incerese, addedtotemp, changestate):
    global temp, state, counter

    counter+=incerese
    temp+=addedtotemp

    if changestate !=-1:
        state = changestate


def lexicalanalyzation():

    global temp,state, counter


    path = sys.argv [1]
    #path = "source.txt"
    f = open( path, 'r')

    skipstate = False
    single = False
    for line in f:

        if not skipstate:
            state =0
        else:
            state=1 if single else 2
        skipstate=False


        counter=0

        while counter < len (line):


            chr =line[counter]
            # counter += 1
            # print()
            #print(state)
            # print(chr)

            if state == 0:  # ischarbut not "" or ''
            ##################STRING PART########################
                if chr == "\'":
                    if counter+2 < len(line) and line [counter+2]==chr:
                        counter +=3
                    else:
                        counter+=1
                    state =1
                    print("Str: ", end="")

                elif chr == "\"":
                    if counter+2 < len(line) and line[counter + 2] == chr:
                        counter += 3
                    else:
                        counter += 1
                    state = 2
                    print("Str: ", end="")
            ##################STRING PART########################

                elif chr in digits or chr ==".": #nonzerodigit or dot
                    state = 3

                elif chr in separatorsunar or chr in operatorsunar or chr=='!':
                    state =10
                elif chr.isalpha():
                    state=9
                else:
                    counter+=1

###############################STRING PART########################################
            elif state == 1: #READING STRING WITH /'

                if chr == "\'":
                    if counter+2 < len(line) and line[counter + 2] == chr:
                        counter += 3
                    else:
                        counter+=1
                    print()
                    state =0

                elif chr == "\\":
                    if line [counter+1] == "\"" or line [counter+1] == "\'" or line [counter+1] =="\\":
                        print (line[counter+1], end="")
                        counter+=2
                    else:
                        print(chr, end="")
                        counter += 1
                else:
                    print(chr, end="")
                    counter += 1

            elif state == 2:  # READING STRING WITH /""
                if chr == "\"":

                    if counter+2 < len(line) and line[counter + 2] == chr:
                        counter += 3
                    else:
                        counter += 1
                    print()
                    state = 0

                elif chr == "\\":
                    if line [counter+1] == "\"" or line [counter+1] == "\'" or line [counter+1] =="\\":
                        print(line[counter + 1], end="")
                        counter += 2
                    else:
                        print(chr, end="")
                        counter += 1
                else:
                    print(chr, end="")
                    counter+=1
###############################STRING PART########################################

###############################DIGIT PART########################################
            elif state ==3: #READING DIGITS/DECIDING

                if chr in digits:
                    updateVariables(1, chr, -1)
                elif chr== ".":
                    if line [counter+1] in digits:
                        updateVariables(1, chr, 4)
                    else:
                        state = 10 #dot is separator
                elif chr=="e" or chr =="E":
                    updateVariables(1, chr, 5)
                elif chr=="o" or chr =="O":
                    updateVariables(1, chr, 7)
                elif chr == "b" or chr =="B":
                    updateVariables(1, chr, 6)
                elif chr == "x" or chr =="X":
                    updateVariables(1, chr, 8)
                else:
                    printTERM ()


            elif state ==4:#READING DIGITS AFTER DOT
                if chr in digits:
                    updateVariables(1, chr, -1)
                elif chr =="e" or chr=="E":
                    updateVariables(1, chr, 5)
                else:
                    printTERM()


            elif state ==5: #READING DIGITS AFTER E/e
                if chr in digits or chr=="+" or chr=="-":
                    updateVariables(1, chr, -1)
                else:
                    printTERM()

            elif state==6:#READING DIGITS AFTER BININTEGER
                if chr =="1" or chr=="0":
                    updateVariables(1, chr, -1)
                else:
                    printTERM()

            elif state==7:#READING DIGITS AFTER OCTAINTEGER
                if chr in octadigits:
                    updateVariables(1, chr, -1)
                else:
                    printTERM()

            elif state==8:#READING DIGITS AFTER OCTAINTEGER
                if chr in hexadecimaldigits:
                    updateVariables(1, chr, -1)
                else:
                    printTERM()
###############################DIGIT PART########################################

            elif state==9:#READING CHARACTERS --> VARIABLES/KEYWORDS
                if chr.isalpha() or chr in digits or chr=='_':
                    updateVariables(1, chr, -1)
                else:
                    printTERM()

            elif state==10: #DECIDING ABOUT SEPARATORS/OPERATORS

                if counter+2 < len(line):
                    symb=chr+line [counter+1] + line[counter+2]
                    if symb in separatorstrenar:
                        print("Sep: %s" %symb)
                        counter+=3
                        state=0
                        continue

                if counter+1 <len(line):
                    symb=chr + line[counter+1]
                    if symb in separatorsbinar:
                        print("Sep: %s" % symb)
                        counter += 2
                        state = 0
                        continue
                    if symb in operatorsbinar:
                        print("Ope: %s" % symb)
                        counter += 2
                        state = 0
                        continue


                if chr in separatorsunar:
                    print("Sep: %s" % chr)
                    counter += 1
                    state = 0
                    continue
                if chr in operatorsunar:
                    print("Ope: %s" % chr)
                    counter += 1
                    state = 0
                    continue

        if state==1:
            skipstate=True
            single=True
        elif state==2:
            skipstate=True
            single=False













lexicalanalyzation()



a = "'b\"c#d' #e"
#b= "i="j\"k'l#m" #n"
b = "if c=="  # ":"