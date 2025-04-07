from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import *


def Home(request):
    template = loader.get_template('recipesite.html')
    return HttpResponse(template.render())

@login_required
def RecipeAdd(request):
    recipe_form = RecipeForm(request.POST or None)
    formset = RecipeIngredientFormSet(request.POST or None)

    if 'create_recipe' in request.POST and recipe_form.is_valid():
        recipe = recipe_form.save(commit=False)
        profile = Profile.objects.get(user=request.user)
        recipe.author = profile
        recipe.save()

        return redirect('recipe_list')

    elif 'add_ingredient' in request.POST and formset.is_valid():
        for form in formset:
            recipe = form.cleaned_data.get('recipe')
            ingredient = form.cleaned_data.get('ingredient')
            new_ingredient = form.cleaned_data.get('new_ingredient')
            quantity = form.cleaned_data.get('quantity')
            
            if new_ingredient:
                ingredient = Ingredient.objects.create(name=new_ingredient)

            if ingredient and quantity:
                recipe_ingredient = form.save(commit=False)
                recipe_ingredient = RecipeIngredient(
                    recipe=recipe,
                    ingredient=ingredient,
                    quantity=quantity
                )
                recipe_ingredient.save()

        return redirect('recipe_list')


    ctx = {"formset": formset, "recipe_form": recipe_form}
    return render(request, 'foodrecipecreate.html', ctx)

@login_required
def RecipeImageAdd(request, num):
    recipe = Recipe.objects.get(id=num) 
    image_form = RecipeImageForm(request.POST, request.FILES)

    if image_form.is_valid():
        recipe_image = image_form.save(commit=False)
        recipe_image = RecipeImage(
            recipe=recipe,
            description=recipe_image.description,
            image=recipe_image.image,
        )
        recipe_image.save()

        return redirect('food_recipe', num=recipe.id)

    ctx = {"image_form":image_form, "recipe": recipe}
    return render(request, 'foodrecipeimageadd.html', ctx)

@login_required
def RecipeList(request):
    recipes = Recipe.objects.filter(author=request.user.profile)
   
    return render(request, 'foodrecipelist.html', {"recipes" : recipes})

@login_required
def RecipeIngredientDatabase(request, num=1):
    recipe = Recipe.objects.get(id=num) 
    ingredients = RecipeIngredient.objects.filter(recipe=recipe) 
    images = recipe.recipe.all()

    if recipe.author != request.user.profile:
        return redirect('recipe_list')

    else:

        ctx = {
            'recipe': recipe,
            'Name': recipe.name,
            'author': recipe.author.name,
            'ingredients':[{'ingredient': ingredient.ingredient.name, 'quantity': ingredient.quantity  }
            for ingredient in ingredients],
            'images': images
            }

        return render(request, 'foodrecipedetail.html', ctx)