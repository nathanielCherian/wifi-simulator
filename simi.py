#! python3

from random import randint


packetSize1 = 500
packetSize2 = 500

packetDelay1 = 500
packetDelay2 = 500

playerIn1 = 10
playerIn2 = 10

minRange1 = 15
maxRange1 = 1000

minRange2 = 15
maxRange2 = 1000



class Player():
    _id = 0
    packetSize = 0
    packetDelay = 0
    minRange = 0
    maxRange = 0

    pair = 0
    isPlaying = False
    place = 0

    moves = 0
    pairPC = 0
    points = 0
    totalP = 0
    collisionsC = 0

    def __init__(self, _id, packetSize, packetDelay, minRange, maxRange):
        self._id = _id
        self.packetSize = packetSize
        self.packetDelay = packetDelay
        self.minRange = minRange
        self.maxRange = maxRange
        self.setRand()
    
    def setRand(self):
        self.place = randint(0, self.minRange)


def zeroCheck(plist):   #returns index of 0 or 1
    l = []
    for p in plist:
        l.append(p.place)
    if 0 in l:
        return l.index(0)
    else:
        return -1

def collision(plist, minRange): #will alter plist if #0 > 1

    l = []
    for p in plist:
        l.append(p.place)
    
    indeces = [i for i, z in enumerate(l) if z == 0]

    while len(indeces) > 1:
        for l in indeces:
            if plist[l].minRange < plist1[l].maxRange:
                plist[l].minRange = plist[l].minRange*2
            plist[l].setRand()
            plist[l].collisionsC += 1
            l = []
            for p in plist:
                l.append(p.place)
            indeces = [i for i, z in enumerate(l) if z == 0]

    for p in plist:
        p.minRange = minRange

def shift(plist, otherplist): #shifts its pair isnt playign THIS WORKS 
    for p in plist:
        if p.pair != 0:
            l = []
            for p in otherplist:
                l.append(p.pair)
            if p.pair in l:
                if otherplist[l.index(p.pair)].isPlaying == False:
                    p.place -= 1
        else:
            p.place -= 1

def findPair(plist, pair):
    for i in range(len(plist)):
        if plist[i].pair == pair:
            return i
    return -1 #should never get here(method only called if pair found)
     
plist1 = []
for i in range(playerIn1):
    plist1.append(Player(i, packetSize1,packetDelay1,minRange1,maxRange1))

plist2 = []
for i in range(playerIn2):
    plist2.append(Player(i, packetSize2,packetDelay2,minRange2,maxRange2))


y = 0
z = 0
for i in range(1000000):

    collision(plist1, minRange1)
    l = []
    for p in plist1:
        l.append(p.place)

    zc = zeroCheck(plist1) # holding on as variable
    if y==i and zeroCheck(plist1) >= 0: #found something with a zero

        if plist1[zc].pair != 0 and z == i: #checks for pairs and availability

        

    if y == i:
        shift(plist1, plist2) 


