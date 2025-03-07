from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    
class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    
    # search_fields = ('Recipe', )
    list_display = ('Recipe', 'Ingredient', 'Quantity',)
    # list_filter = ('Ingredient', )





# registering the model and the admin is what tells
# Django that admin pages must be generated for the models specified
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)