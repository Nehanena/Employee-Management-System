from django import forms
from .models import Recipe, Ingredient, Instruction  # Changed from CookingInstruction

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity']  # Added quantity field

class InstructionForm(forms.ModelForm):  # Changed from CookingInstructionForm
    class Meta:
        model = Instruction  # Changed from CookingInstruction
        fields = ['step_number', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }