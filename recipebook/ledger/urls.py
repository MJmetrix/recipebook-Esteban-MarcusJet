from django.urls import path
from .views import Home, RecipeList, RecipeIngredientDatabase
from django.shortcuts import redirect

urlpatterns = [
    path("", lambda request: redirect("recipeList")),
    path("recipes/list/", RecipeList, name="recipeList"),
    path("recipe/<int:num>", RecipeIngredientDatabase, name="foodRecipe")
]