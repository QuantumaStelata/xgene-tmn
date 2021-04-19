from django.shortcuts import render, HttpResponseRedirect, Http404
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password
from apps.main.models import ClanInfo
from apps.players.models import Players
from apps.main.views import MainView
from apps.interview.models import Question
import requests, json
# Create your views here.

class WgOpenIdView(View):
    def get(self, request, *args, **kwargs):
        # return HttpResponseRedirect('https://api.worldoftanks.ru/wot/auth/login/?application_id=f43f7018199159cf600980288310be15&redirect_uri=http%3A%2F%2F127.0.0.1:8000%2Fuser%2Flogin')
        return HttpResponseRedirect('https://api.worldoftanks.ru/wot/auth/login/?application_id=f43f7018199159cf600980288310be15&redirect_uri=https%3A%2F%2Fxgenex.herokuapp.com%2Fuser%2Flogin')

class LoginView(View):
    def get(self, request, *args, **kwargs):
        url = f"https://api.worldoftanks.ru/wot/account/info/?application_id=f43f7018199159cf600980288310be15&account_id={request.GET.get('account_id')}&access_token={request.GET.get('access_token')}"
        check_user = json.loads(requests.get(url).text)
        
        try:
            if check_user['status'] == 'ok':
                player = Players.objects.get(player_id=request.GET.get('account_id'))
            else:
                return HttpResponseRedirect('/')
        except:
            return HttpResponseRedirect('/')

        user, created = User.objects.get_or_create(username=request.GET.get('nickname'))

        if created:
            user.is_superuser=False
            user.is_staff=False
            user.is_active=True

        user.profile.play = player
        user.profile.token = request.GET.get('access_token')
        user.password = make_password(request.GET.get('nickname'))
        user.save()


        user = auth.authenticate(username=request.GET.get('nickname'), password=request.GET.get('nickname'))
        auth.login(request, user)
        return HttpResponseRedirect('/')

class UserView(View):
    def get(self, request, username, *args, **kwargs):
        clan = ClanInfo.objects.get()
        question = Question.objects.filter(users=request.user.profile.play)
        try:
            user = User.objects.get(username=username)
        except:
            raise Http404

        return render(request, 'users/user.html', {'online': MainView.online(), 'clan': clan, 'user_': user, 'question': question})

class EditUser(View):
    def get(self, request, username, *args, **kwargs):
        clan = ClanInfo.objects.get()
        user_ = User.objects.get(username=username)

        if request.user.username == user_.username:
            return render(request, 'users/user.html', {'online': MainView.online(), 'clan': clan, 'user_': user_, 'edit': True})
        else:
            return HttpResponseRedirect('/')
    
    def post(self, request, username, *args, **kwargs):
        clan = ClanInfo.objects.get()
        user = User.objects.get(username=username)
        if 'photo' in request.POST:
            user.profile.photo = request.POST['photo']
        if 'text' in request.POST:
            user.profile.url = request.POST['text']
        user.save()

        return HttpResponseRedirect(f'/user/{user}')

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect('/')