from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bascketball.views import game
from bascketball.views import team
router = DefaultRouter()

# ################################# ###################### ################################

router.register(r'search/match',game.match_search_view)
router.register(r'update/match_org',game.match_update_view_for_org)
router.register(r'update/match_director',game.match_update_view_for_director)

router.register(r'search/meeting',game.meeting_search_view)
router.register(r'update/meeting_org',game.meeting_update_view_for_org)
router.register(r'update/meeting_director',game.meeting_update_view_for_director)

router.register(r'search/tournament',game.tournament_search_view)
router.register(r'search_short/tournament',game.tournament_search_short_view)
router.register(r'update/tournament_org',game.tournament_update_view_for_org)

router.register(r'update/team',team.team_update_view)
router.register(r'update_org/team',team.team_update_view_for_org)
router.register(r'search/team', team.team_search_view)

router.register(r'search/player', team.player_search_view)
router.register(r'update/player_org',team.player_update_view_for_org)
router.register(r'update/player_user',team.player_update_view_for_user)
router.register(r'update/player_director',team.player_update_view_for_director)

router.register(r'delete/offers',team.offers_delete_view_for_director)
router.register(r'search/offers', team.offers_search_view)

router.register(r'update/application_tournament_org',game.application_tournament_update_view_for_org)
router.register(r'update/application_tournament',game.application_tournament_update_view)
router.register(r'search/application_tournament',game.application_tournament_search_view)

router.register(r'search/application_meeting',game.application_meeting_search_view)
router.register(r'update/application_meeting',game.application_meeting_update_view)
router.register(r'update/application_meeting_org',game.application_meeting_update_view_for_org)

router.register(r'search/record_stat',game.record_stat_search_view)

urlpatterns = [
    path('bascketball/reg/application_meeting/', game.application_meeting_reg_view.as_view({
        'post': 'create'
    }), name='cwasdas'),
    path('bascketball/reg/meeting/', game.meeting_reg_view.as_view({
        'post': 'create'
    }), name='cwasdas'),
    path('bascketball/reg/application_tournament/', game.application_tournament_reg_view.as_view({
        'post': 'create'
    }), name='cwasdas'),
    path('bascketball/reg/offers/', team.offers_reg_view.as_view({
        'post': 'create'
    }), name='cwasdas'),
    path('bascketball/reg/player/', team.player_reg_view.as_view({
        'post': 'create'
    }), name='cwasdas'),
    path('bascketball/reg/team/', team.team_reg_view.as_view({
        'post': 'create'
    }), name='cwasdas'),
    path('bascketball/reg/match/', game.match_reg_view.as_view({
        'post': 'create'
    }), name='cwasdas'),
    path('bascketball/reg/tournament/', game.tournament_reg_view.as_view({
        'post': 'create'
    }), name='cwasdas'),
    path('bascketball/reg/record_stat/', game.record_stat_reg_view.as_view({
        'post': 'create'
    }), name='cwasdas'),
]

urlpatterns += path('bascketball/', include(router.urls)),