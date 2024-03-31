from django.urls import path, include
from rest_framework.routers import DefaultRouter

from poker.views import game
from poker.views import player
router = DefaultRouter()

# ################################# ###################### ################################

router.register(r'reg_match',game.match_reg_view)
router.register(r'search_match',game.match_search_view,'match-search')
router.register(r'update_match_org',game.match_update_view_for_org,'match-update_org')
router.register(r'update_match_player',game.match_update_view_for_player,'match-update_player')

router.register(r'reg_tournament',game.tournament_reg_view)
router.register(r'search_tournament',game.tournament_search_view,'tournament-search')
router.register(r'update_tournament_org',game.tournament_update_view_for_org,'tournament-update_org')
router.register(r'update_tournament_player',game.tournament_update_view_for_player,'tournament-update_player')

router.register(r'reg_player',player.player_reg_view)
router.register(r'search_player', player.player_search_view,'team-search_player')
router.register(r'update_player_org',player.player_update_view_for_org,'team-update_player_org')
router.register(r'update_player_user',player.player_update_view_for_user,'team-update_player_user')

router.register(r'application_no_team_reg_tournament',game.application_no_team_tournament_reg_view)
router.register(r'application_no_team_update_tournament_org',game.application_no_team_tournament_update_view_for_org,'application_no_team_tournament-update_org')
router.register(r'application_no_team_update_tournament',game.application_no_team_tournament_update_view,'application_no_team_tournament-up')


urlpatterns = []

urlpatterns += path('poker/', include(router.urls)),