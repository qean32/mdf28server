from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from transfers import models
from users.models import User
from dota.models.team import team_DOTA
from cs.models.team import team_CS
from bascketball.models.team import team_BASCKETBALL
from api.serializers_by import user_short_serializer,team_DOTA_short_serializer


# ------------------------------------------------------------------------------ #

class transfer_DOTA_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.transfer_DOTA
        fields = (
            '__all__'
        )

class transfer_DOTA_search_serializer(serializers.ModelSerializer):
    user = user_short_serializer()
    team = team_DOTA_short_serializer()
    class Meta:
        model = models.transfer_DOTA
        fields = (
            'user',
            'team',
            'script',
            'date_crate',
        )
        depth = 1

# ------------------------------------------------------------------------------ #


class transfer_CS_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.transfer_CS
        fields = (
            '__all__'
        )

class transfer_CS_search_serializer(serializers.ModelSerializer):
    user = user_short_serializer()

    class Meta:
        model = models.transfer_CS
        fields = (
            'user',
            'team',
            'script',
            'date_crate',
        )
        depth = 1

# ------------------------------------------------------------------------------ #


class transfer_BASCKETBALL_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.transfer_BASCKETBALL
        fields = (
            '__all__'
        )

class transfer_BASCKETBALL_search_serializer(serializers.ModelSerializer):
    user = user_short_serializer()

    class Meta:
        model = models.transfer_BASCKETBALL
        fields = (
            'user',
            'team',
            'script',
            'date_crate',
        )
        depth = 1
