from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from b_unification.models import game
from b_unification.models.team import team
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
            'is_qualification',
            'team_one_ball',
            'team_two_ball',
            'date',
            'is_friends',
            'created_at',
            'tournament',
            'matches',
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
            'id_match',
            'time',
            'created_at',
            'meeting',
            'direction',
            'win_team',
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



class application_meeting_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.application_meeting
        fields = (
            '__all__'
        )

class application_meeting_search_serializer(serializers.ModelSerializer):
    team_one = team_short_serializer()
    team_two = team_short_serializer()
    date = serializers.DateField(format="%Y-%m-%d")

    class Meta:
        model = game.application_meeting
        fields = (
            'id',
            'team_one',
            'team_two',
            'date',
            'is_accept',
            'is_on',
            'matches',
            'time1',
            'time2',
            'direction',
        )

class application_meeting_update_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.application_meeting
        fields = (
            'is_accept',
            'is_on',
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

# ################################# ############# #########################################   