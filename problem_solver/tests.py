from django.test import TestCase
# django.test.client

from problem_solver.chessboard import KnightFigure, make_board
from problem_solver.service import KnightFigureService


class CheckMoveTest(TestCase):
    def setUp(self):
        self.board = make_board(0, 0)
        self.knight_figure = KnightFigure(self.board)

    def tearDown(self):
        del self.board, self.knight_figure

    def test_one_to_four(self):
        for i in range(1, 4):
            for j in range(1, 4):
                self.assertEqual(
                    self.knight_figure.check_move(i, j), True
                )

    def test_zero_zero(self):
        self.assertEqual(
            self.knight_figure.check_move(0, 0), False
        )

    def test_five_to_hundred(self):
        for i in range(5, 100):
            for j in range(5, 100):
                self.assertEqual(
                    self.knight_figure.check_move(i, j), False
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
    def setUp(self):
        self.board = make_board(0, 0)
        self.knight_figure = KnightFigure(self.board)

    def tearDown(self):
        del self.board, self.knight_figure

    def test_move_zero_to_four(self):
        for i in range(0, 5):
            for j in range(0, 5):
                self.assertEqual(
                    self.knight_figure.move(i, j), True
                )

    def test_move_ten_to_hundred(self):
        for i in range(10, 101):
            for j in range(10, 101):
                self.assertEqual(
                    self.knight_figure.move(i, j), False
                )


class ServiceTest(TestCase):
    def setUp(self):
        self.knight_figure_service = KnightFigureService(('1', '1'))

    def tearDown(self):
        del self.knight_figure_service

    def test_service_two_two(self):
        self.assertEqual(
            self.knight_figure_service.execute(),
            ([[25, 16, 7, 2, 19], [6, 1, 18, 15, 8], [17, 24, 11, 20, 3], [12, 5, 22, 9, 14], [23, 10, 13, 4, 21]],
             'Problem solved ;)')
        )
