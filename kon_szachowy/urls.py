from django.conf.urls import url

from app.views import LandingPageView

urlpatterns = [
    url(r'', LandingPageView.as_view(), name='landing_pange'),
]
