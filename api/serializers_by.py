from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from users.models import User
from dota.models.team import team_DOTA
from cs.models.team import team_CS
from bascketball.models.team import team_BASCKETBALL



class user_short_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'ava',
            'smail',
            'team_sap',
        )
        depth = 1

class team_DOTA_short_serializer(serializers.ModelSerializer):
    # director = user_short_serializer()

    class Meta:
        model = team_DOTA
        fields = (
            'id',
            'team_name',
            'logo',
            'director',
            'matches',
            'win_matches',
            'color',
        )
class team_CS_short_serializer(serializers.ModelSerializer):
    # director = user_short_serializer()

    class Meta:
        model = team_CS
        fields = (
            'id',
            'team_name',
            'logo',
            'director',
            'matches',
            'win_matches',
            'color',
        )

class team_BASCKETBALL_short_serializer(serializers.ModelSerializer):
    # director = user_short_serializer()

    class Meta:
        model = team_BASCKETBALL
        fields = (
            'id',
            'team_name',
            'logo',
            'director',
            'matches',
            'win_matches',
            'color',
        )