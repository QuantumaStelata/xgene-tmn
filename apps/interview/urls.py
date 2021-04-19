from django.urls import path
from .views import Interview

urlpatterns = [
    path('', Interview.as_view(), name='interview'),
]
