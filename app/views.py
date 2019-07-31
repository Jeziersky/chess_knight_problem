from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from app.function import move, make_board
from app.models import Knight


class LandingPageView(View):
    def get(self, request):
        """ Drukuje strone glowna aplikacji """
        board_range = range(0, 4)
        return render(request, 'app/main.html', context={'range': board_range})

    def post(self, request):
        """ Zapis do bazy danych """
        place = tuple(request.POST.get('place'))
        knight = Knight.objects.create(position_x=int(place[0]), position_y=int(place[1]))
        start_x = knight.position_x
        start_y = knight.position_y
        counter, board = make_board(start_x, start_y)
        move(start_x, start_y, counter, board)
        return render(request, 'app/table.html', context={'board': board})