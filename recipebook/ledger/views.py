from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


# Create your views here.
def Home(request):
    template = loader.get_template('recipesite.html')
    return HttpResponse(template.render())

@login_required
def RecipeList(request):
    recipes = Recipe.objects.filter(author=request.user.profile)
   
    return render(request, 'recipelistsite.html', {"recipes" : recipes})

@login_required
def RecipeIngredientDatabase(request, num=1):
    recipe = Recipe.objects.get(id=num) 
    ingredients = RecipeIngredient.objects.filter(recipe=recipe) 

    if recipe.author != request.user.profile:
        return redirect('/recipes/list')

    else:

        ctx = {
            'Name': recipe.name,
            'author': recipe.author.name,
            'ingredients':[{'ingredient': ingredient.ingredient.name, 'quantity': ingredient.quantity  }
            for ingredient in ingredients] 
            }

        return render(request, 'foodrecipetemplate.html', ctx)