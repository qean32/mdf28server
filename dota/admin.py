from django.contrib import admin
from dota.models import game
from dota.models import team

# Register your models here.

@admin.register(game.record_stat)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'match',)

@admin.register(game.match_DOTA)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','team_one','team_two',)

@admin.register(game.meeting_DOTA)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','team_one','team_two',)

@admin.register(game.tournament_DOTA)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

@admin.register(team.team_DOTA)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'team_name',)

@admin.register(team.player_DOTA)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(team.cup_DOTA)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(team.solo_cup_DOTA)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(team.offers_DOTA)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'team',)
#
@admin.register(team.rank_DOTA)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'rank_name',)

@admin.register(team.position_DOTA)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'position_name',)

@admin.register(game.application_DOTA_tournament)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(game.application_DOTA_meeting)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(game.hero)
class UserAdmin(admin.ModelAdmin):
    list_display = ('hero_name',)