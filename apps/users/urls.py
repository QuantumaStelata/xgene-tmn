from django.urls import path
from django.conf.urls import url
from .views import WgOpenIdView, LoginView, UserView, EditUser, LogoutView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('', WgOpenIdView.as_view(), name='wgopenid'),
    url(r'(\w+)/edit/', EditUser.as_view(), name='edit'),
    url(r'(\w+)/logout', LogoutView.as_view(), name='logout'),
    url(r'(\w+)', UserView.as_view(), name='user'),
]