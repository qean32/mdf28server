from django.contrib.auth import get_user_model
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework import generics, mixins, permissions
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.permissions import BasePermission, SAFE_METHODS, \
    IsAuthenticated, AllowAny
from rest_framework import viewsets, mixins, serializers

class ExtendedView:
    multi_permission_classes = None
    multi_serializer_class = None
    request = None
class ExtendedGenericViewSet(ExtendedView, GenericViewSet):
    pass
class ListViewSet(ExtendedGenericViewSet, mixins.ListModelMixin):
    pass
class UpdateViewSet(ExtendedGenericViewSet, mixins.UpdateModelMixin):
    pass
class DictMixinSerializer(serializers.Serializer):
    code = serializers.CharField()
    name = serializers.CharField()

class DictListMixin(ListViewSet):
    serializer_class = DictMixinSerializer
    pagination_class = None
    model = None


class IsNoBan(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if request.user.is_BAN == True:
            return False
        return True
class IsOrg(IsNoBan):
    def has_object_permission(self, request, view, obj):
        if request.user.is_org == True:
            return True
        return False
class IsUser(IsNoBan):
    def has_object_permission(self, request, view, obj):
        if request.user == obj:
            return True
        return False