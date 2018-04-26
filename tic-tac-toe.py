import numpy as np
import random
import time
import matplotlib.pyplot as plt1

player=1

# creates board of 3X3, initialized with all zeros.
#--> called in play_game()
def create_board():
    return np.zeros((3,3),np.int8)

# places players marker on position specified.
def place(board,player,position):
    if(not board[position]):
        board[position] = player
    return board
  
# checks for all empty positions
# on board(positions that have 0)  
# ie. positions where both players haven't 
# placed their markers.
def possibilities(board):
    row ,col = np.where(board==0)
    available = []
    for x in range(0,len(row)):
        available.append(tuple([row[x],col[x]]))
    return available 
    
# places specified players marker
# on random available position on board.
#--> called in play_game()
def random_place(board,player):
    board = place(board,player,random.choice(possibilities(board)))
    return board 
 
# checks whether specified player has got
# all his marker, on any row of the board.  
def row_win(board,player):
    for row in range(3):
        decision = all(board[row,:]==player)
        if(decision):
            return True
    return False

# checks whether specified player has got
# all his marker, on any column of the board.      
def col_win(board,player):
    for col in range(3):
        decision = all(board[:,col]==player)
        if(decision):
            return True
    return False

# checks whether specified player has got
# all his marker, on any diagonal of the board.    
def diag_win(board,player):
    diag1=[]
    diag2=[]
    for i in range(0,len(board)):
        diag1.append(board[i,i]==player)
        diag2.append(board[i,len(board)-1-i]==player)
    decision1 = all(diag1)
    decision2 = all(diag2)
    if(decision1 or decision2):
        return True
    return False

# evaluates if any of the player's
# wins and returns that player's number. 
# if board is full -1 is returned.
# else 0 is returned.
#-->  called in play_game()
def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if( row_win(board,player) or col_win(board,player) or diag_win(board,player)):
            winner=player
            break
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner
    
# main call to start the game.chances of player-1 winning are less.
# calls --> create_board()
# calls --> evaluate()
# calls --> random()
def play_game():
    board = create_board()
    global player
    while(True):
        #print 
        #print board
        winner = evaluate(board)
        if(winner != 0):
            return winner
        random_place(board,player)
        if(player==1):
            player = 2
        else:
            player = 1

# main call to start the game.chances of player-1 winning are more.
# calls --> create_board()
# calls --> evaluate()
# calls --> random()            
def play_strategic_game():
    board, winner = create_board(), 0
    board[1,1] = 1
    while winner == 0:
        for player in [2,1]:
            # use `random_place` to play a game, and store as `board`.
            random_place(board, player)
            # use `evaluate(board)`, and store as `winner`.
            winner = evaluate(board)
            if winner != 0:
                break
    return winner


x=play_strategic_game()

if(x==1):
    print "Player 1 wins"
elif(x==2):
    print "Player 2 wins"
else:
    print "DRAW"


# evaluating results after multiple games(future scope)
'''w=[]

start_time = time.time()
for i in range(1000):
    x=play_strategic_game()
    if(x!=-1):
        w.append(x)
    else:
        w.append(3)
end_time = time.time()
avg = end_time-start_time
print (avg)
plt1.hist(w,bins = np.linspace(0.5,3.5,4))

plt1.savefig("strategic.jpeg")
'''

# calling functions
#board = create_board() 
#board = place(board,player_1,(0,0))
#possibilities(board)
#board = random_place(board,player_2)
#row_win(board,player_1)
#col_win(board,player_1)
#diag_win(board,player_2)
#evaluate(board)
