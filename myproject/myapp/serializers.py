from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import TechStack, DeploymentPreference, HostingSuggestion


# 🔹 Existing Serializers for Your Models
class TechStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechStack
        fields = "__all__"


class HostingSuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostingSuggestion
        fields = ["id", "name", "why", "created_at"]


class DeploymentPreferenceSerializer(serializers.ModelSerializer):
    hosting_suggestions = HostingSuggestionSerializer(many=True, read_only=True)

    class Meta:
        model = DeploymentPreference
        fields = "__all__"


# 🔹 New Serializers for Authentication
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "email", "password")

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Credentials")
