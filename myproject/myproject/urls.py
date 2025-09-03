from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/myapp/", include("myapp.urls")),  # link to your app urls
]
