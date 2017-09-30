def tournamentSeeds():
    testCases = int(input("Number of Tournaments: "))
    i = 0
    while i < testCases:
        tourneyInput = input("Tournament Information: ")
        tempInts = [int(s) for s in tourneyInput.split(' ')]
        currentPower = 3
        while 2**currentPower < tempInts[0]:
            currentPower = currentPower + 1
        if 2**currentPower == tempInts[0]:
            invariable = tempInts[0] + 1
            j = 1
            while j < len(tempInts):
                print("Seed " + str(tempInts[j]) + " plays seed " + str(invariable - tempInts[j]) + ".")
                j = j + 1
        else:
            currentPower = currentPower - 1
            topSeeds = tempInts[0] - 2**currentPower
            invariable = tempInts[0] + topSeeds + 1
            j = 1
            while j < len(tempInts):
                if tempInts[j] <= topSeeds:
                    print("Seed " + str(tempInts[j]) + " gets a bye.")
                    j = j + 1
                else:
                    print("Seed " + str(tempInts[j]) + " plays seed " + str(invariable - tempInts[j]) + ".")
                    j = j + 1
        i = i + 1

tournamentSeeds()
