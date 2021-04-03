from django.shortcuts import render, HttpResponseRedirect, Http404
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from apps.main.models import ClanInfo
from apps.main.views import MainView
# Create your views here.

class WgOpenIdView(View):
    def get(self, request, *args, **kwargs):
        # return HttpResponseRedirect('https://api.worldoftanks.ru/wot/auth/login/?application_id=f43f7018199159cf600980288310be15&redirect_uri=http%3A%2F%2F127.0.0.1:8000%2Fuser%2Flogin')
        return HttpResponseRedirect('https://api.worldoftanks.ru/wot/auth/login/?application_id=f43f7018199159cf600980288310be15&redirect_uri=https%3A%2F%2Fxgenex-test.herokuapp.com%2Fuser%2Flogin')

class LoginView(View):
    def get(self, request, *args, **kwargs):
        user, created = User.objects.get_or_create(username=request.GET.get('nickname'))

        if created:
            user.is_superuser=False
            user.is_staff=False
            user.is_active=True
            user.password = make_password(request.GET.get('nickname'))
            user.save()


        user = auth.authenticate(username=request.GET.get('nickname'), password=request.GET.get('nickname'))
        auth.login(request, user)
        return HttpResponseRedirect('/')

class UserView(View):
    def get(self, request, username, *args, **kwargs):
        clan = ClanInfo.objects.get()
        try:
            user = User.objects.get(username=username)
        except:
            raise Http404

        return render(request, 'users/user.html', {'online': MainView.online(), 'clan': clan, 'user_': user})

class EditUser(View):
    def get(self, request, username, *args, **kwargs):
        clan = ClanInfo.objects.get()
        user = User.objects.get(username=username)

        return render(request, 'users/user.html', {'online': MainView.online(), 'clan': clan, 'user': user, 'edit': True})
    
    def post(self, request, username, *args, **kwargs):
        clan = ClanInfo.objects.get()
        user = User.objects.get(username=username)
        if 'image' in request.FILES:
            user.profile.image = request.FILES['image']
        if 'text' in request.POST:
            user.profile.url = request.POST['text']
        user.save()

        return HttpResponseRedirect(f'/user/{user}')