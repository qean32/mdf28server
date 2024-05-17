from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from transfers import models
from users.models import User
from api.serializers_by import user_short_serializer,team_short_serializer


# ------------------------------------------------------------------------------ #

class transfer_reg_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.transfer
        fields = (
            '__all__'
        )

class transfer_search_serializer(serializers.ModelSerializer):
    user = user_short_serializer()
    team = team_short_serializer()

    class Meta:
        model = models.transfer
        fields = (
            'user',
            'team',
            'script',
            'created_at',
            'direction',
        )
        depth = 1

# ------------------------------------------------------------------------------ #