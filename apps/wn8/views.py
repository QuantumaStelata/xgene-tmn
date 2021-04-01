from django.shortcuts import render
from django.views.generic import View
from apps.main.views import MainView
from apps.main.models import ClanInfo
from apps.players.models import Players
from bs4 import BeautifulSoup
import requests
# Create your views here.

class Wn8View(View):
    def get(self, request, *args, **kwargs):
        clan = ClanInfo.objects.get()
        return render(request, 'wn8/wn8.html', {'online': MainView.online(), 'clan': clan, 'get': True})

    def post(self, request, *args, **kwargs):
        clan = ClanInfo.objects.get()
        try:
            player = Players.objects.get(name__iexact = request.POST['name'])
        except:
            return render(request, 'wn8/wn8.html', {'online': MainView.online(), 'clan': clan, 'post': False, 'error': 404})

        try:
            xvm = requests.get(f'https://stats.modxvm.com/ru/stats/players/{player.player_id}').text
            soup = BeautifulSoup(xvm, "html.parser")

            battles = soup.find_all("div", {"class": "h2"})[0].text
            win = soup.find_all("div", {"class": "h2"})[1].text
            wn8 = soup.find_all("div", {"class": "h2"})[2].text
            wgr = soup.find_all("div", {"class": "h2"})[3].text
            eff = soup.find_all("div", {"class": "h2"})[5].text
            frags = soup.find_all("div", {"class": "h2"})[12].text
            damage = soup.find_all("div", {"class": "h2"})[13].text
            exp = soup.find_all("div", {"class": "h2"})[14].text
            survive = soup.find_all("div", {"class": "h2"})[18].text
            max_frags = soup.find_all("div", {"class": "h2"})[15].text
            max_damage = soup.find_all("div", {"class": "h2"})[16].text
            max_exp = soup.find_all("div", {"class": "h2"})[17].text

            statistic = {'battles': battles, 'win': win, 'wn8': wn8, 'wgr': wgr, 'eff': eff,
                         'frags': frags, 'damage': damage, 'exp': exp, 'survive': survive,
                         'max_frags': max_frags, 'max_damage': max_damage, 'max_exp': max_exp}
        except:
            return render(request, 'wn8/wn8.html', {'online': MainView.online(), 'clan': clan, 'post': False, 'error': 400})


        return render(request, 'wn8/wn8.html', {'online': MainView.online(), 'clan': clan,
                                                'post': True, 'player': player, 'statistic': statistic})