from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers

#UserSerializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','username', 'email']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create(validated_data['username'], validated_data['email'], validated_data['password'])
    
        return user

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")