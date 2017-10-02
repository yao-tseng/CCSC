def lettersNotUsed():
    testCases = int(input("Number of Test Cases: "))                            #input for number of test cases
    i = 0                                                                       #set index
    alphaBet = "abcdefghijklmnopqrstuvwxyz"                                     #define comparative string
    while i < testCases:                                                        #iterate for each test case
        emptyString = ""                                                        #define empty output variable
        j = 0                                                                   #set index for alphabet check
        string = (input("Case Number " + str(i + 1) + ": ")).lower()            #input string set to lowercase
        while j < len(alphaBet):                                                #iterate for each letter of the alphabet
            if alphaBet[j] in string:                                           #if letter is in string, advance index
                j = j + 1
            else:                                                               #if not, add to output variable
                emptyString = emptyString + alphaBet[j]
                j = j + 1                                                       #advance index for alphabet check
        print("Letters Missing in Case #" + str(i + 1) + ": " + emptyString)    #output string of missing letters
        i = i + 1                                                               #advance index for test cases
        
lettersNotUsed()
