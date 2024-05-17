from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import BasePermission, SAFE_METHODS, \
    IsAuthenticated, AllowAny

from api import permissions
from cash import models
from cash.api import serializers


# ------------------------------------------------------------------------------ #

class list_cash_update_view(viewsets.ModelViewSet):
    queryset = models.list_cash.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = serializers.list_cash_update_serializer
    http_method_names = ['patch', 'get','put']

class list_cash_search_view(permissions.ListViewSet):
    queryset = models.list_cash.objects.all()
    permission_classes = []
    serializer_class = serializers.list_cash_search_serializer

class cash_search_view(permissions.ListViewSet):
    queryset = models.cash.objects.order_by('-created_at')
    permission_classes = []
    serializer_class = serializers.cash_search_serializer
    
class cash_reg_view(viewsets.ModelViewSet):
    queryset = models.cash.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = serializers.cash_reg_serializer
    http_method_names = ['post', 'get',]

class cash_delete_view(viewsets.ModelViewSet):
    queryset = models.list_cash.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = serializers.cash_delete_serializer
    http_method_names = ['get', 'patch', 'put']