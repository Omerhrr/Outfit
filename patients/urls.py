
from django.contrib import admin
from django.urls import path, include
from APP import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.frontend,name="frontend"),

    path("login/", include('django.contrib.auth.urls')),
    path("backend/", views.backend,name="backend"),
    
]
