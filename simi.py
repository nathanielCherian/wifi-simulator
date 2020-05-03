#! python3

from random import randint



def runSim(param):
    print("started")
    packetSize1 = int(param['size1'])
    packetSize2 = int(param['size2'])

    packetDelay1 = int(param['delay1'])
    packetDelay2 = int(param['delay2'])

    playerIn1 = int(param['players1'])
    playerIn2 = int(param['players2'])

    minRange1 = int(param['minR1'])
    maxRange1 = int(param['maxR2'])

    minRange2 = int(param['minR1'])
    maxRange2 = int(param['maxR2'])

    pairs = int(param['pairs'])

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

        def pairRand(self):
            self.place += randint(0, self.minRange)

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

    def shift(plist, otherplist): #shifts its pair isnt playign THIS WORKS Also sets isplaying to false
        for p in plist:
            if p.pair != 0:
                l = []
                for pl in otherplist:
                    l.append(pl.pair)
                if p.pair in l:
                    if otherplist[l.index(p.pair)].isPlaying == False:
                        p.place -= 1
            else:
                p.place -= 1

            p.isPlaying = False

    def findPair(plist, pair):
        for i in range(len(plist)):
            if plist[i].pair == pair:
                return i
        return -1 #should never get here(method only called if pair found)
        
    def setPair(plistOne, plistTwo):
        for i in range(pairs):
            plistOne[i].pair = i+1
            plistTwo[i].pair = i+1

    plist1 = []
    plist2_1 = []
    plist3_1 = []
    for i in range(playerIn1):
        plist1.append(Player(i, packetSize1,packetDelay1,minRange1,maxRange1))
        plist2_1.append(Player(i, packetSize1,packetDelay1,minRange1,maxRange1))
        plist3_1.append(Player(i, packetSize1,packetDelay1,minRange1,maxRange1))

    plist2 = []
    plist2_2 = []
    plist3_2 = []
    for i in range(playerIn2):
        plist2.append(Player(i, packetSize2,packetDelay2,minRange2,maxRange2))
        plist2_2.append(Player(i, packetSize2,packetDelay2,minRange2,maxRange2))
        plist3_2.append(Player(i, packetSize2,packetDelay2,minRange2,maxRange2))

    setPair(plist1, plist2)
    setPair(plist2_1, plist2_2)
    setPair(plist3_1, plist3_2)


    y = 0
    z = 0
    y2 = 0
    z2 = 0
    y3 = 0
    z3 = 0
    for i in range(1000000):

        collision(plist1, minRange1)
        zc = zeroCheck(plist1) # holding on as variable
        if y==i and zc >= 0: #found something with a zero

            if plist1[zc].pair != 0 and z == i: #checks for pairs and availability
                pr = findPair(plist2, plist1[zc].pair)

                plist2[pr].pairPC += 1
                plist2[pr].minRange = minRange2
                plist2[pr].moves += 1
                plist2[pr].isPlaying = True
                plist2[pr].setRand()
                plist2[pr].place += packetDelay2
                z += packetSize2
            
            plist1[zc].minRange = minRange1
            plist1[zc].moves += 1
            plist1[zc].isPlaying = True
            plist1[zc].setRand()
            plist1[zc].place += packetDelay1
            y += packetSize1


        collision(plist2, minRange2)
        zc = zeroCheck(plist2)
        if z == i and zc >= 0:

            if plist2[zc].pair != 0 and y == i:
                pr = findPair(plist1, plist2[zc].pair)

                plist1[pr].pairPC += 1
                plist1[pr].minRange = minRange1
                plist1[pr].moves += 1
                plist1[pr].isPlaying = True
                plist1[pr].setRand()
                plist1[pr].place += packetDelay1
                y += packetSize1

            plist2[zc].minRange = minRange2
            plist2[zc].moves += 1
            plist2[zc].isPlaying = True
            plist2[zc].setRand()
            plist2[zc].place += packetDelay2
            z += packetSize2

        if y == i:
            shift(plist1, plist2)
            y += 1

        if z == i:
            shift(plist2, plist1)
            z += 1

    #HERE ON IS METHOD2(3)

        collision(plist2_1, minRange1)
        zc = zeroCheck(plist2_1) # holding on as variable
        if y2==i and zc >= 0: #found something with a zero

            if plist2_1[zc].pair != 0 and z2 == i: #checks for pairs and availability
                pr = findPair(plist2_2, plist2_1[zc].pair)

                plist2_2[pr].pairPC += 1
                plist2_2[pr].minRange = minRange2
                plist2_2[pr].moves += 1
                plist2_2[pr].isPlaying = True
                plist2_2[pr].pairRand()
                plist2_2[pr].place += packetDelay2
                z2 += packetSize2
            
            plist2_1[zc].minRange = minRange1
            plist2_1[zc].moves += 1
            plist2_1[zc].isPlaying = True
            plist2_1[zc].setRand()
            plist2_1[zc].place += packetDelay1
            y2 += packetSize1


        collision(plist2_2, minRange2)
        zc = zeroCheck(plist2_2)
        if z2 == i and zc >= 0:

            if plist2_2[zc].pair != 0 and y2 == i:
                pr = findPair(plist2_1, plist2_2[zc].pair)

                plist2_1[pr].pairPC += 1
                plist2_1[pr].minRange = minRange1
                plist2_1[pr].moves += 1
                plist2_1[pr].isPlaying = True
                plist2_1[pr].pairRand()
                plist2_1[pr].place += packetDelay1
                y2 += packetSize1

            plist2_2[zc].minRange = minRange2
            plist2_2[zc].moves += 1
            plist2_2[zc].isPlaying = True
            plist2_2[zc].setRand()
            plist2_2[zc].place += packetDelay2
            z2 += packetSize2

        if y2 == i:
            shift(plist2_1, plist2_2)
            y2 += 1

        if z2 == i:
            shift(plist2_2, plist2_1)
            z2 += 1

    # HERE IS METHOD 3

        collision(plist3_1, minRange1)
        zc = zeroCheck(plist3_1) # holding on as variable
        if y3==i and zc >= 0: #found something with a zero

            if plist3_1[zc].pair != 0 and z3 == i: #checks for pairs and availability
                pr = findPair(plist3_2, plist3_1[zc].pair)

                plist3_2[pr].pairPC += 1
                plist3_2[pr].minRange = minRange2
                plist3_2[pr].moves += 1
                plist3_2[pr].isPlaying = True
                plist3_2[pr].setRand()
                plist3_2[pr].place += packetDelay2
                z3 += packetSize2
            
            plist3_1[zc].minRange = minRange1
            plist3_1[zc].moves += 1
            plist3_1[zc].isPlaying = True
            plist3_1[zc].setRand()
            plist3_1[zc].place += packetDelay1
            y3 += packetSize1


        collision(plist3_2, minRange2)
        zc = zeroCheck(plist3_2)
        if z3 == i and zc >= 0:

            if plist3_2[zc].pair != 0 and y3 == i:
                pr = findPair(plist3_1, plist3_2[zc].pair)

                plist3_1[pr].pairPC += 1
                plist3_1[pr].minRange = minRange1
                plist3_1[pr].moves += 1
                plist3_1[pr].isPlaying = True
                plist3_1[pr].setRand()
                plist3_1[pr].place += packetDelay1
                y3 += packetSize1

            plist3_2[zc].minRange = minRange2
            plist3_2[zc].moves += 1
            plist3_2[zc].isPlaying = True
            plist3_2[zc].setRand()
            plist3_2[zc].place += packetDelay2
            z3 += packetSize2

        if y3 == i:
            shift(plist3_1, plist3_2)
            y3 += 1

        if z3 == i:
            shift(plist3_2, plist3_1)
            z3 += 1

    avgMoveUP1 = [0,0,0]
    avgMoveP1 = [0,0,0]
    avgMoveUP2 = [0,0,0]
    avgMoveP2 = [0,0,0]
    for i in range(playerIn1):
        if i < pairs:
            avgMoveP1[0] += plist1[i].moves/pairs
            avgMoveP1[1] += plist2_1[i].moves/pairs
            avgMoveP1[2] += plist3_1[i].moves/pairs

        else:
            #print(str(plist1[i].moves) + " " + str(plist1[i].moves/playerIn1-pairs))
            avgMoveUP1[0] += plist1[i].moves/(playerIn1-pairs)
            avgMoveUP1[1] += plist2_1[i].moves/(playerIn1-pairs)
            avgMoveUP1[2] += plist3_1[i].moves/(playerIn1-pairs)

    for i in range(playerIn2):
        if i < pairs:

            avgMoveP2[0] += plist2[i].moves/pairs
            avgMoveP2[1] += plist2_2[i].moves/pairs
            avgMoveP2[2] += plist3_2[i].moves/pairs
        else:
            #print(str(plist1[i].moves) + " " + str(plist1[i].moves/playerIn1-pairs))

            avgMoveUP2[0] += plist2[i].moves/(playerIn2-pairs)
            avgMoveUP2[1] += plist2_2[i].moves/(playerIn2-pairs)
            avgMoveUP2[2] += plist3_2[i].moves/(playerIn2-pairs)


    for p in plist1:
        print(str(p.moves) +" : " + str(p.collisionsC) + " : " + str(p.pairPC))

    print("\n\n")
    for p in plist2:
        print(str(p.moves) +" : " + str(p.collisionsC) + " : " + str(p.pairPC))

    print("\nsecond method")

    for p in plist2_1:
        print(str(p.moves) +" : " + str(p.collisionsC) + " : " + str(p.pairPC))

    print("\n\n")
    for p in plist2_2:
        print(str(p.moves) +" : " + str(p.collisionsC) + " : " + str(p.pairPC))

    print("\nthird method")

    for p in plist3_1:
        print(str(p.moves) +" : " + str(p.collisionsC) + " : " + str(p.pairPC))

    print("\n\n")
    for p in plist3_2:
        print(str(p.moves) +" : " + str(p.collisionsC) + " : " + str(p.pairPC))


    return [avgMoveP1, avgMoveUP1, avgMoveP2, avgMoveUP2]