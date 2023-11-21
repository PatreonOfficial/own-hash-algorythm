#v.1
import math
import re
import json
#HashingAlgorythm by PatreonOfficial

#load dictionarys
f = open("lookuptable.json", "r")
data = json.load(f)
InHashed = data["InHashed"]
InClear = data["InClear"]


Hash = 0


def ConvToNumb(clear):
    global n
    n = ""
    #convert to numbers
    for x in clear:
        y = InHashed[InClear.index(str(x))]
        n = n + str(y)
    n = int(n)
def Hashing(Hash):
    global t
    global this
    this = (Hash*(Hash%56))
    t = 0
    
    while(len(str(int(int(this)))) != 25):
        if(len(str(int(this))) > 25):
            this = this/2
            t += 1
        if(len(str(int(this)))<25):
            this = this *3
            t += 1
def makeReadable(Hash):
    global readme
    readme = ""
    count = 0
    for i in re.findall('.{1,5}', str(Hash)):
        if count == 4:
            readme += i
        else:
            readme += i + "-"
        count += 1

while (True):
    ConvToNumb(list(input("Any string: ")))
    Hashing(n)
    lol = int(this)
    makeReadable(lol)
    print(readme)
    #print("Lenghtening operations: " + str(t))
