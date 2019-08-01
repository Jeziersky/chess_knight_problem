def make_board(start_x=0, start_y=0):
    if 0 <= start_x <= 4 and 0 <= start_y <= 4:
        board = []
        for i in range(0, 5):
            board.append(5 * [0])
        board[start_x][start_y] = 1
        counter = 1
        return counter, board
    else:
        return ValueError

def check_move(x, y, board):
    """ Sprawdza czy ruch miesci sie w szachownicy """
    return 0 <= x <= 4 and 0 <= y <= 4 and board[x][y] == 0


def move(x, y, counter, board):
    """ Wykonuje wszystkie mozliwe ruchy naszym pioniem z pozycji startowej"""
    print(counter)
    if counter == 25:
        return board
    jumps = ((-2, 1), (-1, 2), (1, 2), (2, 1),
             (2, -1), (1, -2), (-1, -2), (-2, -1))  # możliwe ruchy skoczka
    for jump in jumps:
        after_x = x + jump[0]
        after_y = y + jump[1]
        if check_move(after_x, after_y, board):  # jesli jest mozliwe skacze dalej
            counter += 1
            board[after_x][after_y] = counter
            move(after_x, after_y, counter, board)
            print("||" + str(counter) + "||")