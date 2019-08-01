from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from problem_solver.views import LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', LandingPageView.as_view(), name='landing_pange'),
]
