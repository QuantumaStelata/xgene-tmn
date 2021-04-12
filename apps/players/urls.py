from django.urls import path
from django.conf.urls import url
from .views import PlayersView, TeamView

urlpatterns = [
     url(r'(\S+)', TeamView.as_view(), name='team'),
     path('', PlayersView.as_view(), name='players')
]
