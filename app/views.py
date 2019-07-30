from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from app.models import Knight


class LandingPageView(View):
    def get(self, request):
        chess_range = tuple('12345')
        return render(request, 'app/main.html', context={'range': chess_range})

    def post(self, request):
        place = tuple(request.POST.get('place'))
        Knight.objects.create(position_x=int(place[0])-1, position_y=int(place[1])-1)
        return redirect(reverse_lazy('table_result'))


class TableResultView(View):
    def get(self, request):
        knight = Knight.objects.last()
        start_x = knight.position_x
        start_y = knight.position_y
        board = []
        for i in range(0, 5):
            board.append(5 * [0])
        board[start_x][start_y] = 1
        print(board)
        return render(request, 'app/table.html', context={'board': board})
