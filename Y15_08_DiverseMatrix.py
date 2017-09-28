def DiverseMatrix():
    numberMatrix = int(input("Number of Matrices: "))                       #input for number of matrices
    matrixArray = []                                                        #final set of matrices (not needed)
    i = 0                                                                   #set index
    while i < numberMatrix:                                                 #iterate for each matrix
        rowsColumns = input("Rows and Columns: ")                           #input for number of rows and columns
        intRowsColumns = [int(s) for s in rowsColumns.split(' ')]           #transform string input into array of numbers
        currentRow = 0                                                      #set up current row input
        matrixTemp = []                                                     #reset empty matrix for row value input loop (not needed)
        sums = []                                                           #reset array for sum of each row
        while currentRow < intRowsColumns[0]:                               #iterate for each row
            rowValues = (input(str(currentRow+1) + " Row Values: "))        #input for row values
            listRowVal = [int(s) for s in rowValues.split(' ')]             #transform string input into array of numbers
            matrixTemp = matrixTemp + [listRowVal]                          #concatenate rows to matrix (not needed)
            sums = sums + [sum(listRowVal)]                                 #concatenate to list of sums
            currentRow = currentRow + 1                                     #advance row index
        if len(set(sums)) == len(sums):                                     #compare row sums for diversity
            print("yes")
        else:
            print("no")
        matrixArray = matrixArray + [matrixTemp]                            #concatenate matrix to list of matrices (not needed)
        i = i + 1                                                           #advance matrix index
    print("Final 3D Matrix: ")
    print(matrixArray)
DiverseMatrix()
