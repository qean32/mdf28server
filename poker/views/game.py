from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import BasePermission, SAFE_METHODS, \
    IsAuthenticated, AllowAny

from api import permissions
from poker.models import game
from poker.serializers import game as game_s

# ############################ - не трогать - ##########################################

class match_update_view_for_org(viewsets.ModelViewSet):
    queryset = game.match_POKER.objects.all()
    permission_classes = [permissions.IsOrg]
    serializer_class = game_s.match_update_serializer

class match_update_view_for_player(viewsets.ModelViewSet):
    queryset = game.match_POKER.objects.all()
    permission_classes = [permissions.IsOrg]
    serializer_class = game_s.match_update_serializer_player

class match_search_view(permissions.ListViewSet):
    queryset = game.match_POKER.objects.exclude()
    permission_classes = [AllowAny]
    filter_backend = (DjangoFilterBackend,)
    serializer_class = game_s.match_search_serializer
    filter_backends = (
       SearchFilter,
    )
    search_fields = (
        '__all__',
    )

class match_reg_view(viewsets.ModelViewSet):
    queryset = game.match_POKER.objects.all()
    permission_classes = [permissions.IsOrg]
    serializer_class = game_s.match_reg_serializer
    http_method_names = ['post', 'get',]


# ############################ - не трогать - ##########################################


class tournament_update_view_for_org(viewsets.ModelViewSet):
    queryset = game.tournament_POKER.objects.all()
    permission_classes = [permissions.IsOrg]
    serializer_class = game_s.tournament_update_serializer

class tournament_update_view_for_player(viewsets.ModelViewSet):
    queryset = game.tournament_POKER.objects.all()
    permission_classes = [permissions.IsOrg]
    serializer_class = game_s.tournament_update_serializer_for_player


class tournament_search_view(permissions.ListViewSet):
    queryset = game.tournament_POKER.objects.exclude()
    permission_classes = [AllowAny]
    filter_backend = (DjangoFilterBackend,)
    serializer_class = game_s.tournament_search_serializer
    filter_backends = (
        SearchFilter,
    )
    search_fields = (
        '__all__',
    )


class tournament_reg_view(viewsets.ModelViewSet):
    queryset = game.tournament_POKER.objects.all()
    permission_classes = [permissions.IsOrg]
    serializer_class = game_s.tournament_reg_serializer
    http_method_names = ['post', 'get',]


# ############################ - не трогать - ##########################################

class application_no_team_tournament_reg_view(viewsets.ModelViewSet):
    queryset = game.application_POKER_tournament_no_team.objects.all()
    permission_classes = [permissions.IsOrg]
    serializer_class = game_s.application_tournament_no_team_reg_serializer
    http_method_names = ['post', 'get',]


class application_no_team_tournament_update_view(viewsets.ModelViewSet):
    queryset = game.application_POKER_tournament_no_team.objects.all()
    permission_classes = [permissions.IsOrg]
    serializer_class = game_s.application_tournament_no_team_update_serializer

class application_no_team_tournament_update_view_for_org(viewsets.ModelViewSet):
    queryset = game.application_POKER_tournament_no_team.objects.all()
    permission_classes = [permissions.IsOrg]
    serializer_class = game_s.application_tournament_no_team_update_serializer_for_org

class tournament_no_team_update_view_for_player(viewsets.ModelViewSet):
    queryset = game.tournament_POKER.objects.all()
    permission_classes = [permissions.IsOrg]
    serializer_class = game_s.tournament_no_team_update_serializer_for_player

