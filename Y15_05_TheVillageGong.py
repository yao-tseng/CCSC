def villageGong():
    testCases = int(input("Number of Test Cases: "))        #input for number of test cases
    i = 0                                                   #set index
    while i < testCases:                                    #iterate for each test case
        timeInput = input("Test Case " + str(i+1) + ": ")   #input time for each test case
        HMS = [int(s) for s in timeInput.split(":")]        #transform str input into int array
        totalSeconds = (HMS[1] * 60) + HMS[2]               #find total seconds from minutes + seconds
        secondsLeft = 600 - (totalSeconds % 600)            #find remaining seconds out of 10 minutes
        print(secondsLeft)                                  #output seconds
        i = i + 1                                           #advance index
        
villageGong()
