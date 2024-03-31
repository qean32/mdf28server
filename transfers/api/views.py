from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import BasePermission, SAFE_METHODS, \
    IsAuthenticated, AllowAny

from api import permissions
from transfers import models
from transfers.api import serializers


# ------------------------------------------------------------------------------ #

class transfer_DOTA_search_view(permissions.ListViewSet):
    queryset = models.transfer_DOTA.objects.order_by('-date_crate')
    permission_classes = []
    serializer_class = serializers.transfer_DOTA_search_serializer

class transfer_DOTA_reg_view(viewsets.ModelViewSet):
    queryset = models.transfer_DOTA.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = serializers.transfer_DOTA_reg_serializer
    http_method_names = ['post', 'get']
# ------------------------------------------------------------------------------ #


class transfer_CS_search_view(permissions.ListViewSet):
    queryset = models.transfer_CS.objects.order_by('-date_crate')
    permission_classes = []
    serializer_class = serializers.transfer_CS_search_serializer

class transfer_CS_reg_view(viewsets.ModelViewSet):
    queryset = models.transfer_CS.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = serializers.transfer_CS_reg_serializer
    http_method_names = ['post', 'get']
# ------------------------------------------------------------------------------ #


class transfer_BASCKETBALL_search_view(permissions.ListViewSet):
    queryset = models.transfer_BASCKETBALL.objects.order_by('-date_crate')
    permission_classes = []
    serializer_class = serializers.transfer_BASCKETBALL_search_serializer

class transfer_BASCKETBALL_reg_view(viewsets.ModelViewSet):
    queryset = models.transfer_BASCKETBALL.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = serializers.transfer_BASCKETBALL_reg_serializer
    http_method_names = ['post', 'get']

# ------------------------------------------------------------------------------ #
