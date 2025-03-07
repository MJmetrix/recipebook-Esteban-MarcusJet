from django.urls import path
from .views import Home, RecipeList, RecipeIngredientDatabase

urlpatterns = [
    path("recipes/list/", RecipeList, name="RecipeList"),
    path("recipe/<int:num>", RecipeIngredientDatabase, name="foodrecipe")
]