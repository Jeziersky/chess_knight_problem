from django.conf.urls import url

from problem_solver.views import LandingPageView

urlpatterns = [
    url(r'^$', LandingPageView.as_view(), name='landing_pange'),
]
