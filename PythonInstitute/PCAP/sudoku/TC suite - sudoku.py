
def validateSudoku(records):

    def sortedCharsAreEqual(sortedRecord):
        #print("printing sorted record:")
        #print(sortedRecord)
        for i in range(0, len(sortedRecord)):
            #print("i + 1 =", i+1)
            #print("sortedRecord[i] =", sortedRecord[i])
            if not str(i + 1) == sortedRecord[i]:
                #print("Failing")
                return False
        return True

    # 0. Pasar los records a un board ( una lista de listas de chars).
    board = [[[i for i in row] for row in rows] for rows in records]

    # 1. Validate rows.
    for rows in board:
        for row in rows:
            #print("printing row:")
            #print(row)
            sortedRow = sorted(row)
            #print("comparing rows:")
            if not sortedCharsAreEqual(sortedRow):
                print("Failed in rows")
                return "No"

    # 2. Validate columns.
    for i in range(0, len(board)):
        col = ""
        for j in range(0, 9):
            col += board[j][0][i]
        sortedCol = sorted(col)
        if not sortedCharsAreEqual(sortedCol):
            print("Failed in cols")
            return "No"

    # 3. Validate tiles.
    start_i = start_j = 0
    stop_i = stop_j = 3
    counter = 0
    tileX = ""

    while counter < 9:

        for i in range(start_i, stop_i):
            for j in range(start_j, stop_j):
                tileX += board[i][0][j]

        sortedTile = sorted(tileX)
        if not sortedCharsAreEqual(sortedTile):
            print("Failed in tiles")
            return "No"
        tileX = ""
        start_i = stop_i
        stop_i += 3
        counter += 1

        if counter == 3:
            start_i = 0
            stop_i = 3
            start_j += 3
            stop_j += 3
        elif counter == 6:
            start_i = 0
            stop_i = 3
            start_j += 3
            stop_j += 3

    return "Yes"


testBoard = [
    [
        # TC 1 - All rows, cols and tiles valid
        ["295743861"],
        ["431865927"],
        ["876192543"],
        ["387459216"],
        ["612387495"],
        ["549216738"],
        ["763524189"],
        ["928671354"],
        ["154938672"],
    ],
    [
        # TC 2 - Invalid 1st Row
        ["295743961"],
        ["431865927"],
        ["876192543"],
        ["387459216"],
        ["612387495"],
        ["549216738"],
        ["763524189"],
        ["928671354"],
        ["154938672"],
    ],
    [
        # TC 3 - Invalid last row
        ["295743861"],
        ["431865927"],
        ["876192543"],
        ["387459216"],
        ["612387495"],
        ["549216738"],
        ["763524189"],
        ["928671354"],
        ["154935672"],
    ],
    [
        # TC 4 - Invalid 1st column
        ["295743861"],
        ["431865927"],
        ["876192543"],
        ["387459216"],
        ["612387495"],
        ["549216738"],
        ["976352418"],
        ["928671354"],
        ["154938672"],
    ],
    [
        # TC 5 - Invalid last column
        ["295743861"],
        ["431865927"],
        ["876192543"],
        ["387459216"],
        ["612387495"],
        ["549216738"],
        ["763524189"],
        ["286713549"],
        ["154938672"],
    ],
    [
        # TC 6 - Invalid 1st tile
        ["189763524"],
        ["354928671"],
        ["671254938"],
        ["862195743"],
        ["927431865"],
        ["543876192"],
        ["216387459"],
        ["495612387"],
        ["738549216"],
    ],
    [
        # TC 7 - Invalid non 1st tile
        ["743862195"],
        ["865927431"],
        ["192543876"],
        ["459216387"],
        ["387495612"],
        ["216738549"],
        ["524189763"],
        ["671354928"],
        ["938671254"]
    ]
]

testObjective = ["Valid rows, valid columns and valid tiles",
                "Invalid 1st row",
                "Invalid last row",
                "Invalid 1st col",
                "Invalid last col",
                "Invalid 1st tile",
                "Invalid non 1st tile"]
expectedResult = ["Yes", "No", "No", "No", "No", "No", "No"]

for i in range(0, len(testBoard)):
    functionResult = validateSudoku(testBoard[i])
    print("TC", i+1, ": ", testObjective[i], sep="")
    print("Actual result:\t\t", functionResult)
    print("Expected result:\t", expectedResult[i])
    if functionResult == expectedResult[i]:
        print("PASSED\n")
    else:
        print("FAILED\n")
