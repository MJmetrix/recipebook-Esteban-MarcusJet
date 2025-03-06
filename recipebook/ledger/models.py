from datetime import datetime
from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

class Recipe(models.Model):
    name = models.CharField(max_length=50)

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
    def __str__(self):
        return '{} requires {}{}'.format(self.Recipe, self.Quantity, self.Ingredient)

    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.name)])
 
    # @property
    # def is_due(self):
    #     return datetime.now() >= self.due_date

    # class Meta:
    #     ordering = ['due_date'] # order by due date ascending order
    #     unique_together = ['due_date', 'name'] # Don't create a duplicate task
    #     verbose_name = 'task'
    #     verbose_name_plural = 'tasks'