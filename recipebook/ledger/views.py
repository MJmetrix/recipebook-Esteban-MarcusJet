from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Ingredient, Recipe, RecipeIngredient


# Create your views here.
def Home(request):
    template = loader.get_template('recipesite.html')
    return HttpResponse(template.render())

def RecipeList(request):
    recipes = Recipe.objects.all()
   
    return render(request, 'recipelistsite.html', {"recipes" : recipes})

def RecipeIngredientDatabase(request, num=1):
    recipe = Recipe.objects.get(id=num) 
    ingredients = RecipeIngredient.objects.filter(recipe=recipe) 

    ctx = {
        'Name': recipe.name,
        'author': recipe.author.name,
        'ingredients':[{'ingredient': ingredient.ingredient.name, 'quantity': ingredient.quantity  }
        for ingredient in ingredients] 
    }
    
    return render(request, 'foodrecipetemplate.html', ctx)