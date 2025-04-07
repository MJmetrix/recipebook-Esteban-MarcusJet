from django.urls import path
from .views import *
from django.shortcuts import redirect

urlpatterns = [
    path("", lambda request: redirect("recipe_list")),
    path("recipes/list/", RecipeList, name="recipe_list"),
    path("recipe/<int:num>", RecipeIngredientDatabase, name="food_recipe"),
    path("recipe/add/", RecipeAdd, name= "recipe_add")
]