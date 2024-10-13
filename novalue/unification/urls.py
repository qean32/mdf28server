from django.urls import path, include
from rest_framework.routers import DefaultRouter

from unification.views import game
from unification.views import team
from unification.views import player
router = DefaultRouter()

# ################################# ###################### ################################

router.register(r'search/match',game.match_search_view)
# router.register('update/match_org',game.match_update_view_for_org)

# router.register(r'search/meeting', game.meeting_search_view)
router.register(r'update/meeting_org',game.meeting_update_view_for_org)

router.register(r'search/tournament',game.tournament_search_view)
# router.register(r'search_short/tournament',game.tournament_search_short_view)
# router.register(r'update/tournament_org',game.tournament_update_view_for_org)

router.register(r'update/team',team.team_update_view)
# router.register(r'update_org/team',team.team_update_view_for_org)
# router.register(r'search/team', team.team_search_view)

# router.register(r'search/player/dota', player.player_search_view_DOTA)
# router.register(r'update/player_org/dota',player.player_update_view_for_org_DOTA)
# router.register(r'update/player_user/dota',player.player_update_view_for_user_DOTA)
# router.register(r'update/player_director/dota',player.player_update_view_for_director_DOTA)

router.register(r'search/player/cs', player.player_search_view_CS)
# router.register(r'update/player_org/cs',player.player_update_view_for_org_CS)
# router.register(r'update/player_user/cs',player.player_update_view_for_user_CS)
# router.register(r'update/player_director/cs',player.player_update_view_for_director_CS)

router.register(r'search/player/bascketball', player.player_search_view_BASCKETBALL)
# router.register(r'update/player_org/bascketball',player.player_update_view_for_org_BASCKETBALL)
# router.register(r'update/player_user/bascketball',player.player_update_view_for_user_BASCKETBALL)
# router.register(r'update/player_director/bascketball',player.player_update_view_for_director_BASCKETBALL)

# router.register(r'delete/offers',team.offers_delete_view_for_director)
# router.register(r'search/offers', team.offers_search_view)
# router.register(r'search/offers_short', team.offers_search_view_short)

# router.register(r'update/application/tournament',game.application_tournament_update_view)
router.register(r'search/application/tournament',game.application_tournament_search_view)

# router.register(r'update/application/meeting',game.application_meeting_update_view)
router.register(r'search/application/meeting',game.application_meeting_search_view)

urlpatterns = [
    # path('unification/reg/player/dota/', player.player_reg_view_DOTA.as_view({'post': 'create'}), name='cwasdas'),
    # path('unification/reg/player/cs/', player.player_reg_view_CS.as_view({'post': 'create'}), name='cwasdas'),
    # path('unification/reg/player/bascketball/', player.player_reg_view_BASCKETBALL.as_view({'post': 'create'}), name='cwasdas'),
    # path('unification/reg/application/meeting/', game.application_meeting_reg_view.as_view({'post': 'create'}), name='cwasdas'),
    # path('unification/reg/application/tournament/', game.application_tournament_reg_view.as_view({'post': 'create'}), name='cwasdas'),


    path('unification/reg/meeting/', game.meeting_reg_view.as_view({'post': 'create'}), name='cwasdas'),
    path('unification/search/meeting/', game.meeting_search_view.as_view({'get': 'list'}), name='cwasdas'),
    path('unification/search/meeting/short/', game.meeting_search_view.as_view({'get': 'list'}), name='cwasdas'),

    path('unification/reg/match/', game.match_reg_view.as_view({'post': 'create'}), name='cwasdas'),
    path('unification/search/match/', game.match_search_view.as_view({'get': 'list'}), name='cwasdas'),

    path('unification/reg/offers/', team.offers_reg_view.as_view({'post': 'create'}), name='cwasdas'),
    path('unification/search/offers/', team.offers_search_view.as_view({'get': 'list'}), name='cwasdas'),

    path('unification/reg/team/', team.team_reg_view.as_view({'post': 'create'}), name='cwasdas'),
    path('unification/search/team/', team.team_search_view.as_view({'get': 'list'}), name='cwasdas'),
    path('unification/search/team/short/', team.team_search_view.as_view({'get': 'list'}), name='cwasdas'),

    path('unification/reg/tournament/', game.tournament_reg_view.as_view({'post': 'create'}), name='cwasdas'),
    path('unification/search/tournament/', game.tournament_search_view.as_view({'get': 'list'}), name='cwasdas'),
    path('unification/search/tournament/short/', game.tournament_search_short_view.as_view({'get': 'list'}), name='cwasdas'),
]

urlpatterns += path('unification/', include(router.urls)),