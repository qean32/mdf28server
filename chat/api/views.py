from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import BasePermission, SAFE_METHODS, \
    IsAuthenticated, AllowAny

from chat.models import message,like_m
from chat.api import serializers
from api import permissions

# ------------------------------------------------------------------------------ #

class message_reg_view(viewsets.ModelViewSet):
    queryset = message.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = serializers.message_reg_serializer
    http_method_names = ['post', 'get']
class message_update_view(viewsets.ModelViewSet):
    queryset = message.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = serializers.message_update_serializer
    http_method_names = ['get', 'patch', 'put']

class message_search_view(viewsets.ModelViewSet):
    queryset = message.objects.order_by('-created_at')
    permission_classes = []
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['direction']
    serializer_class = serializers.message_search_serializer

# ------------------------------------------------------------------------------ #


class like_reg_view(viewsets.ModelViewSet):
    queryset = like_m.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = serializers.like_reg_serializer
    http_method_names = ['get', 'post']

class like_delite_view(viewsets.ModelViewSet):
    queryset = like_m.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = serializers.like_delite_serializer
    http_method_names = ['delete', 'patch']