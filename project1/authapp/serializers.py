from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializations(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ('username' , 'password','email')
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


