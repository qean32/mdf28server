from django.contrib import admin
from bascketball.models import game
from bascketball.models import team

# Register your models here.

@admin.register(game.match_BASCKETBALL)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','team_one','team_two',)

@admin.register(game.meeting_BASCKETBALL)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','team_one','team_two',)

@admin.register(game.tournament_BASCKETBALL)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

@admin.register(team.team_BASCKETBALL)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'team_name',)

@admin.register(team.player_BASCKETBALL)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(team.cup_BASCKETBALL)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(team.solo_cup_BASCKETBALL)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(team.offers_BASCKETBALL)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'team',)

@admin.register(team.position_BASCKETBALL)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'position_name',)

@admin.register(game.application_BASCKETBALL_tournament)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(game.application_BASCKETBALL_meeting)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(game.record_stat)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'match',)