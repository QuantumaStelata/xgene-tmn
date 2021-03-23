from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'(\w+)', Wn8View.as_view(), name='wn8-search'),
    path(r'', Wn8View.as_view(), name='wn8'),
]
