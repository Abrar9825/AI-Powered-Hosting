from django.db import models
from django.utils import timezone

class TechStack(models.Model):
    # store everything as JSON
    data = models.JSONField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        langs = self.data.get("languages", [])
        return f"TechStack: {', '.join(langs)[:50]}"

class DeploymentPreference(models.Model):
    CODING_CHOICES = (("coding","coding"), ("no-code","no-code"))
    RUNTIME_CHOICES = (("static","static"), ("serverless","serverless"), ("container","container"))

    techstack = models.ForeignKey(TechStack, on_delete=models.CASCADE, related_name="preferences")
    coding_choice = models.CharField(max_length=10, choices=CODING_CHOICES)
    monthly_users = models.IntegerField(help_text="Estimate monthly active users")
    runtime = models.CharField(max_length=20, choices=RUNTIME_CHOICES)
    media_upload = models.BooleanField(default=False)
    auth_required = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.coding_choice} / {self.runtime} / {self.monthly_users} users"
    
class HostingSuggestion(models.Model):
    preference = models.ForeignKey(
        DeploymentPreference, on_delete=models.CASCADE, related_name="hosting_suggestions"
    )
    name = models.CharField(max_length=100)
    why = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)