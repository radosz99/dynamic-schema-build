from django.urls import path

from config.dynamic_schema_build import views


urlpatterns = [
    path("", views.index, name="index"),
]