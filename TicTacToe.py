board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

players = [1, 2]
# begin = 1
turn = 1


def check_diagonal(player):
    # check if any diagonal rows match
    if board[0][0] == player & board[1][1] == player & board[2][2] == player | board[0][2] == player & board[1][1]\
            == player & board[2][0] == player:
        return True


def check_vertical(player):
    # check if any vertical rows match
    if board[0][0] == player & board[0][1] == player & board[0][2] == player | board[1][0] == player & board[1][1]\
            == player & board[1][2] == player | board[2][0] == player & board[2][1] == player & board[2][2] == player:
        return True


def check_horizontal(player):
    # check if any horizontal rows match
    if board[0][0] == player & board[2][0] == player & board[2][0] == player | board[0][1] == player & board[1][1]\
            == player & board[2][1] == player | board[0][2] == player & board[1][2] == player & board[2][2] == player:
        return True


def check_win(players):
    # loop players and run check for each win possibility
    win = False
    for play in players:

        if check_diagonal(play):
            print('Player {} wins!'.format(play))
            win = True

        if check_vertical(play):
            print('Player {} wins!'.format(play))
            win = True

        if check_horizontal(play):
            print('Player {} wins!'.format(play))
            win = True
    return win


def make_move(player):
    # print who gets to make a move
    print('Player {} turn to move'.format(player))
    # print the board
    # print(board)
    print_board()
    # take input and place in board
    row = int(input('Input row to put mark'))
    column = int(input('Input column to put mark'))
    board[row][column] = player


def print_board():
    # print board with line breaks
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in board]))

print("Player {} gets to make the first move.".format(turn))
while True:
    # make a move
    make_move(turn)

    # check if anyone won
    if check_win(players):
        print('{} won!'.format(turn))
        exit()

# change turn to other players turn
    if turn == 1:
        turn = 2
    else:
        turn = 1
