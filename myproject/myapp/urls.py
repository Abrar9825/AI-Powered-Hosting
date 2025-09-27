from django.urls import path
from . import views
from .views import (
    extract_techstack,
    create_deployment_pref,
    RegisterAPI,
    LoginAPI,
    DashboardAPI,
)

urlpatterns = [
    # API endpoints
    path("extract/", extract_techstack, name="extract-techstack"),
    path("deployment/preferences/", create_deployment_pref, name="deployment-pref"),

    # Auth APIs
    path("api/register/", RegisterAPI.as_view(), name="register"),
    path("api/login/", LoginAPI.as_view(), name="login"),
    path("api/dashboard/", DashboardAPI.as_view(), name="dashboard"),

    # Frontend views
    path("", views.idea_input, name="idea_input"),
    path("login/", views.login_view, name="login"),
    path("questions/", views.questions, name="questions"),
    path("deploy-plan/", views.deploy_plan, name="deploy_plan"),
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
]
