from django.shortcuts import render
from django.views import View

from problem_solver.chessboard import move, make_board
from problem_solver.models import Knight, Board, Field


class LandingPageView(View):
    def get(self, request):
        """ Main page of app """
        board_range = range(5)
        return render(request, 'app/main.html', context={'range': board_range})

    def post(self, request):
        """ POST request handler """
        place = tuple(request.POST.get('place'))
        knight = Knight.objects.create(position_x=int(place[0]), position_y=int(place[1]))
        start_x = knight.position_x
        start_y = knight.position_y
        counter, board = make_board(start_x, start_y)
        move(start_x, start_y, counter, board)
        obj_board = Board.objects.create()
        for i in range(5):
            for j in range(5):
                value = board[i][j]
                Field.objects.create(board=obj_board, position_x=i, position_y=j, value=value)
        return render(request, 'app/table.html', context={'board': board})