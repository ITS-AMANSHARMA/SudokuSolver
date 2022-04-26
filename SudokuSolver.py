myBoard =   []

def getBoard(myBoard, quesFile):
    for line in quesFile:
        temp = [int(i) for i in line.strip().split()]
        myBoard.append(temp);

def solveBoard(B):
    # printBoard(B)
    # print("________________________________")
    find = findEmpty(B)
    if not find:
        return True
    else:
        row,col = find
    for i in range(1,10):
        if validMove(B,i,(row,col)):
            B[row][col] = i
            if solveBoard(B):
                return True
            B[row][col] = 0

    return False

def printBoard(B,solFile):
    for i in range(len(B)):
        if i%3 == 0 and i!=0:
            solFile.write("- - - - - - - - - - - \n")
        for j in range(len(B[0])):
            if j%3 == 0 and j!=0:
                solFile.write("| ")
            if j == 8:
                solFile.write(str(B[i][j])+"\n")
            else:
                solFile.write(str(B[i][j]) + " ")
    solFile.write("\n")

def findEmpty(B):
    for i in range(len(B)):
        for j in range(len(B[0])):
            if B[i][j] == 0:
                return (i,j) # return (row,col)
    return None

def validMove(B,num,pos):
    #Checking row
    for i in range(len(B[0])):
        if i != pos[1] and B[pos[0]][i] == num:
            return False
    
    #Checking column
    for i in range(len(B)):
        if i != pos[0] and B[i][pos[1]] == num:
            return False
    
    #Checking Box
    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3,box_y*3+3):
        for j in range(box_x*3,box_x*3+3):
            if B[i][j] == num and (i,j) != pos:
                return False
    
    return True

# printBoard(myBoard)
# print(findEmpty(myBoard))
# myBoard[0][2] = 6
# printBoard(myBoard)
# print(validMove(myBoard,6,(0,2)))
quesFile = open("UnsolvedSudoku.txt","r")

getBoard(myBoard,quesFile)

# print(myBoard)
# print(type(myBoard))
# print(type(myBoard[0]))
# print(type(myBoard[0][0]))
solutionFile = open("SolvedSudoku.txt","w")

solveBoard(myBoard)
printBoard(myBoard,solutionFile)

solutionFile.close()

