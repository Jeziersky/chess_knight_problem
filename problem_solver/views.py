from django.shortcuts import render
from django.views import View

from problem_solver.chessboard import SIZE_OF_BOARD
from problem_solver.service import KnightFigureService


class LandingPageView(View):
    def get(self, request):
        """ Main page of app """
        board_range = range(SIZE_OF_BOARD.max+1)
        return render(request, 'app/main.html', context={'range': board_range})

    def post(self, request):
        """ POST request handler """
        place = tuple(request.POST.get('place'))
        knight_figure_service = KnightFigureService(place)
        board = knight_figure_service.execute()
        return render(request, 'app/table.html', context={'board': board})
