from django.contrib import admin
from django.urls import path, include

urlpatterns = [path("raihan_app/", include("login.urls")),
    path('admin/', admin.site.urls),
]
