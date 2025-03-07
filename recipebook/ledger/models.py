from datetime import datetime
from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('ingredient_detail', args=[str(self.name)])

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.name)])

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    Quantity = models.IntegerField()
    Recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients'
    )

    Ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='recipe'
    )
   

    
 