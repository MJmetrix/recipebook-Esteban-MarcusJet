from datetime import datetime
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    def get_absolute_url(self):
        return reverse('recipe_list', args=[str(self.name)])

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('food_recipe', args=[str(self.id)])
        
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_on']


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

class RecipeImage(models.Model):
    image = models.ImageField(upload_to='images/', null=False)
    description = models.TextField(max_length=255)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe'
    )
