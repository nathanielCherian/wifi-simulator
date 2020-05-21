from random import randint

class Player():

    accWait = [0]

    def __init__(self):
        self.accWait = [0]
        


plist = []
for i in range(5):
    plist.append(Player())

for i in range(10):

    for p in plist:
        p.accWait[-1] += 1


    if i == 6:
        plist[4].accWait.append(0)
        print("hi")


for i in range(5):
    print(plist[i].accWait)

