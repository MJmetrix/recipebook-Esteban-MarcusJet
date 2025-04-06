from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    
class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeImageInline]
    list_filter = ('name', )
    list_display = ('author','name', 'created_on', 'updated_on')
    
class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient    
    list_filter = ('name', )
    list_display = ('name', )

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    list_display = ('recipe__author','recipe', 'ingredient', 'quantity',)
    search_fields = ('recipe__name', )

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('user', 'name', 'bio',)
    can_delete = False

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeImage)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)