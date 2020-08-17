from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name = "home"),
    path("index/",views.index, name = "index"),
    path("index/<int:article_id>/", views.detail, name = "detail"),
    path("create/", views.create, name = "create"),
    path("index/<int:article_id>/update/", views.update, name = "update"),
    path("index/<int:article_id>/delete/", views.delete, name = "delete"),
    # path("signup", views.signup, name = "signup"),
]