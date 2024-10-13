from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from unification.models import team
from api.serializers_by import user_short_serializer,team_short_serializer


# ------------------------------------------------------------------------------ #

class offers_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = team.offers
        fields = (
            '__all__'
        )

class offers_search_serializer(serializers.ModelSerializer):
    team = team_short_serializer()
    user = user_short_serializer()

    class Meta:
        model = team.offers
        fields = (
            'id',
            'is_view',
            'user',
            'team',
            'created_at',
            'matches_in_offers',
            'direction',
        )
        depth = 1

class offers_search_serializer_short(serializers.ModelSerializer):
    team = team_short_serializer()
    user = user_short_serializer()

    class Meta:
        model = team.offers
        fields = (
            'id',
            'is_view',
            'user',
            'team',
        )
        depth = 1

class offers_delete_serializer(serializers.ModelSerializer):
    class Meta:
        model = team.offers
        fields = (
            '__all__'
        )

# ------------------------------------------------------------------------------ #


class team_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = team.team
        fields = (
            '__all__'
        )


class team_search_serializer(serializers.ModelSerializer):
    director = user_short_serializer()
    class Meta:
        model = team.team
        fields = (
            'id',
            'name',
            'logo',
            'background',
            'status',
            'detail',
            'director',
            'is_recognized',
            'direction',
        )
        depth = 1

class team_update_serializer(serializers.ModelSerializer):
    class Meta:
        model = team.team
        fields = (
            '__all__'
        )

# ------------------------------------------------------------------------------ #

class player_update_serializer_for_director(serializers.ModelSerializer):
    class Meta:
        model = team.player
        fields = (
            'team_dota',
            'team_cs',
        )

class player_update_serializer(serializers.ModelSerializer):
    class Meta:
        model = team.player
        fields = (
            'name',
            'team_dota',
            'team_cs',
        )

class player_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = team.player
        fields = (
            '__all__'
        )

class player_search_serializer(serializers.ModelSerializer):
    user = user_short_serializer()
    team = team_short_serializer()

    class Meta:
        model = team.player
        fields = (
            'user',
            'name',
            'team_dota',
            'team_cs',
        )
        depth = 2
