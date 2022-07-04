from django.urls import path
from . import views

urlpatterns = [path("login/", views.main_login, name="login"),
path("login/detection/", views.detection, name="detection"),
path("login/register/", views.register_page, name="register"),
path("login/register/register_process/", views.reg_process, name="register2"),
path("see_database/", views.see_database, name="database"),
path("see_database/delete/<int:id>/", views.delete, name='delete'),
path("login/detection/main_app/<int:id>", views.main_app, name='main')
]
