from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import BasePermission, SAFE_METHODS, \
    IsAuthenticated, AllowAny
from django_filters import rest_framework as filters

from api import permissions
from unification.models import team
from unification.serializers import team as team_s



# ------------------------------------------------------------------------------ #

class team_update_view(viewsets.ModelViewSet):
    queryset = team.team.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = team_s.team_update_serializer
    http_method_names = ['patch','get','put', 'delete',]

class team_search_view(permissions.ListViewSet):
    queryset = team.team.objects.all()
    permission_classes = []
    serializer_class = team_s.team_search_serializer
    filter_backends = (DjangoFilterBackend,SearchFilter,)
    filterset_fields = ['director','id','direction',]
    search_fields = ('name',)

class team_reg_view(viewsets.ModelViewSet):
    queryset = team.team.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = team_s.team_reg_serializer
    http_method_names = ['post', 'get',]

# ------------------------------------------------------------------------------ #



class offers_reg_view(viewsets.ModelViewSet):
    queryset = team.offers.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = team_s.offers_reg_serializer
    http_method_names = ['post', 'get',]

class offers_search_view(permissions.ListViewSet):
    queryset = team.offers.objects.order_by('-created_at')
    permission_classes = []
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['user',]
    serializer_class = team_s.offers_search_serializer

class offers_search_view_short(permissions.ListViewSet):
    queryset = team.offers.objects.order_by('-created_at')
    permission_classes = []
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['user',]
    serializer_class = team_s.offers_search_serializer_short

class offers_delete_view_for_director(viewsets.ModelViewSet):
    queryset = team.offers.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = team_s.offers_delete_serializer
    http_method_names = ['get', 'delete','patch',]

# ------------------------------------------------------------------------------ #

