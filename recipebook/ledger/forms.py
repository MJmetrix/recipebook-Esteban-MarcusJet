from django import forms
from .models import *
from django.forms import formset_factory

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name']


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity']

    ingredient = forms.ModelChoiceField(
        queryset=Ingredient.objects.all(), 
        required=False,
    )

    new_ingredient = forms.CharField(required=False, label="New Ingredient")

    def clean(self):
        cleaned_data = super().clean()
        ingredient = cleaned_data.get('ingredient')
        new_ingredient = cleaned_data.get('new_ingredient')

        if ingredient and new_ingredient:
            raise forms.ValidationError("Must select a new ingredient or list a new one, not both.")
        if not ingredient and not new_ingredient:
            raise forms.ValidationError("No Ingredient. please select or enter a new ingredient.")

        return cleaned_data

    def get_ingredient(self):
        return self.cleaned_data.get('new_ingredient') or self.cleaned_data.get('ingredient')   

RecipeIngredientFormSet = formset_factory(
    RecipeIngredientForm,
    extra=1,
)

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description']
        