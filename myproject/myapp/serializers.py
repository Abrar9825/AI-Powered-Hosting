from rest_framework import serializers
from .models import TechStack, DeploymentPreference, HostingSuggestion

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
