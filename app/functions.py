def check_move(x, y, board):
    """ Sprawdza czy ruch miesci sie w szachownicy """

    if 0 <= x < 5 and 0 <= y < 5 and board[x][y] == 0:
        return True
    return False


def move(x, y, counter, board):
    """ Wykonuje wszystkie mozliwe ruchy naszym pioniem z pozycji startowej"""
    if counter == 24:
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
        else:
            move(x, y, counter, board)
