from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from app.models import Knight


class LandingPageView(View):
    def get(self, request):
        """ Drukuje strone glowna aplikacji """
        chess_range = tuple('12345')
        return render(request, 'app/main.html', context={'range': chess_range})

    def post(self, request):
        """ Zapis do bazy danych """
        place = tuple(request.POST.get('place'))
        knight = Knight.objects.create(position_x=int(place[0]) - 1, position_y=int(place[1]) - 1)
        start_x = knight.position_x
        start_y = knight.position_y
        board = []
        for i in range(0, 5):
            board.append(5 * [0])
        board[start_x][start_y] = 1
        counter = 1

        def check_move(x, y):
            """ Sprawdza czy ruch miesci sie w szachownicy """
            if 0 <= x < 5 and 0 <= y < 5 and board[x][y] == 0:
                return True
            return False

        def move(x, y, counter):
            """ Wykonuje wszystkie mozliwe ruchy naszym pioniem z pozycji startowej"""
            jumps = ((-2, 1), (-1, 2), (1, 2), (2, 1),
                     (2, -1), (1, -2), (-1, -2), (-2, -1))  # możliwe ruchy skoczka
            for jump in jumps:
                after_x = x + jump[0]
                after_y = y + jump[1]
                if check_move(after_x, after_y):  # jesli jest mozliwe skacze dalej
                    counter += 1
                    board[after_x][after_y] = counter
                    move(after_x, after_y, counter)

        move(start_x, start_y, counter)
        return render(request, 'app/table.html', context={'board': board})