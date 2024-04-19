from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from dota.models import game
from dota.models.team import team_DOTA
from users.models import User
from dota.serializers.team import player_search_serializer
from api.serializers_by import user_short_serializer,team_DOTA_short_serializer



# ------------------------------------------------------------------------------ #

class meeting_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.meeting_DOTA
        fields = (
            '__all__'
        )

class meeting_search_serializer(serializers.ModelSerializer):
    team_one = team_DOTA_short_serializer()
    team_two = team_DOTA_short_serializer()
    win_team = team_DOTA_short_serializer()
    class Meta:
        model = game.meeting_DOTA
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
        model = game.meeting_DOTA
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

class meeting_update_serializer_for_director(serializers.ModelSerializer):
    class Meta:
        model = game.meeting_DOTA
        fields = (
            'teams_structure_one',
            'teams_structure_two',
        )

# ------------------------------------------------------------------------------ #


class match_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.match_DOTA
        fields = (
            '__all__'
        )

class match_search_serializer(serializers.ModelSerializer):
    team_one = team_DOTA_short_serializer()
    team_two = team_DOTA_short_serializer()
    win_team = team_DOTA_short_serializer()
    class Meta:
        model = game.match_DOTA
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
        model = game.match_DOTA
        fields = (
            'team_one',
            'team_two',
            'win_team',
            'team_one_score',
            'team_two_score',
            'id_match',
            'time',
        )

class match_update_serializer_for_director(serializers.ModelSerializer):
    class Meta:
        model = game.match_DOTA
        fields = (
            'time',
        )

# ------------------------------------------------------------------------------ #

class tournament_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.tournament_DOTA
        fields = (
            '__all__'
        )

class tournament_search_serializer(serializers.ModelSerializer):

    class Meta:
        model = game.tournament_DOTA
        fields = (
            '__all__'
        )
        depth = 1
class tournament_search_short_serializer(serializers.ModelSerializer):

    class Meta:
        model = game.tournament_DOTA
        fields = (
            'name',
            'date',
            'id',
            'date',
        )
class tournament_update_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.tournament_DOTA
        fields = (
            'teams',
            'win_tournament',
            'is_on',
        )

# ------------------------------------------------------------------------------ #



class application_meeting_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.application_DOTA_meeting
        fields = (
            '__all__'
        )

class application_meeting_search_serializer(serializers.ModelSerializer):
    team_one = team_DOTA_short_serializer()
    team_two = team_DOTA_short_serializer()
    author = user_short_serializer()
    date = serializers.DateField(format="%Y-%m-%d")

    class Meta:
        model = game.application_DOTA_meeting
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
        model = game.application_DOTA_meeting
        fields = (
            'is_accept',
            'is_on',
        )

class application_meeting_update_serializer_for_org(serializers.ModelSerializer):
    class Meta:
        model = game.application_DOTA_meeting
        fields = (
            'is_accept',
            'is_on',
        )
# ------------------------------------------------------------------------------ #



class application_tournament_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.application_DOTA_tournament
        fields = (
            '__all__'
        )

class application_tournament_update_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.application_DOTA_tournament
        fields = (
            'is_on',
        )

class application_tournament_update_serializer_for_org(serializers.ModelSerializer):
    class Meta:
        model = game.application_DOTA_tournament
        fields = (
            'is_on',
        )

class application_tournament_search_serializer(serializers.ModelSerializer):
    team = team_DOTA_short_serializer()
    author = user_short_serializer()

    class Meta:
        model = game.application_DOTA_tournament
        fields = (
            'id',
            'tournament',
            'team',
            'date',
            'author',
            'is_on',
        )

# ################################# ############# #########################################   
        
class record_stat_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.record_stat
        fields = (
            '__all__'
        )


class record_stat_search_serializer(serializers.ModelSerializer):
    user = user_short_serializer()
    
    class Meta:
        model = game.record_stat
        fields = (
            'user',
            'match',
            'kill',
            'death',
            'assist',
            'hero',
            'damage',
            'win',
            'damage_t',
            'heal',
            'first_team',
            'gold',
        )
        depth = 1