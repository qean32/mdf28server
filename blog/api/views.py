from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import BasePermission, SAFE_METHODS, \
    IsAuthenticated, AllowAny

from blog.models import post
from blog.api import serializers
from api import permissions


# ############################ - не трогать - ##########################################

class post_reg_view(viewsets.ModelViewSet):
    queryset = post.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = serializers.post_reg_serializer

class post_search_view(permissions.ListViewSet):
    queryset = post.objects.exclude()
    permission_classes = []
    filter_backend = (DjangoFilterBackend,)
    serializer_class = serializers.post_search_serializer
    filter_backends = (
       SearchFilter,
    )
    search_fields = (
        '__all__',
    )

class post_update_view(viewsets.ModelViewSet):
    queryset = post.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = serializers.post_update_serializer


# ############################ - не трогать - ##########################################