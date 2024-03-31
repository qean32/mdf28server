from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import BasePermission, SAFE_METHODS, \
    IsAuthenticated, AllowAny
from django_filters import rest_framework as filters

from api import permissions
from dota.models import team
from dota.serializers import team as team_s



# ------------------------------------------------------------------------------ #

class player_reg_view(viewsets.ModelViewSet):
    queryset = team.player_DOTA.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = team_s.player_reg_serializer
    http_method_names = ['post', 'get']

class player_search_view(permissions.ListViewSet):
    queryset = team.player_DOTA.objects.order_by('-created_at')
    permission_classes = []
    serializer_class = team_s.player_search_serializer
    filter_backends = (DjangoFilterBackend,SearchFilter,)
    filterset_fields = ['team', 'user']
    search_fields = ('name',)

class player_update_view_for_director(viewsets.ModelViewSet):
    queryset = team.player_DOTA.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = team_s.player_update_serializer_for_director
    http_method_names = ['patch','get','put']

class player_update_view_for_org(viewsets.ModelViewSet):
    queryset = team.player_DOTA.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = team_s.player_update_serializer_for_org
    http_method_names = ['patch','get','put']

class player_update_view_for_user(viewsets.ModelViewSet):
    queryset = team.player_DOTA.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = team_s.player_update_serializer_for_user
    http_method_names = ['patch','get','put']

# ------------------------------------------------------------------------------ #



class team_update_view(viewsets.ModelViewSet):
    queryset = team.team_DOTA.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = team_s.team_update_serializer
    http_method_names = ['patch','get','put', 'delete']

class team_search_view(permissions.ListViewSet):
    queryset = team.team_DOTA.objects.order_by('-win_matches')
    permission_classes = []
    serializer_class = team_s.team_search_serializer
    filter_backends = (DjangoFilterBackend,SearchFilter,)
    filterset_fields = ['director','id']
    search_fields = ('team_name',)

class team_update_view_for_org(viewsets.ModelViewSet):
    queryset = team.team_DOTA.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = team_s.team_update_serializer_for_org
    http_method_names = ['patch','get','put']

class team_reg_view(viewsets.ModelViewSet):
    queryset = team.team_DOTA.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = team_s.team_reg_serializer
    http_method_names = ['post', 'get']

# ------------------------------------------------------------------------------ #



class offers_reg_view(viewsets.ModelViewSet):
    queryset = team.offers_DOTA.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = team_s.offers_reg_serializer
    http_method_names = ['post', 'get']

class offers_search_view(permissions.ListViewSet):
    queryset = team.offers_DOTA.objects.order_by('-date')
    permission_classes = []
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['user']
    serializer_class = team_s.offers_search_serializer

class offers_delete_view_for_director(viewsets.ModelViewSet):
    queryset = team.offers_DOTA.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = team_s.offers_delete_serializer
    http_method_names = ['get', 'delete','patch']

# ------------------------------------------------------------------------------ #

