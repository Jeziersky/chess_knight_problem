from django.test import TestCase
# django.test.client

from problem_solver.chessboard import KnightFigure, make_board

board = make_board(0, 0)
knight_figure = KnightFigure(board)


class CheckMoveTest(TestCase):
    def test_one_to_four(self):
        for i in range(1, 4):
            for j in range(1, 4):
                self.assertEqual(
                    knight_figure.check_move(i, j), True
                )

    def test_zero_zero(self):
        self.assertEqual(
            knight_figure.check_move(0, 0), False
        )

    def test_five_to_hundred(self):
        for i in range(5, 100):
            for j in range(5, 100):
                self.assertEqual(
                    knight_figure.check_move(i, j), False
                )


class MakeBoardTest(TestCase):
    def test_zero_to_four(self):
        test_board = []
        for i in range(0, 5):
            test_board.append(5 * [0])
        for i in range(0, 5):
            for j in range(0, 5):
                test_board[i][j] = 1
                self.assertEqual(
                    make_board(i, j), test_board
                )
                test_board[i][j] = 0


class MoveTest(TestCase):
    def test_move_zero_to_four(self):
        for i in range(0, 5):
            for j in range(0, 5):
                self.assertEqual(
                    knight_figure.move(i, j), True
                )

    def test_move_ten_to_hundred(self):
        for i in range(10, 101):
            for j in range(10, 101):
                self.assertEqual(
                    knight_figure.move(i, j), False
                )
