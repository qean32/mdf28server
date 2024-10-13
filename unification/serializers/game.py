from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from unification.models import game
from unification.models.team import team
from users.models import User
from api.serializers_by import user_short_serializer,team_short_serializer



# ------------------------------------------------------------------------------ #

class meeting_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.meeting
        fields = (
            '__all__'
        )

class meeting_search_serializer(serializers.ModelSerializer):
    team_one = team_short_serializer()
    team_two = team_short_serializer()
    win_team = team_short_serializer()

    class Meta:
        model = game.meeting
        fields = (
            'id',
            'team_one',
            'team_two',
            'win_team',
            'team_one_score',
            'team_two_score',
            'team_one_ball',
            'team_two_ball',
            'is_friends',
            'is_qualification',
            'date',
            'created_at',
            'tournament',
            'countmatch',
            'direction',
        )

class meeting_update_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.meeting
        fields = (
            'team_one',
            'team_two',
            'win_team',
            'team_one_score',
            'team_two_score',
            'team_one_ball',
            'team_two_ball',
            'date',
        )

# ------------------------------------------------------------------------------ #


class match_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.match
        fields = (
            '__all__'
        )

class match_search_serializer(serializers.ModelSerializer):
    team_one = team_short_serializer()
    team_two = team_short_serializer()
    win_team = team_short_serializer()
    class Meta:
        model = game.match
        fields = (
            'id',
            'team_one',
            'team_two',
            'win_team',
            'team_one_score',
            'team_two_score',
            'time',
            'id_match',
            'meeting',
            'direction',
            'created_at',
        )

class match_update_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.match
        fields = (
            'team_one',
            'team_two',
            'win_team',
            'team_one_score',
            'team_two_score',
            'id_match',
            'time',
        )

# ------------------------------------------------------------------------------ #

class tournament_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.tournament
        fields = (
            '__all__'
        )

class tournament_search_serializer(serializers.ModelSerializer):

    class Meta:
        model = game.tournament
        fields = (
            '__all__'
        )
        depth = 1

class tournament_search_short_serializer(serializers.ModelSerializer):

    class Meta:
        model = game.tournament
        fields = (
            'name',
            'date',
            'id',
            'direction',
        )

class tournament_update_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.tournament
        fields = (
            'teams',
            'is_on',
            'win_tournament',
        )

# ------------------------------------------------------------------------------ #


class application_tournament_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.application_tournament
        fields = (
            '__all__'
        )

class application_tournament_update_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.application_tournament
        fields = (
            'is_on',
        )

class application_tournament_search_serializer(serializers.ModelSerializer):
    team = team_short_serializer()

    class Meta:
        model = game.application_tournament
        fields = (
            'id',
            'tournament',
            'team',
            'is_on',
        )