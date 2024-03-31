from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from chat.models import message,like_m

from api.serializers_by import user_short_serializer

# ------------------------------------------------------------------------------ #

class message_reg_serializer(serializers.ModelSerializer):
     class Meta:
         model = message
         fields = (
             '__all__'
         )
class message_update_serializer(serializers.ModelSerializer):
    class Meta:
        model = message
        fields = (
            '__all__'
        )
class message_search_serializer(serializers.ModelSerializer):
    author = user_short_serializer()

    class Meta:
        model = message
        fields = (
            '__all__'
        )

# ------------------------------------------------------------------------------ #


class like_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = like_m
        fields = (
            '__all__'
        )

class like_delite_serializer(serializers.ModelSerializer):

    class Meta:
        model = like_m
        fields = (
            '__all__'
        )
