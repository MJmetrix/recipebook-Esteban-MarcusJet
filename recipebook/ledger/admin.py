from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_filter = ('name', )
    list_display = ('name', )
    
class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient    
    list_filter = ('name', )
    list_display = ('name', )


class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    
    list_display = ('Recipe', 'Ingredient', 'Quantity',)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)