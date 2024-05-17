from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from users.models import User
from b_unification.models.team import team



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

class team_short_serializer(serializers.ModelSerializer):
    # director = user_short_serializer()

    class Meta:
        model = team
        fields = (
            'id',
            'name',
            'logo',
            'director',
            'matches',
            'color',
        )