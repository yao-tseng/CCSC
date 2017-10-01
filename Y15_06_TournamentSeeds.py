def tournamentSeeds():
    testCases = int(input("Number of Tournaments: "))                                                               #input for number of test cases
    i = 0                                                                                                           #set index for number of test cases
    while i < testCases:                                                                                            #iterate for each test case
        tourneyInput = input("Tournament Information: ")                                                            #input for number of players and three player seeds
        tempInts = [int(s) for s in tourneyInput.split(' ')]                                                        #transform string input into an array of numbers
        currentPower = 3                                                                                            #set power count to 3 (2**3 == 8)
        while 2**currentPower < tempInts[0]:                                                                        #find the x where 2**x is the closest to number of players
            currentPower = currentPower + 1                                                                         #increase power one level
        if 2**currentPower == tempInts[0]:                                                                          #check if current power level equals number of players
            invariable = tempInts[0] + 1                                                                            #on true, combine high and low seed for invariable
            j = 1                                                                                                   #set index for player count
            while j < len(tempInts):                                                                                #iterate for player count
                print("Seed " + str(tempInts[j]) + " plays seed " + str(invariable - tempInts[j]) + ".")            #output player seed and their opponent seed
                j = j + 1                                                                                           #advance index for player count
        else:                                                                                                       #check if current power level does not equal number of players
            currentPower = currentPower - 1                                                                         #lower power level to be under the player numbers
            topSeeds = tempInts[0] - 2**currentPower                                                                #find how many byes there will be
            invariable = tempInts[0] + topSeeds + 1                                                                 #combine high and lowest non-bye seed for invariable
            j = 1                                                                                                   #set index for player count
            while j < len(tempInts):                                                                                #iterate for player count
                if tempInts[j] <= topSeeds:                                                                         #check if player seed gets a bye
                    print("Seed " + str(tempInts[j]) + " gets a bye.")                                              #on true, output player seed bye
                    j = j + 1                                                                                       #advance index for player count
                else:                                                                                               #check if player seed plays another player
                    print("Seed " + str(tempInts[j]) + " plays seed " + str(invariable - tempInts[j]) + ".")        #on true, output player seed and their opponent seed
                    j = j + 1                                                                                       #advance index for player count
        i = i + 1                                                                                                   #advance index for number of test cases

tournamentSeeds()
