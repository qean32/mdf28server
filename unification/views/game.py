from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import BasePermission, SAFE_METHODS, \
    IsAuthenticated, AllowAny

from api import permissions
from unification.models import game
from unification.serializers import game as game_s
from django_filters import rest_framework as filters


# ------------------------------------------------------------------------------ #

class meeting_update_view(viewsets.ModelViewSet):
    queryset = game.meeting.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = game_s.meeting_update_serializer
    http_method_names = ['patch','get','put',]

class meeting_search_view(permissions.ListViewSet):
    queryset = game.meeting.objects.order_by('-created_at')
    permission_classes = []
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['id','tournament','is_qualification','direction',]
    serializer_class = game_s.meeting_search_serializer

class meeting_reg_view(viewsets.ModelViewSet):
    queryset = game.meeting.objects.all()
    permission_classes = [permissions.IsOrg]
    serializer_class = game_s.meeting_reg_serializer
    http_method_names = ['post', 'get',]

# ------------------------------------------------------------------------------ #

class match_update_view(viewsets.ModelViewSet):
    queryset = game.match.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = game_s.match_update_serializer
    http_method_names = ['patch','get','put']

class match_search_view(permissions.ListViewSet):
    queryset = game.match.objects.order_by('-created_at')
    permission_classes = []
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['meeting','direction', 'team_one', 'team_two', 'win_team',]
    serializer_class = game_s.match_search_serializer

class match_reg_view(viewsets.ModelViewSet):
    queryset = game.match.objects.all()
    permission_classes = [permissions.IsOrg]
    serializer_class = game_s.match_reg_serializer
    http_method_names = ['post', 'get',]

# ------------------------------------------------------------------------------ #


class tournament_update_view(viewsets.ModelViewSet):
    queryset = game.tournament.objects.all()
    permission_classes = [permissions.IsNoBan]
    
    serializer_class = game_s.tournament_update_serializer
    http_method_names = ['patch','get','put',]

class tournament_search_view(permissions.ListViewSet):
    queryset = game.tournament.objects.order_by('-created_at')
    permission_classes = []
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filterset_fields = ['id','direction', 'win_team',]
    serializer_class = game_s.tournament_search_serializer

class tournament_search_short_view(permissions.ListViewSet):
    queryset = game.tournament.objects.order_by('-created_at')
    permission_classes = []
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filterset_fields = ['direction',]
    serializer_class = game_s.tournament_search_short_serializer

class tournament_reg_view(viewsets.ModelViewSet):
    queryset = game.tournament.objects.all()
    permission_classes = [permissions.IsOrg]
    serializer_class = game_s.tournament_reg_serializer
    http_method_names = ['post', 'get',]

# ------------------------------------------------------------------------------ #

class application_tournament_reg_view(viewsets.ModelViewSet):
    queryset = game.application_tournament.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = game_s.application_tournament_reg_serializer
    http_method_names = ['post', 'get',]

class application_tournament_search_view(permissions.ListViewSet):
    queryset = game.application_tournament.objects.order_by('-created_at')
    permission_classes = []
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['tournament','team', 'direction']
    serializer_class = game_s.application_tournament_search_serializer

class application_tournament_update_view(viewsets.ModelViewSet):
    queryset = game.application_tournament.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = game_s.application_tournament_update_serializer
    http_method_names = ['patch','get','put']