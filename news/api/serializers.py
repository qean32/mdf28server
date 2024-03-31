from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from news.models import post,like,coment,direction

from users.models import User
from api.serializers_by import user_short_serializer

# ------------------------------------------------------------------------------ #

class post_search_serializer(serializers.ModelSerializer):
    author = user_short_serializer()
    class Meta:
        model = post
        fields = (
            'id',
            'content',
            'author',
            'created_at',
            'image',
            'direction',
        )
        depth = 1

# ------------------------------------------------------------------------------ #


class like_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = like
        fields = (
            '__all__'
        )

class like_update_serializer(serializers.ModelSerializer):
    author = user_short_serializer()

    class Meta:
        model = like
        fields = (
            'postt',
            'author',
        )

class like_search_serializer(serializers.ModelSerializer):
    author = user_short_serializer()
    class Meta:
        model = like
        fields = (
            '__all__'
        )

# ------------------------------------------------------------------------------ #


class coment_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = coment
        fields = (
            '__all__'
        )

class coment_update_serializer(serializers.ModelSerializer):
    class Meta:
        model = coment
        fields = (
            '__all__'
        )

class coment_search_serializer(serializers.ModelSerializer):
    author = user_short_serializer()
    class Meta:
        model = coment
        fields = (
            'content',
            'author',
            'created_at',
            'post',
        )