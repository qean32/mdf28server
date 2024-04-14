from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import BasePermission, SAFE_METHODS, \
    IsAuthenticated, AllowAny

from api import permissions
from bascketball.models import game
from bascketball.serializers import game as game_s


class meeting_update_view_for_org(viewsets.ModelViewSet):
    queryset = game.meeting_BASCKETBALL.objects.all()
    permission_classes = []
    serializer_class = game_s.meeting_update_serializer
    http_method_names = ['patch','get','put']

class meeting_update_view_for_director(viewsets.ModelViewSet):
    queryset = game.meeting_BASCKETBALL.objects.all()
    permission_classes = []
    serializer_class = game_s.meeting_update_serializer_for_director
    http_method_names = ['patch','get']

class meeting_search_view(permissions.ListViewSet):
    queryset = game.meeting_BASCKETBALL.objects.order_by('-created_at')
    permission_classes = []
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['id','tournament','is_qualification']
    serializer_class = game_s.meeting_search_serializer

class meeting_reg_view(viewsets.ModelViewSet):
    queryset = game.meeting_BASCKETBALL.objects.all()
    permission_classes = [permissions.IsOrg]
    serializer_class = game_s.meeting_reg_serializer
    http_method_names = ['post', 'get',]

# ------------------------------------------------------------------------------ #

class match_update_view_for_org(viewsets.ModelViewSet):
    queryset = game.match_BASCKETBALL.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = game_s.match_update_serializer
    http_method_names = ['patch','get','put']

class match_update_view_for_director(viewsets.ModelViewSet):
    queryset = game.match_BASCKETBALL.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = game_s.match_update_serializer_for_director
    http_method_names = ['patch','get','put']

class match_search_view(permissions.ListViewSet):
    queryset = game.match_BASCKETBALL.objects.order_by('-created_at')
    permission_classes = []
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['meeting']
    serializer_class = game_s.match_search_serializer

class match_reg_view(viewsets.ModelViewSet):
    queryset = game.match_BASCKETBALL.objects.all()
    permission_classes = [permissions.IsOrg]
    serializer_class = game_s.match_reg_serializer
    http_method_names = ['post', 'get',]


# ------------------------------------------------------------------------------ #


class tournament_update_view_for_org(viewsets.ModelViewSet):
    queryset = game.tournament_BASCKETBALL.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = game_s.tournament_update_serializer
    http_method_names = ['patch','get','put']

class tournament_search_view(permissions.ListViewSet):
    queryset = game.tournament_BASCKETBALL.objects.order_by('-created_at')
    permission_classes = []
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filterset_fields = ['id']
    serializer_class = game_s.tournament_search_serializer

class tournament_search_short_view(permissions.ListViewSet):
    queryset = game.tournament_BASCKETBALL.objects.order_by('-created_at')
    permission_classes = []
    serializer_class = game_s.tournament_search_short_serializer
class tournament_reg_view(viewsets.ModelViewSet):
    queryset = game.tournament_BASCKETBALL.objects.all()
    permission_classes = [permissions.IsOrg]
    serializer_class = game_s.tournament_reg_serializer
    http_method_names = ['post', 'get',]

# ------------------------------------------------------------------------------ #


class application_meeting_update_view(viewsets.ModelViewSet):
    queryset = game.application_BASCKETBALL_meeting.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = game_s.application_meeting_update_serializer
    http_method_names = ['patch','get','put','delete']

class application_meeting_update_view_for_org(viewsets.ModelViewSet):
    queryset = game.application_BASCKETBALL_meeting.objects.all()
    permission_classes = [permissions.IsOrg]
    serializer_class = game_s.application_meeting_update_serializer_for_org
    http_method_names = ['patch','get','put','delete']

class application_meeting_search_view(permissions.ListViewSet):
    queryset = game.application_BASCKETBALL_meeting.objects.order_by('-created_at')
    permission_classes = []
    serializer_class = game_s.application_meeting_search_serializer

class application_meeting_reg_view(viewsets.ModelViewSet):
    queryset = game.application_BASCKETBALL_meeting.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = game_s.application_meeting_reg_serializer
    http_method_names = ['post', 'get',]


# ------------------------------------------------------------------------------ #

class application_tournament_reg_view(viewsets.ModelViewSet):
    queryset = game.application_BASCKETBALL_tournament.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = game_s.application_tournament_reg_serializer
    http_method_names = ['post', 'get',]

class application_tournament_search_view(permissions.ListViewSet):
    queryset = game.application_BASCKETBALL_tournament.objects.order_by('-date')
    permission_classes = []
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['tournament','team']
    serializer_class = game_s.application_tournament_search_serializer

class application_tournament_update_view(viewsets.ModelViewSet):
    queryset = game.application_BASCKETBALL_tournament.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = game_s.application_tournament_update_serializer
    http_method_names = ['patch','get','put']

class application_tournament_update_view_for_org(viewsets.ModelViewSet):
    queryset = game.application_BASCKETBALL_tournament.objects.all()
    permission_classes = [permissions.IsOrg]
    serializer_class = game_s.application_tournament_update_serializer_for_org
    http_method_names = ['patch','get','put']

# ------------------------------------------------------------------------------ #

class record_stat_reg_view(viewsets.ModelViewSet):
    queryset = game.record_stat.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = game_s.record_stat_reg_serializer
    http_method_names = ['post', 'get']

class record_stat_search_view(permissions.ListViewSet):
    queryset = game.record_stat.objects.all()
    permission_classes = []
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['user','match']
    serializer_class = game_s.record_stat_search_serializer