board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

players = [1, 2]
turn = 1
score = {1: 0, 2: 0}


def clear_board():
    print('Clearing board')
    # get amount of rows and columns
    rows = len(board)
    col = len(board[0])
    # loop rows and columns, setting each to 0
    for i in range(rows):
        for j in range(col):
            board[i][j] = 0


def check_diagonal(player):
    # check if any diagonal rows match
    if board[0][0] == player & board[1][1] == player & board[2][2] == player or board[0][2] == player & board[1][1]\
            == player & board[2][0] == player:
        return True


def check_vertical(player):
    # check if any vertical rows match
    if board[0][0] == player & board[0][1] == player & board[0][2] == player or board[1][0] == player & board[1][1]\
            == player & board[1][2] == player or board[2][0] == player & board[2][1] == player & board[2][2] == player:
        return True


def check_horizontal(player):
    # check if any horizontal rows match
    if board[0][0] == player & board[2][0] == player & board[2][0] == player or board[0][1] == player & board[1][1]\
            == player & board[2][1] == player or board[0][2] == player & board[1][2] == player & board[2][2] == player:
        return True


def check_win(players):
    win = False
    # loop players and run check for each win possibility
    for player in players:

        if check_diagonal(player):
            print('Player {} wins!'.format(player))
            win = True
            score[player] = score[player] + 1

        if check_vertical(player):
            print('Player {} wins!'.format(player))
            win = True
            score[player] = score[player] + 1

        if check_horizontal(player):
            print('Player {} wins!'.format(player))
            win = True
            score[player] = score[player] + 1

    return win


def make_move(player):
    # print who gets to make a move
    print('Player {}\'s turn to move'.format(player))
    # print the board
    print_board()
    free = True
    while free:
        # take input and place in board
        # validate input to be between 0 and 2
        while True:
            row = int(input('Input row to put mark (0-2)\n'))
            if row < 0 or row > 2:
                print('Please enter a value between 0 and 2')
            else:
                break
        while True:
            column = int(input('Input column to put mark (0-2)\n'))
            if column < 0 or column > 2:
                print('Please enter a value between 0 and 2')
            else:
                break

        # check if spot is unclaimed
        if board[row][column] == 0:
            # add player to spot
            board[row][column] = player
            free = False
        else:
            print('Spot already claimed, please try another one.')


def print_board():
    # print board with line breaks
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in board]))
turn = int(input('Which player should begin?'))
while True:
    # make a move
    make_move(turn)

    # check if anyone won
    if check_win(players):
        print('Score is {}'.format(score))
        clear_board()
        turn = int(input('Which player should begin?'))
        #exit()

# change turn to other players turn
    if turn == 1:
        turn = 2
    else:
        turn = 1
