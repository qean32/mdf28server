from django.urls import path, include
from rest_framework.routers import DefaultRouter

from unification.views import game
from unification.views import team
router = DefaultRouter()

# ################################# ###################### ################################

router.register(r'update/match',game.match_update_view)
router.register(r'update/meeting',game.meeting_update_view)
router.register(r'update/application/tournament',game.application_tournament_update_view)

router.register(r'update/tournament',game.tournament_update_view)
router.register(r'update/team',team.team_update_view)
router.register(r'delete/offers',team.offers_delete_view_for_director)

router.register(r'update/player', team.player_update_view)
# router.register(r'update/player/director', team.player_update_view_for_director)

urlpatterns = [
    path('unification/reg/meeting/', game.meeting_reg_view.as_view({'post': 'create'}), name='cwasdas'),
    path('unification/search/meeting/', game.meeting_search_view.as_view({'get': 'list'}), name='cwasdas'),

    path('unification/reg/player/', team.player_reg_view.as_view({'post': 'create'}), name='cwasdas'),
    path('unification/search/player/', team.player_search_view.as_view({'get': 'list'}), name='cwasdas'),

    path('unification/reg/application/tournament/', game.application_tournament_reg_view.as_view({'post': 'create'}), name='cwasdas'),
    path('unification/search/application/tournament/', game.application_tournament_search_view.as_view({'get': 'list'}), name='cwasdas'),

    path('unification/reg/match/', game.match_reg_view.as_view({'post': 'create'}), name='cwasdas'),
    path('unification/search/match/', game.match_search_view.as_view({'get': 'list'}), name='cwasdas'),

    path('unification/reg/offers/', team.offers_reg_view.as_view({'post': 'create'}), name='cwasdas'),
    path('unification/search/offers/', team.offers_search_view.as_view({'get': 'list'}), name='cwasdas'),
    path('unification/search/offers/short/', team.offers_search_view_short.as_view({'get': 'list'}), name='cwasdas'),

    path('unification/reg/team/', team.team_reg_view.as_view({'post': 'create'}), name='cwasdas'),
    path('unification/search/team/', team.team_search_view.as_view({'get': 'list'}), name='cwasdas'),
    path('unification/search/team/short/', team.team_search_view.as_view({'get': 'list'}), name='cwasdas'),

    path('unification/reg/tournament/', game.tournament_reg_view.as_view({'post': 'create'}), name='cwasdas'),
    path('unification/search/tournament/', game.tournament_search_view.as_view({'get': 'list'}), name='cwasdas'),
    path('unification/search/tournament/short/', game.tournament_search_short_view.as_view({'get': 'list'}), name='cwasdas'),
]

urlpatterns += path('unification/', include(router.urls)),