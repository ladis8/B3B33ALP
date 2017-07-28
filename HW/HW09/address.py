import sys


def makenote():
    digits = "0123456789"

    #f = open("source2.txt", 'r')
    f = open(sys.argv[1], 'r')
    for line in f:
        line = line.rstrip('\n')
        counter = 0
        state = 0
        krestnijmeno=""
        prijmeni=""
        ulice =""
        psc=""
        mesto=""

        #print (line)

        while counter < len(line):
            token = line[counter]
            #print (token)
            #print (state)


            if state==0: #cele jmeno

                if token.isalpha():
                    state=1
                elif token ==';' and line[counter+1]==" ":
                    state=6
                    counter+=2
                else:
                    state="ERROR"

            elif state ==1: #krestni jmeno
                if token.isalpha():
                    krestnijmeno+=token
                    counter+=1
                elif token==" ":
                    state = 2
                    counter+=1
                else:
                    state="ERROR"


            elif state ==2: #krestni jmeno DECISION

                if token == '{':  # vyssi priorita
                    counter += 1
                    state = 4
                elif token=='(':
                    state=3
                    counter+=1
                elif token.isalpha():
                    state=5
                #????
                elif token==" ":
                    counter+=1
                    continue
                else:
                    state = "ERROR"

            elif state ==3: #krestni jmeno v zavorkach
                if token.isalpha():
                    counter+=1
                elif token==" ":
                    counter+=1
                elif token ==')':
                    if line[counter+2]=='{':
                        state=4
                        counter+=3
                    elif line [counter+2].isalpha():
                        state=5
                        counter+=2
                    else:
                        state="ERROR"
                else:
                    state="ERROR"

            elif state==4: #rodne prijmeni
                if  token.isalpha():
                    counter+=1
                elif token=='}':
                    state=5
                    counter+=1
                else:
                    state="ERROR"
            elif state==5: #prijmeni
                if token.isalpha():
                    prijmeni+=token
                    counter+=1
                elif token ==';':
                    state=0
                elif token ==" ":
                    counter+=1
                    continue
                else:
                    state = "ERROR"

            elif state==6: #
                if token.isalpha():
                    ulice+=token
                    counter+=1
                elif token=='.':
                    ulice+=token
                    counter+=1
                elif token==" ":
                    state=7 if ulice =="ul." or ulice=="tr." or ulice=="nam." or ulice=="nabr." else "ERROR"
                    ulice += token
                    counter+=1
                else:
                    state="ERROR"
            elif state==7:
                if token.isalpha():
                    ulice+=token
                    counter+=1
                elif token==','and line [counter+1] ==" ":
                    counter+=2
                    state=8
                else:
                    state=="ERROR"

            elif state==8: #psc
                if token in digits:
                    psc+=token
                    counter+=1
                elif counter +1<len(line) and token == ',' and line[counter + 1] == " ":
                    if len(psc)==5:
                        counter += 2
                        state=9
                    else:
                        state="ERROR"
                        break
                elif token==" ":
                    counter+=1

                else:
                    state=="ERROR"
                    break

            elif state==9: #mesto
                if token.isalpha():
                    mesto+=token
                    counter+=1
                else:
                    state="ERROR"
                    break

            elif state =="ERROR":
                break


        if state==9:
            print("%s, %s, %s, %s, %s" %(mesto,psc,ulice,krestnijmeno,prijmeni))


makenote()













