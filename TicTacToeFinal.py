
# <br>To clear the screen between moves:
# 
#     from IPython.display import clear_output
#     clear_output()
#     
# Note that clear_output() will only work in jupyter. To clear the screen in other IDEs, consider:
# 
#     print('\n'*100)
#     
# This scrolls the previous board up out of view. Now on to the program!
# %% [markdown]
# **Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.**

# %%
from IPython.display import clear_output

def display_board(board):
    clear_output()

    print(' ' + ' ' +board[7] + '  | ' + board[8] + ' | ' + board[9])
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

# %%
test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# %%
def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Choose X or O')

    if marker == 'X':
        return ('X', 'O')
    else: 
        return ('O', 'X')


# %%
#TEST
player_input()


# %%
def place_marker(board, marker, position):
    board[position] = marker
    

# %%
place_marker(test_board,'$',8)
display_board(test_board)


# %%
def win_check(board, mark):
    return (
        (board[7] == board[8] == board[9] == mark) or
        (board[4] == board[5] == board[6] == mark) or
        (board[1] == board[2] == board[3] == mark) or
        (board[7] == board[4] == board[1] == mark) or
        (board[8] == board[5] == board[2] == mark) or
        (board[9] == board[6] == board[3] == mark) or
        (board[7] == board[5] == board[3] == mark) or
        (board[1] == board[5] == board[9] == mark)      
    )
    

# %%
#TEST
win_check(test_board,'X')


# %%
import random
def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# %%
#Checks whether space on board is open, returns T/F
def space_check(board, position):
    return board[position] == ''
    


# %%
def full_board_check(board):
    for i in range(1,10): #includes 1 but not 10 (reminder)
        if space_check(board, i):
            return False

    return True


# %%
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose position (1-9)'))


# %%
def replay():
    return input('Play again? Enter y or n')


# %%
print('Tic Tac Toe is Starting!')

while True:
#initialize board
    the_board = ['']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + 'goes first')

    #Prompt user to begin game
    play_game = input('Ready to play? Enter y or n')
    if play_game.lower() == 'y':
        game_on = True
    else:
        game_on = False

    #Conditions for player turns
    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

        #check for win
        if win_check(the_board, player1_marker):
            display_board(the_board)
            print('Game over, Player 1 wins')
            game_on = False
        elif full_board_check(the_board):
            display_board(the_board)
            print('Tie Game!')
            break
        else:
            turn = 'Player 2'

        #Player 2 turn
        if turn == 'Player 2':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

        #check for win
        if win_check(the_board, player2_marker):
            display_board(the_board)
            print('Game over, Player 2 wins')
            game_on = False
        elif full_board_check(the_board):
            display_board(the_board)
            print('Tie Game!')
            break
        else:
            turn = 'Player 1'

    if not replay():
        break

