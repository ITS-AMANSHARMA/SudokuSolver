myBoard =   []

#getBoard() is used to get the initial board position
def getBoard(myBoard, quesFile):
    for line in quesFile:
        temp = [int(i) for i in line.strip().split()]
        myBoard.append(temp);


#solveBoard() is used to solve the Sudoku using backtracking method
def solveBoard(B):
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


# printBoard() is used to print the board
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

#findEmpty() is used to find the next empty position in the board
def findEmpty(B):
    for i in range(len(B)):
        for j in range(len(B[0])):
            if B[i][j] == 0:
                return (i,j) # return (row,col)
    
    return None


#validMove() is used to check the validity of the number at that position
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


quesFile = open("UnsolvedSudoku.txt","r")

getBoard(myBoard,quesFile)

solutionFile = open("SolvedSudoku.txt","w")

#Solving the actual board
printBoard(myBoard,solutionFile)
solutionFile.write("\n--------------------------------------------------------------------------\n\n\n")
solveBoard(myBoard)
printBoard(myBoard,solutionFile)

#Closing both the Unsolved and Solved Sudoku file
quesFile.close()
solutionFile.close()

