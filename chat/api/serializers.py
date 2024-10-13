from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from chat.models import message

from api.serializers_by import user_short_serializer

# ------------------------------------------------------------------------------ #

class message_reg_serializer(serializers.ModelSerializer):
     class Meta:
         model = message
         fields = (
             '__all__'
         )
        
class message_search_serializer(serializers.ModelSerializer):
    author = user_short_serializer()

    class Meta:
        model = message
        fields = (
            '__all__'
        )

# ------------------------------------------------------------------------------ #