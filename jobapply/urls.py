# jobapply/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("suggest/titles/", views.suggest_titles, name="suggest_titles"),
    path("suggest/locations/", views.suggest_locations, name="suggest_locations"),
]
