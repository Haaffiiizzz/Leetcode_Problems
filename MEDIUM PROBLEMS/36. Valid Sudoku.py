board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]     # for test


for row in board:
    rowDup = row[:]
    while "." in rowDup:
        rowDup.remove(".")
    if len(set(rowDup)) != len(rowDup):
        return False

for column in range(9):
    columnList = []
    for row in board:
        columnList.append(row[column])
    while "." in columnList:
        columnList.remove(".")
        
    if len(set(columnList)) != len(columnList):
        print(columnList)
        return False

for row in range(3):
    for col in range(3):
        gridList = []
        for i in range(3*row, 3*row + 3):
            for j in range(3*col, 3*col+3):
                gridList.append(board[i][j])


        while "." in gridList:
            gridList.remove(".")
        if len(set(gridList)) != len(gridList):
            return False      

return True

