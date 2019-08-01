from django.test import TestCase
# django.test.client

from problem_solver.chessboard import KnightFigure, make_board

counter, board = make_board(0, 0)


class CheckMoveTest(TestCase):
    def test_one_to_four(self):
        for i in range(1, 4):
            for j in range(1, 4):
                self.assertEqual(
                    check_move(i, j, board), True
                )

    def test_zero_zero(self):
        self.assertEqual(
            check_move(0, 0, board), False
        )

    def test_five_to_hundred(self):
        for i in range(5, 100):
            for j in range(5, 100):
                self.assertEqual(
                    check_move(i, j, board), False
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
                    make_board(i, j), (1, test_board)
                )
                test_board[i][j] = 0

    def test_five_to_hundred(self):
        for i in range(5, 101):
            for j in range(5, 101):
                self.assertRaises(
                    make_board(i, j), ValueError
                )