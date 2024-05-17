from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from b_unification.models import player
from api.serializers_by import user_short_serializer,team_short_serializer


# ------------------------------------------------------------------------------ #



class player_update_serializer_for_director_DOTA(serializers.ModelSerializer):
    class Meta:
        model = player.player_DOTA
        fields = (
            'team',
        )

class player_update_serializer_for_org_DOTA(serializers.ModelSerializer):
    class Meta:
        model = player.player_DOTA
        fields = (
            'matches',
            'win_matches',
            'tournament',
            'win_tournament',
            'team',
            'matches_in_offers',
        )

class player_update_serializer_for_user_DOTA(serializers.ModelSerializer):
    class Meta:
        model = player.player_DOTA
        fields = (
            'rank',
            'mmr',
            'name',
            'team',
        )

class player_reg_serializer_DOTA(serializers.ModelSerializer):
    class Meta:
        model = player.player_DOTA
        fields = (
            '__all__'
        )

class player_search_serializer_DOTA(serializers.ModelSerializer):
    user = user_short_serializer()
    team = team_short_serializer()

    class Meta:
        model = player.player_DOTA
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
            'mmr',
            'rank',
        )
        depth = 2

# ------------------------------------------------------------------------------ #



class player_update_serializer_for_director_CS(serializers.ModelSerializer):
    class Meta:
        model = player.player_CS
        fields = (
            'team',
        )

class player_update_serializer_for_org_CS(serializers.ModelSerializer):
    class Meta:
        model = player.player_CS
        fields = (
            'matches',
            'win_matches',
            'tournament',
            'win_tournament',
            'team',
            'matches_in_offers',
        )

class player_update_serializer_for_user_CS(serializers.ModelSerializer):
    class Meta:
        model = player.player_CS
        fields = (
            'rank',
            'mmr',
            'name',
            'team',
        )

class player_reg_serializer_CS(serializers.ModelSerializer):
    class Meta:
        model = player.player_CS
        fields = (
            '__all__'
        )

class player_search_serializer_CS(serializers.ModelSerializer):
    user = user_short_serializer()
    team = team_short_serializer()

    class Meta:
        model = player.player_CS
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
            'mmr',
            'rank',
        )
        depth = 2

# ------------------------------------------------------------------------------ #



class player_update_serializer_for_director_BASCKETBALL(serializers.ModelSerializer):
    class Meta:
        model = player.player_BASCKETBALL
        fields = (
            'team',
        )

class player_update_serializer_for_org_BASCKETBALL(serializers.ModelSerializer):
    class Meta:
        model = player.player_BASCKETBALL
        fields = (
            'matches',
            'win_matches',
            'tournament',
            'win_tournament',
            'team',
            'matches_in_offers',
        )

class player_update_serializer_for_user_BASCKETBALL(serializers.ModelSerializer):
    class Meta:
        model = player.player_BASCKETBALL
        fields = (
            'rank',
            'mmr',
            'name',
            'team',
            'number',
        )

class player_reg_serializer_BASCKETBALL(serializers.ModelSerializer):
    class Meta:
        model = player.player_BASCKETBALL
        fields = (
            '__all__'
        )

class player_search_serializer_BASCKETBALL(serializers.ModelSerializer):
    user = user_short_serializer()
    team = team_short_serializer()

    class Meta:
        model = player.player_BASCKETBALL
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
            'number',
        )
        depth = 2
