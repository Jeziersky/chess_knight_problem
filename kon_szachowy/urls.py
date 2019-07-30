from django.conf.urls import url

from app.views import LandingPageView, TableResultView

urlpatterns = [
    url(r'^$', LandingPageView.as_view(), name='landing_pange'),
    url(r'^result/$', TableResultView.as_view(), name='table_result'),
]
