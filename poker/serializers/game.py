from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from poker.models import game

class match_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.match_POKER
        fields = (
            '__all__'
        )

class match_search_serializer(serializers.ModelSerializer):

    class Meta:
        model = game.match_POKER
        fields = (
            '__all__'
        )
        depth = 1

class match_update_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.match_POKER
        fields = (
            '__all__'
        )

class match_update_serializer_player(serializers.ModelSerializer):
    class Meta:
        model = game.match_POKER
        fields = (
            '__all__'
        )

# ############################ - не трогать - ##########################################


class tournament_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.tournament_POKER
        fields = (
            '__all__'
        )

class tournament_search_serializer(serializers.ModelSerializer):

    class Meta:
        model = game.tournament_POKER
        fields = (
            '__all__'
        )
        depth = 1

class tournament_update_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.tournament_POKER
        fields = (
            '__all__'
        )

class tournament_update_serializer_for_player(serializers.ModelSerializer):
    class Meta:
        model = game.tournament_POKER
        fields = (
            'player',
        )

# ############################ - не трогать - ##########################################



class application_tournament_no_team_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.application_POKER_tournament_no_team
        fields = (
            '__all__'
        )

class application_tournament_no_team_update_serializer(serializers.ModelSerializer):
    class Meta:
        model = game.application_POKER_tournament_no_team
        fields = (
            '__all__'
        )

class application_tournament_no_team_update_serializer_for_org(serializers.ModelSerializer):
    class Meta:
        model = game.application_POKER_tournament_no_team
        fields = (
            '__all__'
        )

class tournament_no_team_update_serializer_for_player(serializers.ModelSerializer):
    class Meta:
        model = game.tournament_POKER
        fields = (
            'applications'
        )
