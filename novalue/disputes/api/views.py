from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import BasePermission, SAFE_METHODS, \
    IsAuthenticated, AllowAny

from disputes import models
from disputes.models import message
from disputes.api import serializers
from api import permissions
from django_filters import rest_framework as filters
# ------------------------------------------------------------------------------ #

class message_reg_view(viewsets.ModelViewSet):
    queryset = models.message.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = serializers.message_reg_serializer
    http_method_names = ['get', 'post',]

class message_update_view(viewsets.ModelViewSet):
    queryset = models.message.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = serializers.message_update_serializer
    http_method_names = ['get', 'patch', 'put']

class message_search_view(viewsets.ModelViewSet):
    queryset = models.message.objects.order_by('-created_at')
    permission_classes = []
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['disput']
    serializer_class = serializers.message_search_serializer
class disput_search_view(viewsets.ModelViewSet):
    queryset = models.disput.objects.order_by('-created_at')
    permission_classes = []
    filter_backends = (SearchFilter,)
    search_fields = ('id',)
    serializer_class = serializers.disput_search_serializer

class disput_search_view_short(viewsets.ModelViewSet):
    queryset = models.disput.objects.all()
    permission_classes = []
    filter_backends = (SearchFilter,)
    search_fields = ('title',)
    serializer_class = serializers.disput_search_serializer_short

class disput_update_view_for_org(viewsets.ModelViewSet):
    queryset = models.disput.objects.all()
    permission_classes = [permissions.IsOrg]
    serializer_class = serializers.disput_update_serializer_for_org
    http_method_names = ['get', 'patch', 'put']

class disput_reg_view(viewsets.ModelViewSet):
    queryset = models.disput.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = serializers.disput_reg_serializer
    http_method_names = ['get', 'post']

