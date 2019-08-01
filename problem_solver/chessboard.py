from collections import namedtuple

BoardTpl = namedtuple('BoardTpl', 'min max')
SIZE_OF_BOARD = BoardTpl(0, 4)


class ChessFigure:
    """ Generic chess figure """
    __figure_moves = ()
    name = None
    board = None

    def __init__(self, name, figure_moves, board):
        self.name = name
        self.__figure_moves = figure_moves
        self.board = board

    @property
    def figure_moves(self):
        return self.__figure_moves

    def move(self, x, y):
        raise NotImplementedError

    def check_move(self, x, y):
        raise NotImplementedError


class KnightFigure(ChessFigure):
    """ Class representing knight figure """

    def __init__(self, board):
        figure_moves = ((-2, 1), (-1, 2), (1, 2), (2, 1),
                        (2, -1), (1, -2), (-1, -2), (-2, -1))
        self.counter = 1
        super().__init__("Knight", figure_moves, board)

    def move(self, x, y):
        """ Make all possible moves for knight"""
        if self.counter == (SIZE_OF_BOARD.max + 1) * (SIZE_OF_BOARD.max + 1):
            return True
        for jump in self.figure_moves:
            after_x, after_y = x + jump[0], y + jump[1]
            if self.check_move(after_x, after_y):  # Move knight if true
                self.counter += 1
                self.board[after_x][after_y] = self.counter
                if not self.move(after_x, after_y):
                    self.board[after_x][after_y] = 0
                    self.counter -= 1
                else:
                    return True
        return False

    def check_move(self, x, y):
        """ Check move correctness """
        return SIZE_OF_BOARD.min <= x <= SIZE_OF_BOARD.max and SIZE_OF_BOARD.min <= y <= SIZE_OF_BOARD.max and \
               self.board[x][y] == 0


def make_board(start_x=0, start_y=0):
    """ Create game board """
    if SIZE_OF_BOARD.min <= start_x <= SIZE_OF_BOARD.max and SIZE_OF_BOARD.min <= start_y <= SIZE_OF_BOARD.max:
        board = [5 * [0] for i in range(SIZE_OF_BOARD.min, SIZE_OF_BOARD.max + 1)]
        board[start_x][start_y] = 1
        return board
    else:
        raise ValueError
