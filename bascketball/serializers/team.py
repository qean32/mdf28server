from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from bascketball.models import team
from api.serializers_by import user_short_serializer,team_BASCKETBALL_short_serializer


# ------------------------------------------------------------------------------ #

class offers_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = team.offers_BASCKETBALL
        fields = (
            '__all__'
        )

class offers_search_serializer(serializers.ModelSerializer):
    team = team_BASCKETBALL_short_serializer()
    user = user_short_serializer()

    class Meta:
        model = team.offers_BASCKETBALL
        fields = (
            'id',
            'is_view',
            'user',
            'team',
            'generation',
            'position',
            'date',
            'matches_in_offers',
        )
        depth = 1

class offers_delete_serializer(serializers.ModelSerializer):
    class Meta:
        model = team.offers_BASCKETBALL
        fields = (
            '__all__'
        )

# ------------------------------------------------------------------------------ #


class team_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = team.team_BASCKETBALL
        fields = (
            '__all__'
        )


class team_search_serializer(serializers.ModelSerializer):
    director = user_short_serializer()
    class Meta:
        model = team.team_BASCKETBALL
        fields = (
            'id',
            'team_name',
            'logo',
            'background',
            'status',
            'detail',
            'director',
            'matches',
            'win_matches',
            'tournament',
            'win_tournament',
            'is_recognized',
            'cups',
            'color',
        )
        depth = 1

class team_update_serializer(serializers.ModelSerializer):
    class Meta:
        model = team.team_BASCKETBALL
        fields = (
            '__all__'
        )

class team_update_serializer_for_org(serializers.ModelSerializer):
    class Meta:
        model = team.team_BASCKETBALL
        fields = (
            'matches',
            'win_matches',
            'tournament',
            'win_tournament',
            'is_recognized',
        )


# ------------------------------------------------------------------------------ #



class player_update_serializer_for_director(serializers.ModelSerializer):
    class Meta:
        model = team.player_BASCKETBALL
        fields = (
            '__all__'
        )

class player_update_serializer_for_org(serializers.ModelSerializer):
    class Meta:
        model = team.player_BASCKETBALL
        fields = (
            'matches',
            'win_matches',
            'tournament',
            'win_tournament',
            'team_DOTA',
            'matches_in_offers',
        )

class player_update_serializer_for_org_matches_in_offers(serializers.ModelSerializer):
    class Meta:
        model = team.player_BASCKETBALL
        fields = (
            'matches_in_offers',
        )

class player_update_serializer_for_user(serializers.ModelSerializer):
    class Meta:
        model = team.player_BASCKETBALL
        fields = (
            '__all__'
        )

class player_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = team.player_BASCKETBALL
        fields = (
            '__all__'
        )

class player_search_serializer(serializers.ModelSerializer):
    user = user_short_serializer()
    team = team_BASCKETBALL_short_serializer()

    class Meta:
        model = team.player_BASCKETBALL
        fields = (
            'user',
            'team',
            'cups',
            'position',
            'generation',
            'name',
            'matches_in_offers',
            'matches',
            'win_matches',
            'tournament',
            'win_tournament',
            'is_recognized',
            'matches_in_offers',
            'number',
        )
        depth = 2