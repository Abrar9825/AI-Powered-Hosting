from django.urls import path
from .views import extract_techstack,create_deployment_pref

urlpatterns = [
    path("extract/", extract_techstack, name="extract-techstack"),
    path("deployment/preferences/",create_deployment_pref,name="deployment-pref"),
]
