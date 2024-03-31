from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from blog.models import post
from users.models import User

# ############################ - не трогать - ##########################################

class post_reg_serializer(serializers.ModelSerializer):

     class Meta:
         model = post
         fields = (
             '__all__'
         )
class post_search_serializer(serializers.ModelSerializer):

    class Meta:
        model = post
        fields = (
            '__all__'
        )
        depth = 1

class post_update_serializer(serializers.ModelSerializer):

    class Meta:
        model = post
        fields = (
            '__all__'
        )


# ############################ - не трогать - ##########################################