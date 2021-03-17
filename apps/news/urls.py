from django.urls import path
from django.conf.urls import url
from .views import News, Articles

urlpatterns = [
    url(r'(\d+)', Articles.as_view(), name='article'),
    path('', News.as_view(), name='news'),
]
