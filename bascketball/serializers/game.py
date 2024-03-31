from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from bascketball.models import game
from bascketball.models.team import team_BASCKETBALL
from users.models import User
from bascketball.serializers.team import player_search_serializer
from api.serializers_by import user_short_serializer,team_BASCKETBALL_short_serializer



# ------------------------------------------------------------------------------ #

class meeting_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.meeting_BASCKETBALL
        fields = (
            '__all__'
        )

class meeting_search_serializer(serializers.ModelSerializer):
    team_one = team_BASCKETBALL_short_serializer()
    team_two = team_BASCKETBALL_short_serializer()
    win_team = team_BASCKETBALL_short_serializer()
    class Meta:
        model = game.meeting_BASCKETBALL
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
            'teams_structure_one',
            'teams_structure_two',
            'is_friends',
            'created_at',
            'tournament',
            'matches',
        )

class meeting_update_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.meeting_BASCKETBALL
        fields = (
            '__all__'
        )

class meeting_update_serializer_for_director(serializers.ModelSerializer):
    class Meta:
        model = game.meeting_BASCKETBALL
        fields = (
            'teams_structure_one',
            'teams_structure_two',
        )

# ------------------------------------------------------------------------------ #


class match_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.match_BASCKETBALL
        fields = (
            '__all__'
        )

class match_search_serializer(serializers.ModelSerializer):
    team_one = team_BASCKETBALL_short_serializer()
    team_two = team_BASCKETBALL_short_serializer()
    win_team = team_BASCKETBALL_short_serializer()
    class Meta:
        model = game.match_BASCKETBALL
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
            'win_team',
        )

class match_update_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.match_BASCKETBALL
        fields = (
            '__all__'
        )

class match_update_serializer_for_director(serializers.ModelSerializer):
    class Meta:
        model = game.match_BASCKETBALL
        fields = (
            'time',
        )

# ------------------------------------------------------------------------------ #



class tournament_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.tournament_BASCKETBALL
        fields = (
            '__all__'
        )

class tournament_search_serializer(serializers.ModelSerializer):

    class Meta:
        model = game.tournament_BASCKETBALL
        fields = (
            '__all__'
        )
        depth = 1
class tournament_search_short_serializer(serializers.ModelSerializer):

    class Meta:
        model = game.tournament_BASCKETBALL
        fields = (
            'name',
            'date',
            'id',
            'date',
        )
class tournament_update_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.tournament_BASCKETBALL
        fields = (
            '__all__'
        )

# ------------------------------------------------------------------------------ #



class application_meeting_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.application_BASCKETBALL_meeting
        fields = (
            '__all__'
        )

class application_meeting_search_serializer(serializers.ModelSerializer):
    team_one = team_BASCKETBALL_short_serializer()
    team_two = team_BASCKETBALL_short_serializer()
    author = user_short_serializer()
    date = serializers.DateField(format="%Y-%m-%d")

    class Meta:
        model = game.application_BASCKETBALL_meeting
        fields = (
            'id',
            'team_one',
            'team_two',
            'date',
            'author',
            'is_accept',
            'is_on',
            'matches',
            'time1',
            'time2',
        )

class application_meeting_update_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.application_BASCKETBALL_meeting
        fields = (
            '__all__'
        )

class application_meeting_update_serializer_for_org(serializers.ModelSerializer):
    class Meta:
        model = game.application_BASCKETBALL_meeting
        fields = (
            '__all__'
        )

# ------------------------------------------------------------------------------ #



class application_tournament_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.application_BASCKETBALL_tournament
        fields = (
            '__all__'
        )

class application_tournament_update_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.application_BASCKETBALL_tournament
        fields = (
            '__all__'
        )

class application_tournament_update_serializer_for_org(serializers.ModelSerializer):
    class Meta:
        model = game.application_BASCKETBALL_tournament
        fields = (
            '__all__'
        )

class application_tournament_search_serializer(serializers.ModelSerializer):
    team = team_BASCKETBALL_short_serializer()
    author = user_short_serializer()

    class Meta:
        model = game.application_BASCKETBALL_tournament
        fields = (
            'id',
            'tournament',
            'team',
            'date',
            'author',
            'is_on',
        )