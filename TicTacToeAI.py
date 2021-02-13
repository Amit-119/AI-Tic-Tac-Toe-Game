#--------- Developed by Amit Singh ----------
#--------- NIT Manipur ----------------------




#Status of the Board, Initially empty
theBoard = [None,' ',' ',' ',' ',' ',' ',' ',' ',' ']
computer,opponent = "X","O"


#Function to print the current status of Board
def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])



#Function to check if any moves left in Board
def MovesLeft(Board):
    for box in Board:
        if box == " ":
            return True
    return False


#Evaluation function of the Board for next move
def Evaluate(board):
    for x in [1,4,7]:
        if board[x]==board[x+1]==board[x+2]:
            if board[x]==computer:
                return 100
            elif board[x]==opponent:
                return -100
    for y in [1,2,3]:
        if board[y]==board[y+3]==board[y+6]:
            if board[y]==computer:
                return 100
            elif board[y]==opponent:
                return -100
    if board[1]==board[5]==board[9]:
        if board[5]==computer:
            return 100
        elif board[5]==opponent:
            return -100
    if board[3]==board[5]==board[7]:
        if board[5]==computer:
            return 100
        elif board[5]==opponent:
            return -100
    return 0



#Minimax function to evaluate score
def MiniMax(board,depth,isMax):
    score = Evaluate(board)
    if score == 100 or score == -100:
        return score

    if not MovesLeft(board):
        return 0

    if isMax:
        best = -10000
        for i in range(1,10):
            if board[i]==" ":
                board[i] = computer
                best = max(best,MiniMax(board,depth+1,not isMax)) - depth
                board[i] = " "
        return best
    
    else:
        best = 10000
        for i in range(1,10):
            if board[i]==" ":
                board[i] = opponent
                best = min(best,MiniMax(board,depth+1,not isMax)) + depth
                board[i] = " "
        return best



#Function to find the next Best move for Computer
def FindBestMove(board):
    bestVal = -10000
    index = -1
    for i in range(1,10):
        if board[i] == " ":
            board[i] = computer
            reward = MiniMax(board,0,False)
            board[i] = " "
            if reward>bestVal:
                bestVal = reward
                index = i
    #print("The maxinum reward is :",bestVal)
    #You can uncomment the above line to see the reward
    #for next move
    return index



#Function to check if move given by player is valid
#This is for smart intellectuals who intentionally give wrong input :)
def isValidMove(board,move):
    if not move.isdigit():
        print("Please enter a number from 1 to 9.\n")
        return False
    move = int(move)
    if move<1 or move>9:
        print("Please enter a number from 1 to 9.\n")
        return False
    if board[move]!=" ":
        print("That index is taken please select a valid index.\n")
        return False
    return True



#Checking if anyone have won the game at rurntime
def Wins(board):
    if board[1]==board[2]==board[3] and board[1] != ' ':
        return True
    if board[1]==board[4]==board[7] and board[1] != ' ':
        return True
    if board[1]==board[5]==board[9] and board[1] != ' ':
        return True
    if board[9]==board[8]==board[7] and board[9] != ' ':
        return True
    if board[9]==board[6]==board[3] and board[9] != ' ':
        return True
    if board[5]==board[3]==board[7] and board[5] != ' ':
        return True
    if board[5]==board[2]==board[8] and board[5] != ' ':
        return True
    if board[5]==board[4]==board[6] and board[5] != ' ':
        return True
    return False



#Utilize all the functions and Plays the game for once
def PlayGame(board):
    while " " in board:
        while True:
            move = input("Enter your move : ")
            if isValidMove(board,move):
                move = int(move)
                board[move] = "O"
                break
        printBoard(board)
        print("\n")
        if Wins(board):
            print("Congrats!! You won.  :)")
            break

        if " " not in board:
            break
        Comp_move = FindBestMove(board)
        print("I choose",Comp_move)
        board[Comp_move] = "X"
        printBoard(board)
        print("\n")
        if Wins(board):
            print("OOps!  I won.  :)")
            break


#Driver code
if __name__=="__main__":
    print("\nYou have 'O' and I have 'X' ")
    indexBoard = [None,'1','2','3','4','5','6','7','8','9']
    print("Select your move according to the index given: ")
    printBoard(indexBoard)
    print("\n")

    board = theBoard
    while True:
        PlayGame(board)
        wish = input("Want to play more?  Press N to exit:  ")
        if wish=="N" or wish=="n":
            break
        board = [None,' ',' ',' ',' ',' ',' ',' ',' ',' ']
        printBoard(board)
        print()



#----------- Developed by Amit Singh --------------------------
