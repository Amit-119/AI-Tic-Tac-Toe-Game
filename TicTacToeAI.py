import random as rd

theBoard = [None,' ',' ',' ',' ',' ',' ',' ',' ',' ']

def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])


def wins(board):
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

def choose(board):
    #attacking the player's mistake
    a = [board[1],board[5],board[9]]
    b = [1,5,9]
    if a.count('O')==2 and ' ' in a:
        return b[a.index(' ')]
    a = [board[3],board[5],board[7]]
    b = [3,5,7]
    if a.count('O')==2 and ' ' in a:
        return b[a.index(' ')]
    a = [board[2],board[5],board[8]]
    b = [2,5,8]
    if a.count('O')==2 and ' ' in a:
        return b[a.index(' ')]
    a = [board[4],board[5],board[6]]
    b = [4,5,6]
    if a.count('O')==2 and ' ' in a:
        return b[a.index(' ')]
    a = [board[1],board[2],board[3]]
    b = [1,2,3]
    if a.count('O')==2 and ' ' in a:
        return b[a.index(' ')]
    a = [board[1],board[4],board[7]]
    b = [1,4,7]
    if a.count('O')==2 and ' ' in a:
        return b[a.index(' ')]
    a = [board[3],board[6],board[9]]
    b = [3,6,9]
    if a.count('O')==2 and ' ' in a:
        return b[a.index(' ')]
    a = [board[7],board[8],board[9]]
    b = [7,8,9]
    if a.count('O')==2 and ' ' in a:
        return b[a.index(' ')]
    
    #defence for players making pair of 3 X's
    a = [board[1],board[5],board[9]]
    b = [1,5,9]
    if a.count('X')==2 and ' ' in a:
        print(b)
        return b[a.index(' ')]
    a = [board[3],board[5],board[7]]
    b = [3,5,7]
    if a.count('X')==2 and ' ' in a:
        print(b)
        return b[a.index(' ')]
    a = [board[2],board[5],board[8]]
    b = [2,5,8]
    if a.count('X')==2 and ' ' in a:
        print(b)
        return b[a.index(' ')]
    a = [board[4],board[5],board[6]]
    b = [4,5,6]
    if a.count('X')==2 and ' ' in a:
        print(b)
        return b[a.index(' ')]
    a = [board[1],board[2],board[3]]
    b = [1,2,3]
    if a.count('X')==2 and ' ' in a:
        print(b)
        return b[a.index(' ')]
    a = [board[1],board[4],board[7]]
    b = [1,4,7]
    if a.count('X')==2 and ' ' in a:
        print(b)
        return b[a.index(' ')]
    a = [board[3],board[6],board[9]]
    b = [3,6,9]
    if a.count('X')==2 and ' ' in a:
        print(b)
        return b[a.index(' ')]
    a = [board[7],board[8],board[9]]
    b = [7,8,9]
    if a.count('X')==2 and ' ' in a:
        print(b)
        return b[a.index(' ')]
    
    #strategy to counter the player
    if board[5] == ' ':
        return 5
    elif board[5] == 'X':
        option = [1,3,7,9]
        for i in option:
            if board[i] != ' ':
                option.remove(i)
        print("Options:",option)
        if len(option)!=0:
            return (rd.choice(option))
    
    if board[1] == 'X':
        if board[9] == ' ':
            return 9
        else:
            option = [3,7]
            for i in option:
                if board[i] != ' ':
                    option.remove(i)
            print("Options:",option)
            if len(option)!=0:
                return (rd.choice(option))
    if board[3] == 'X':
        if board[7] == ' ':
            return 7
        else:
            option = [1,9]
            for i in option:
                if board[i] != ' ':
                    option.remove(i)
            print("Options:",option)
            if len(option)!=0:
                return (rd.choice(option))
    if board[7] == 'X':
        if board[3] == ' ':
            return 3
        else:
            option = [1,9]
            for i in option:
                if board[i] != ' ':
                    option.remove(i)
            print("Options:",option)
            if len(option)!=0:
                return (rd.choice(option))
    if board[9] == 'X':
        if board[1] == ' ':
            return 1
        else:
            option = [3,7]
            for i in option:
                if board[i] != ' ':
                    option.remove(i)
            print("Options:",option)
            if len(option)!=0:
                return (rd.choice(option))
    #finally useless moves for formality
    print(board.index(' '))
    return board.index(' ')


print("You have 'X' and I have 'O'")

while ' ' in theBoard:
    turn = 'X'
    printBoard(theBoard)
    print("\nYour turn. Move on which index? ")
    move = int(input())%10
    if theBoard[move] != ' ':
        print("That position is already occupied.")
        continue
    theBoard[move] = turn
    printBoard(theBoard)
    if wins(theBoard):
        print("Congrats! You won.")
        break
    if ' ' not in theBoard:
        break
    turn = 'O'
    move = choose(theBoard)
    print("\nI move on index ",move)
    theBoard[move] = turn
    if wins(theBoard):
        print("Oops... I won :):)")
        break

printBoard(theBoard)



    
