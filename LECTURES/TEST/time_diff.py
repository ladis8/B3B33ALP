#singlerowinput


def readinput():
    time1 = input()
    time2 = input()
    try:
        if int (time1[:2]) < 24 and int (time2 [:2]) <24:
            hours = int (time1[:2]) - int (time2 [:2])
        else:
            return False
        if int (time1 [3:5]) <60 and int (time2 [3:5])<60:
            minutes = int (time1 [3:5]) - int (time2 [3:5])
        else:
            return False
        if int (time1 [6:8])< 60 and  int (time2 [6:8])<60:
            seconds = int (time1 [6:8])- int (time2 [6:8])
        else:
            return False
        #print(hours, minutes,seconds)
        return  abs (hours *3600 + minutes*60+seconds)

    except (Exception):
        return False



def timereturn (secondsnum):
    hours = secondsnum //3600
    secondsnum = secondsnum - hours*3600
    minutes = secondsnum//60
    secondsnum = secondsnum - minutes*60

    seconds = secondsnum
    #print(seconds)
    return  hours,minutes,seconds


def printoutput(hours, minutes, seconds):

    hours = str(hours)
    if len(hours)==1:
        hours="0"+hours
    minutes = str(minutes)
    if len(minutes) == 1:
        minutes = "0" + minutes
    seconds = str(seconds)
    if len(seconds) == 1:
        seconds = "0" + seconds
    return ("%sh%sm%ss" %(hours,minutes,seconds))



a = readinput()

if a == False:
    print("ERROR")
else:
    (hours, minutes, seconds) = timereturn(a)
    print(printoutput(hours,minutes, seconds))