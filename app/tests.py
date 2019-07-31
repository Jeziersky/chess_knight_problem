from django.test import TestCase

from app.functions import check_move


class CheckMoveTest(TestCase):

    def test_zero_to_four(self):
        for i in range(0,4):
            for j in range(0,4):
                self.assertEqual(
                    check_move(i, j, board), True
                )