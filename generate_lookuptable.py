#v.1
import string
import random
import json

InClear = []
InHashed = []
seed = input("What should your seed be? The same seed will generate the same Table: ")

for i in string.printable:
    InClear.append(i)
    

for i in InClear:
    random.seed(str(seed) + str(i))
    InHashed.append(random.randint(0,50000))


dic = {
    "InHashed": InHashed,
    "InClear": InClear
}
f = open("lookuptable.json", "w")
json.dump(dic, f)