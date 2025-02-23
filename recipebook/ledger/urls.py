from django.urls import path
from .views import home, recipelist, foodrecipe

urlpatterns = [
    path('', home, name="home"),
    path("recipes/list/", recipelist, name="recipelist"),
    path("recipe/<int:num>", foodrecipe, name="foodrecipe")
]