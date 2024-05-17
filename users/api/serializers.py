from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.db import transaction,models
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ParseError
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()
from users import models
from api.serializers_by import user_short_serializer


# ------------------------------------------------------------------------------ #

class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True
    )
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
            'id',
        )
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# ------------------------------------------------------------------------------ #


class SmailSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.smail
        fields = (
            'image',
        )

class UserSearchListSerializer(serializers.ModelSerializer):
    smail = SmailSerializers()

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'ava',
            'background',
            'status',
            'smail',
            'team_sap',
            'roles',
            'steam',
            'is_org',
            'is_BAN',
        )
        depth = 1

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            '__all__'
        )
        
class UserSearchListSerializer_short(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'team_sap',
            'smail',
            'ava',
            'is_org',
        )
        depth = 1
# ------------------------------------------------------------------------------ #

class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('old_password', 'new_password')

    def validate(self, attrs):
        user = self.instance
        old_password = attrs.pop('old_password')
        if not user.check_password(old_password):
            raise ParseError(
                'Проверьте правильность текущего пароля.'
            )
        return attrs

    def validate_new_password(self, value):
        validate_password(value)
        return value

    def update(self, instance, validated_data):
        password = validated_data.pop('new_password')
        instance.set_password(password)
        instance.save()
        return instance


class ChangeEmailSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = User
        fields = ('password', 'email')

    def validate(self, attrs):
        user = self.instance
        password = attrs.pop('password')
        if not user.check_password(password):
            raise ParseError(
                'Проверьте правильность текущего пароля.'
            )
        return attrs

    def update(self, instance, validated_data):
        with transaction.atomic():
            instance = super().update(instance, validated_data)
        return instance
# ------------------------------------------------------------------------------ #


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):

        token = super().get_token(user)
        token['id'] = user.id
        token['is_org'] = user.is_org

        return token
# ------------------------------------------------------------------------------ #


class follow_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.follow
        fields = (
            'for_r',
            'by',
        )

class follow_delite_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.follow
        fields = (
            'for_r',
            'by',
        )
class follow_search_serializer_id(serializers.ModelSerializer):
    class Meta:
        model = models.follow
        fields = (
            'id',
            'for_r',
            'by',
        )
class follow_search_serializer(serializers.ModelSerializer):
    for_r = user_short_serializer()
    by = user_short_serializer()

    class Meta:
        model = models.follow
        fields = (
            'for_r',
            'by',
        )