#! python3
import random
from random import randint

irRange1 = 15
irRange2 = 15
packetSize = 300
packetDelay1 = 1
packetDelay2 = 1
pairCap = 3
playground1players = 5
playgroud2players = 2


def collision(plist):
    list = []
    for p in plist:
        list.append(p.place)
    
    indeces = [i for i, z in enumerate(list) if z == 0]

    for l in indeces:
        plist[l].randomRange = plist[l].randomRange*2
        plist[l].setRand()
        plist[l].collisionsC += 1
    
    return plist

def zeroCheck(plist):
    for p in plist:
        if p.place == 0:
            return plist.index(p)
    return -1

def findPair(plist, pair):
    list = []
    for p in plist:
        list.append(p.pair)

    if pair in list:
        return list.index(pair)
    else: 
        return -1

def stopPlaying(plist):
    for player in plist:
        player.isPlaying = False
    return plist

def shifter(plist, otherplist):
    for player in plist:
        player.shift(otherplist)
    return plist

class Player:
    place = 0
    moves = 0
    _id = 0
    pair = 0
    randomRange = irRange1
    pairPullC = 0
    collisionsC = 0
    isPlaying = False

    def __init__(self, count, rrange):
        self._id = count
        self.randomRange = rrange
        self.place = randint(0,self.randomRange)
        
    def setRand(self):
        self.place = randint(0,self.randomRange)

    def pairRand(self):
        self.place = self.place + randint(0,self.randomRange)

    def shift(self, plist):
        if self.pair != 0:
            m = findPair(plist, self.pair)
            if plist[m].isPlaying == False:
                self.place -= 1
        else:
            self.place -= 1



plist1 = []
for i in range(0, playground1players):
    plist1.append(Player(i, irRange1))
    
plist2 = []
for i in range(0, playgroud2players):
    plist2.append(Player(i, irRange2))

plist1[0].pair = 1
plist2[0].pair = 1


y = 0
z = 0

for i in range(0, 1000000):

    plist1 = collision(plist1)
    print(str(zeroCheck(plist1)) + "  " + str(y))
    if y == i and zeroCheck(plist1) >= 0:

        if plist1[zeroCheck(plist1)].pair != 0 and z==i:
            pr = findPair(plist2, plist1[zeroCheck(plist1)].pair)
            plist2[pr].pairPullC += 1

            plist2[pr].randomRange = irRange2
            plist2[pr].moves += 1
            plist2[pr].isPlaying = True
            plist2[pr].setRand()
            plist2[pr].place != packetDelay2
            z += packetSize

        zc = zeroCheck(plist1)
        plist1[zc].randomRange = irRange1
        plist1[zc].moves += 1
        plist1[zc].isPlaying = True
        plist1[zc].setRand()
        plist1[zc].place += packetDelay1
        y += packetSize

    
    plist2 = collision(plist2)
    if z == i and zeroCheck(plist2) >= 0:

        if plist2[zeroCheck(plist2)].pair != 0 and y==i:
            pr = findPair(plist1, plist2[zeroCheck(plist2)].pair)
            plist1[pr].pairPullC +=1

            plist1[pr].randomRange = irRange1
            plist1[pr].moves += 1
            plist1[pr].isPlaying = True
            plist1[pr].setRand()
            plist1[pr].place += packetDelay1
            y += packetSize

        print("act")
        zc = zeroCheck(plist2)
        plist2[zc].randomRange = irRange2
        plist2[zc].moves += 1
        plist2[zc].isPlaying = True
        plist2[zc].setRand()
        plist2[zc].place += packetDelay2
        z += packetSize

    
    if y == i:
        plist1 = stopPlaying(plist1)
        plist1 = shifter(plist1, plist2)
        y += 1

    if z == i:
        plist2 = stopPlaying(plist2)
        plist2 = shifter(plist2, plist1)
        z += 1

    
for player in plist1:
    print(str(player.moves) + "\n")

print('\n\n')

for player in plist2:
    print(str(player.moves) + "\n")




