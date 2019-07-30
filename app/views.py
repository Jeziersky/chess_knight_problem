from django.shortcuts import render
from django.views import View


class LandingPageView(View):
    def get(self, request):
        chess_range = tuple('12345')
        request.session['step'] = 0
        return render(request, 'app/main.html', context={'range': chess_range})


    def post(self, request):
        chess_range = tuple('12345')
        place = request.POST.get('place')
        print(place)
        step = request.session.get('step') + 1
        request.session['step'] = step
        print(request.session.get('step'))
        return render(request, 'app/main.html', context={'range': chess_range,
                                                         'step': step})
