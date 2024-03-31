from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from poker.models import player

class director_short_serializer(serializers.ModelSerializer):

    class Meta:
        model = player.User
        fields = (
            'id',
            'full_name',
            'ava'
        )

class player_update_serializer_for_org(serializers.ModelSerializer):
    class Meta:
        model = player.player_POKER
        fields = (
            'matches',
            'win_matches',
            'tournament',
            'win_tournament',
        )

class player_update_serializer_for_user(serializers.ModelSerializer):
    class Meta:
        model = player.player_POKER
        fields = (
            '__all__'
        )

class player_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = player.player_POKER
        fields = (
            '__all__'
        )

class player_search_serializer(serializers.ModelSerializer):
    user = director_short_serializer()

    class Meta:
        model = player.player_POKER
        fields = (
            '__all__'
        )
        depth = 1