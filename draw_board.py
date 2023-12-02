def draw_board(board) :

 board = [['__|__|__'], ['__|__|__'], ['  |  |']]
 for i in range(3):
    print(' '.join(board[i]))

draw_board('board')