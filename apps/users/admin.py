from django.contrib import admin
from .models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    #list_filter = ('role', 'team')
    #search_fields = ('name', 'role__role_ru', 'team__name')
    #fields = (('role', 'team'), 'name', 'player_id', 'battles', 'win', 'wgr', 'damage', 'frags')
