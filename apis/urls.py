from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("param/<str:param>", views.param, name="param"),
    path("exception/", views.exception, name="exception"),
    path("api/", views.api, name="api"),
    path("redis/", views.redis, name="redis"),
    path("mysql/", views.mysql, name="mysql"),
]
