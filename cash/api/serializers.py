from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from cash import models
from users.models import User

from api.serializers_by import user_short_serializer

# ------------------------------------------------------------------------------ #

class cash_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.cash
        fields = (
            '__all__'
        )

class cash_delete_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.cash
        fields = (
            '__all__'
        )

class list_cash_update_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.list_cash
        fields = (
            'price',
        )

class list_cash_search_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.list_cash
        fields = (
            'price',
        )
        
class cash_search_serializer(serializers.ModelSerializer):
    author = user_short_serializer()

    class Meta:
        model = models.cash
        fields = (
            'author',
            'price',
            'content',
            'created_at',
            'direction',
            'created_at',
        )
        depth = 1