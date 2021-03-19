from django.shortcuts import render, Http404
from django.views.generic import View
from apps.main.models import ClanInfo, ClanStatistic, ClanId
from apps.main.views import MainView
from .models import Players, ClanRole
from django.db import transaction
from threading import Thread
import time, json, requests
# Create your views here.

class PlayersView(View):
    def get(self, request, *args, **kwargs):
        all_players = True
        clan = ClanInfo.objects.get()
        players_list = Players.objects.all()
        return render(request, "players/players.html", {'online': MainView.online(), 'all': all_players, 'clan': clan, 
                                                        'list': players_list, 'len': len(players_list)})

class TeamView(View):
    def get(self, request, team, *args, **kwargs):
        clan = ClanInfo.objects.get()
        players_list = Players.objects.filter(team__name=team)

        if players_list:
            return render(request, "players/players.html", {'online': MainView.online(), 'clan': clan, 'team': team, 
                                                        'list': players_list, 'len': len(players_list)})
        else:
            raise Http404('Такая рота не найдена')

@transaction.atomic
def update_clan_static():
    '''
    Обновляет статистику клана после обновления информации о клане,
    либо каждый N минут в другом потоке функции update
    '''
    clan_id = ClanId.objects.last()

    url = f'https://ru.wargaming.net/clans/wot/{clan_id}/api/claninfo/'
    clan_rating = json.loads(requests.get(url).text)['clanview']['rating']

    url = f'https://ru.wargaming.net/clans/wot/{clan_id}/api/stronghold'
    stronghold = json.loads(requests.get(url).text)['stronghold']

    url = f'https://ru.wargaming.net/clans/wot/{clan_id}/api/globalmap/'
    globalmap = json.loads(requests.get(url).text)['globalmap'] 

    clan_static = ClanStatistic()
    clan_info = ClanInfo.objects.get()
   
    clan_static.sh10 = stronghold['esh_10']
    clan_static.sh8 = stronghold['esh_8']
    clan_static.sh6 = stronghold['esh_6']
    clan_static.gm10 = globalmap['gm_elo_rating_10']
    clan_static.gm8 = globalmap['gm_elo_rating_8']
    clan_static.gm6 = globalmap['gm_elo_rating_6']
    clan_static.battles_count = clan_rating['average_battles_count']
    clan_static.win_rate = clan_rating['average_win_rate']
    clan_static.rate = str(clan_rating['rating'])       # May be None
    clan_static.position = str(clan_rating['rating_position'])   # May be None  
    clan_static.xp_per_battle = clan_rating['average_xp_per_battle']
    clan_static.damage_per_battle = clan_rating['average_damage_per_battle']
    clan_static.save()

@transaction.atomic
def update_clan_players():
    '''
    Обновляет список игроков клана после обновления информации о клане,
    либо каждый N минут в другом потоке функции update

    Сначала удаляет из БД лишних игроков клана.
    После обновляет игроков с API, либо добавляет их, если такого игрока не существует.
    '''
    clan_id = ClanId.objects.get()

    url = f'https://api.worldoftanks.ru/wot/clans/info/?application_id=f43f7018199159cf600980288310be15&clan_id={clan_id}'
    players_api = json.loads(requests.get(url).text)['data'][f'{clan_id}']['members']
    
    players_api_list = [i['account_name'] for i in players_api]
    players_db_list = [i.name for i in Players.objects.all()]

    if sorted(players_api_list) != sorted(players_db_list):
        for player in players_db_list:
            if player not in players_api_list:
                Players.objects.get(name=player).delete()

    
    for pl in players_api:
        player, _ = Players.objects.get_or_create(player_id=pl['account_id'], name = pl['account_name'],
                                                    clan = ClanId.objects.get(), role = ClanRole.objects.get(role_ru=str(pl['role_i18n'])))

        url = f'https://api.worldoftanks.ru/wot/account/info/?application_id=f43f7018199159cf600980288310be15&account_id={pl["account_id"]}'
        player_stats = json.loads(requests.get(url).text)['data'][f'{pl["account_id"]}']

        if str(player.battles) != str(player_stats['statistics']['all']['battles']):
            player.battles = player_stats['statistics']['all']['battles']
            player.wgr = player_stats['global_rating']
            player.win = round(int(player_stats['statistics']['all']['wins'])*100/int(player.battles if player.battles != 0 else 1), 2)
            player.damage = round(int(player_stats['statistics']['all']['damage_dealt'])/int(player.battles if player.battles != 0 else 1))
            player.frags = round(int(player_stats['statistics']['all']['frags'])/int(player.battles if player.battles != 0 else 1),2)

            player.save()


def update():
    while True:
        print ('Start Update')
        now = time.time()

        update_clan_static()
        update_clan_players()

        print (f'Update DB - {time.time()-now}s.')
        time.sleep(14400)


Thread(target=update, daemon=True, args=()).start()     

