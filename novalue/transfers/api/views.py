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

class transfer_search_view(permissions.ListViewSet):
    queryset = models.transfer.objects.order_by('-created_at')
    permission_classes = []
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['direction']
    serializer_class = serializers.transfer_search_serializer

class transfer_reg_view(viewsets.ModelViewSet):
    queryset = models.transfer.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = serializers.transfer_reg_serializer
    http_method_names = ['post', 'get']

# ------------------------------------------------------------------------------ #