from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Ingredient, Recipe, RecipeIngredient

# Create your views here.
def Home(request):
    template = loader.get_template('recipesite.html')
    return HttpResponse(template.render())

def RecipeList(request):
    return render(request, 'recipelistsite.html')

def RecipeIngredientDatabase(request, num=1):
    recipe = Recipe.objects.get(id=num) 
    ingredients = RecipeIngredient.objects.filter(Recipe=recipe) 

    ctx = {
        'Name': recipe.name,
        'ingredients':[{'ingredient': ingredient.Ingredient.name, 'quantity': ingredient.Quantity  }
        for ingredient in ingredients] 
    }
    return render(request, 'foodrecipetemplate.html', ctx)