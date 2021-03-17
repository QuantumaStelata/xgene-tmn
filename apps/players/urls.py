from django.urls import path
from .views import PlayersView

urlpatterns = [
     path('', PlayersView.as_view(), name='players')
]
