from django.urls import path
from . import views
from .views import extract_techstack, create_deployment_pref

urlpatterns = [
    path('', views.idea_input, name='idea_input'),
    path("extract/", extract_techstack, name="extract-techstack"),
    path("deployment/preferences/", create_deployment_pref, name="deployment-pref"),
    path('', views.idea_input, name='idea_input'),
    path('login/', views.login_view, name='login'),
    path('questions/', views.questions, name='questions'),
    path('deploy-plan/', views.deploy_plan, name='deploy_plan'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
