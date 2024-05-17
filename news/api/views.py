from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework.viewsets import GenericViewSet

from news.models import post,like,coment
from news.api import serializers
from api import permissions

# ------------------------------------------------------------------------------ #

class post_search_view(permissions.ListViewSet):
    queryset = post.objects.order_by('-created_at')
    permission_classes = []
    serializer_class = serializers.post_search_serializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['direction','is_blog']
    
# ------------------------------------------------------------------------------ #

class like_reg_view(viewsets.ModelViewSet):
    queryset = like.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = serializers.like_reg_serializer
    http_method_names = ['post', 'get']

class like_update_view(viewsets.ModelViewSet):
    queryset = like.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = serializers.like_update_serializer
    http_method_names = ['delete','get']

class like_search_view(permissions.ListViewSet):
    queryset = like.objects.all()
    permission_classes = []
    serializer_class = serializers.like_search_serializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['author','post']

# ------------------------------------------------------------------------------ #


class coment_reg_view(viewsets.ModelViewSet):
    queryset = coment.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = serializers.coment_reg_serializer

class coment_update_view(viewsets.ModelViewSet):
    queryset = coment.objects.all()
    permission_classes = [permissions.IsNoBan]
    serializer_class = serializers.coment_update_serializer
    http_method_names = ['patch','get','put']

class coment_search_view(permissions.ListViewSet):
    queryset = coment.objects.order_by('-created_at')
    permission_classes = []
    serializer_class = serializers.coment_search_serializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['author','post']
