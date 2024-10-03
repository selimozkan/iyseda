from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomePage, name="home"),
    path("change-languge/<str:lng>", views.ChangeLanguage, name="change-language"),
]
