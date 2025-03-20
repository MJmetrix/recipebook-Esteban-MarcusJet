from datetime import datetime
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    def get_absolute_url(self):
        return reverse('recipeList', args=[str(self.name)])

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    def get_absolute_url(self):
        return reverse('foodRecipe', args=[str(self.id)])
        

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients'
    )

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='recipe'
    )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=50)
