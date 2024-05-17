from django.contrib.auth import get_user_model
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.permissions import BasePermission, SAFE_METHODS, \
    IsAuthenticated, AllowAny
from rest_framework import viewsets, mixins

from api import permissions
from users.api import serializers
from users import models

User = get_user_model()




# ------------------------------------------------------------------------------ #

class RegistrationView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = []
    serializer_class = serializers.RegistrationSerializer
    http_method_names = ['post', 'get']

class UserListSearchView(permissions.ListViewSet):
    queryset = User.objects.order_by('-created_at')
    permission_classes = []
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['id']
    serializer_class = serializers.UserSearchListSerializer

class UserUpdateView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.IsUser]
    serializer_class = serializers.UserUpdateSerializer
    http_method_names = ['get', 'patch', 'put']
    
class UserListSearchView_short(permissions.ListViewSet):
    queryset = User.objects.order_by('-created_at')
    permission_classes = []
    serializer_class = serializers.UserSearchListSerializer_short
    filter_backends = (SearchFilter,DjangoFilterBackend)
    filterset_fields = ['id']
    search_fields = ('first_name','last_name',)

class ChangePasswordView(APIView):
    def post(self, request):
        user = request.user
        serializer = serializers.ChangePasswordSerializer(
            instance=user, data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=HTTP_204_NO_CONTENT)

class ChangeEmailView(APIView):
    def post(self, request):
        user = request.user
        serializer = serializers.ChangeEmailSerializer(
            instance=user, data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=HTTP_204_NO_CONTENT)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.MyTokenObtainPairSerializer

class FollowListSearchView_id(permissions.ListViewSet):
    queryset = models.follow.objects.all()
    permission_classes = []
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['for_r', 'by']
    serializer_class = serializers.follow_search_serializer_id

class FollowListSearchView(permissions.ListViewSet):
    queryset = models.follow.objects.all()
    permission_classes = []
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['for_r', 'by']
    serializer_class = serializers.follow_search_serializer

class FollowRegView(viewsets.ModelViewSet):
    queryset = models.follow.objects.all()
    permission_classes = [permissions.IsNoBan]
    filter_backends = (DjangoFilterBackend,)
    serializer_class = serializers.follow_reg_serializer
    http_method_names = ['get', 'post']

class FollowDeleteView(viewsets.ModelViewSet):
    queryset = models.follow.objects.all()
    permission_classes = [permissions.IsNoBan]
    filter_backends = (DjangoFilterBackend,SearchFilter)
    serializer_class = serializers.follow_delite_serializer
    http_method_names = ['get', 'delete',]