from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import BasePermission, SAFE_METHODS, \
    IsAuthenticated, AllowAny

from api import permissions
from poker.models import player
from poker.serializers import player as player_s

# ############################ - не трогать - ##########################################


class player_reg_view(viewsets.ModelViewSet):
    queryset = player.player_POKER.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = player_s.player_reg_serializer

class player_search_view(permissions.ListViewSet):
    queryset = player.player_POKER.objects.exclude()
    permission_classes = [AllowAny]
    filter_backend = (DjangoFilterBackend,)
    serializer_class = player_s.player_search_serializer
    filter_backends = (
       SearchFilter,
    )
    search_fields = (
        '__all__',
    )

class player_update_view_for_org(viewsets.ModelViewSet):
    queryset = player.player_POKER.objects.all()
    permission_classes = [permissions.IsOrg]
    serializer_class = player_s.player_update_serializer_for_org
    http_method_names = ['post', 'put', 'patch', 'get']

class player_update_view_for_user(viewsets.ModelViewSet):
    queryset = player.player_POKER.objects.all()
    permission_classes = [permissions.IsUser]
    serializer_class = player_s.player_update_serializer_for_user
    http_method_names = ['post', 'put', 'patch', 'get']


# ############################ - не трогать - ##########################################