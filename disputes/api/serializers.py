from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from users.models import User
from disputes import models
from disputes.models import message
from api.serializers_by import user_short_serializer

# ------------------------------------------------------------------------------ #


class message_reg_serializer(serializers.ModelSerializer):

     class Meta:
         model = models.message
         fields = (
             '__all__'
         )

class message_update_serializer(serializers.ModelSerializer):

    class Meta:
        model = models.message
        fields = (
            '__all__'
        )

class message_search_serializer(serializers.ModelSerializer):
    author = user_short_serializer()

    class Meta:
        model = models.message
        fields = (
            '__all__'
        )
# ------------------------------------------------------------------------------ #


class disput_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.disput
        fields = (
            '__all__'
        )

class disput_search_serializer(serializers.ModelSerializer):
    author = user_short_serializer()

    class Meta:
        model = models.disput
        fields = (
            '__all__'
        )

class disput_search_serializer_short(serializers.ModelSerializer):
    author = user_short_serializer()
    class Meta:
        model = models.disput
        fields = (
            'author',
            'title',
            'is_of',
        )
class disput_update_serializer_for_org(serializers.ModelSerializer):
    class Meta:
        model = models.disput
        fields = (
            '__all__'
        )