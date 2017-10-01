def villageGong():
    testCases = int(input("Number of Test Cases: "))
    i = 0
    while i < testCases:
        timeInput = input("Test Case " + str(i+1) + ": ")
        HMS = [int(s) for s in timeInput.split(":")]
        totalSeconds = (HMS[1] * 60) + HMS[2]
        secondsLeft = 600 - (totalSeconds % 600)
        print(secondsLeft)
        i = i + 1
        
villageGong()
