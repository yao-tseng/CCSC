def wordScramble():
    numberStrings = int(input("Number of Input Strings: "))     #input for number of strings
    i = 0                                                       #set index for string amount
    while i < numberStrings:                                    #iterate for each string
        scrambleText = input("Input " + str(i+1) + ": ")        #input for each string
        plainText = scrambleText + "A"                          #creation of extra spacing for if statement
        j = 0                                                   #set index for individual string
        while j < len(scrambleText):                            #iterate through the individual string
            if plainText[j] == "A" and plainText[j+1] != "A":   #check letter and next letter for "A"
                a = scrambleText[0:j]                           #splice section before letter "A"
                b = scrambleText[j:j+2]                         #splice section with "A" and letter after
                b = b[::-1]                                     #reverse second section
                c = scrambleText[j+2:]                          #splice section after letters swapped
                scrambleText = a + b + c                        #concatenate spliced sections
                j = j + 2                                       #advance index past the two letters
            else:                                               #everything else - 
                j = j + 1                                       #advance index to next letter
        print(scrambleText)                                     #output scrambled word
        i = i + 1                                               #advance index to next string
        
wordScramble()
