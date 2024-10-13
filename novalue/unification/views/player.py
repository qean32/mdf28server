from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import BasePermission, SAFE_METHODS, \
    IsAuthenticated, AllowAny
from django_filters import rest_framework as filters

from api import permissions
from unification.models import player
from unification.serializers import player as player_s



# ------------------------------------------------------------------------------ #

class player_reg_view_DOTA(viewsets.ModelViewSet):
    queryset = player.player_DOTA.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = player_s.player_reg_serializer_DOTA
    http_method_names = ['post', 'get']

class player_search_view_DOTA(permissions.ListViewSet):
    queryset = player.player_DOTA.objects.order_by('-matches')
    permission_classes = []
    serializer_class = player_s.player_search_serializer_DOTA
    filter_backends = (DjangoFilterBackend,SearchFilter,)
    filterset_fields = ['team', 'user']
    search_fields = ('name',)

class player_update_view_for_director_DOTA(viewsets.ModelViewSet):
    queryset = player.player_DOTA.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = player_s.player_update_serializer_for_director_DOTA
    http_method_names = ['patch','get','put']

class player_update_view_for_org_DOTA(viewsets.ModelViewSet):
    queryset = player.player_DOTA.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = player_s.player_update_serializer_for_org_DOTA
    http_method_names = ['patch','get','put']

class player_update_view_for_user_DOTA(viewsets.ModelViewSet):
    queryset = player.player_DOTA.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = player_s.player_update_serializer_for_user_DOTA
    http_method_names = ['patch','get','put']

# ------------------------------------------------------------------------------ #

class player_reg_view_CS(viewsets.ModelViewSet):
    queryset = player.player_CS.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = player_s.player_reg_serializer_CS
    http_method_names = ['post', 'get']

class player_search_view_CS(permissions.ListViewSet):
    queryset = player.player_CS.objects.order_by('-matches')
    permission_classes = []
    serializer_class = player_s.player_search_serializer_CS
    filter_backends = (DjangoFilterBackend,SearchFilter,)
    filterset_fields = ['team', 'user']
    search_fields = ('name',)

class player_update_view_for_director_CS(viewsets.ModelViewSet):
    queryset = player.player_CS.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = player_s.player_update_serializer_for_director_CS
    http_method_names = ['patch','get','put']

class player_update_view_for_org_CS(viewsets.ModelViewSet):
    queryset = player.player_CS.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = player_s.player_update_serializer_for_org_CS
    http_method_names = ['patch','get','put']

class player_update_view_for_user_CS(viewsets.ModelViewSet):
    queryset = player.player_CS.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = player_s.player_update_serializer_for_user_CS
    http_method_names = ['patch','get','put']

    
# ------------------------------------------------------------------------------ #

class player_reg_view_BASCKETBALL(viewsets.ModelViewSet):
    queryset = player.player_BASCKETBALL.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = player_s.player_reg_serializer_BASCKETBALL
    http_method_names = ['post', 'get']

class player_search_view_BASCKETBALL(permissions.ListViewSet):
    queryset = player.player_BASCKETBALL.objects.order_by('-matches')
    permission_classes = []
    serializer_class = player_s.player_search_serializer_BASCKETBALL
    filter_backends = (DjangoFilterBackend,SearchFilter,)
    filterset_fields = ['team', 'user']
    search_fields = ('name',)

class player_update_view_for_director_BASCKETBALL(viewsets.ModelViewSet):
    queryset = player.player_BASCKETBALL.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = player_s.player_update_serializer_for_director_BASCKETBALL
    http_method_names = ['patch','get','put']

class player_update_view_for_org_BASCKETBALL(viewsets.ModelViewSet):
    queryset = player.player_BASCKETBALL.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = player_s.player_update_serializer_for_org_BASCKETBALL
    http_method_names = ['patch','get','put']

class player_update_view_for_user_BASCKETBALL(viewsets.ModelViewSet):
    queryset = player.player_BASCKETBALL.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = player_s.player_update_serializer_for_user_BASCKETBALL
    http_method_names = ['patch','get','put']

# ------------------------------------------------------------------------------ #