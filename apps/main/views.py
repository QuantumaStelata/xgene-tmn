from django.shortcuts import render
from django.views.generic import View
from django.db.models import signals
from django.dispatch import receiver
from .models import ClanId, ClanInfo, ClanStatistic

import requests, json
# Create your views here.

class MainView(View):
    @staticmethod
    def online():
        url = 'https://wgstatus.com/api/data/wot'
        response = json.loads(requests.get(url).text)
        online = {}
        for i in response['results']:
            try:
                for j in i['data']['servers']:
                    if 'RU' in j['name']:
                        online[j['name']]=j['online']
            except:
                continue
        return online


    def get(self, request, *args, **kwargs):
        clan = ClanInfo.objects.get()
        static = ClanStatistic.objects.latest('static_update')

        url = 'https://ru.wargaming.net/clans/wot/{}/api/personnel/'.format(ClanId.objects.last())
        response = json.loads(requests.get(url).text)
        top_damage = response['personnel']['top_damage_avg']
        top_wins = response['personnel']['top_wins_ratio']
        top_battles = response['personnel']['top_battles_count_daily']
        return render(request, 'main/main.html', {'online': MainView.online(), 'clan': clan, 'static': static,
                                             'top_damage': top_damage, 'top_wins': top_wins, 'top_battles': top_battles})


@receiver(signals.post_save, sender=ClanId)
@receiver(signals.post_delete, sender=ClanId)
def update_clan_info(*args, **kwargs):
    '''
    Обновляет инфорамацию о клане каждый раз, когда изменился ClanId
    '''
    clan_id = ClanId.objects.last()

    url = f'https://ru.wargaming.net/clans/wot/{clan_id}/api/claninfo/'
    clan_info = json.loads(requests.get(url).text)

    if ClanInfo.objects.exists():
        clan_name = ClanInfo.objects.get().delete()
     
    try:
        clan_name = ClanInfo()
        clan_name.tag = clan_info['clanview']['clan']['tag']
        clan_name.name = clan_info['clanview']['clan']['name']
        clan_name.motto = clan_info['clanview']['clan']['motto']
        clan_name.color = clan_info['clanview']['clan']['color']
        clan_name.emblem = 'https://ru.wargaming.net' + clan_info['clanview']['clan']['huge_emblem_url']
        clan_name.save()
    except:
        ClanId.objects.last().delete()
