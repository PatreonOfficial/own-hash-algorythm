import math
#HashingAlgorythm by PatreonOfficial


InClear = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","-","_"]
InHashed = ["0","1","2","3","4","5","6","7","8","9","6587","1598","6574","657","465","743","19","456","657","859","35","456","76","78","564","23","132","156","456","54","4656","789","15","465","1596","657","651","657","15","189","1798","415","657","4189","741","198","657","198","987","651","6541","561","651","657","67","657","465","46849","1655","156","65735","165","654","185"]
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
        #this = int(this)
        

while (True):
    ConvToNumb(list(input("Any string: ")))
    #print (n)
    Hashing(n)
    lol = int(this)
    print(lol)
    print("Lenghtening operations: " + str(t))
