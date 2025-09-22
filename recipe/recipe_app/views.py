from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, Ingredient, Instruction  # Changed from CookingInstruction
from .forms import RecipeForm, IngredientForm, InstructionForm  # Changed from CookingInstructionForm

# RECIPE Views
class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'  # Your actual template
    context_object_name = 'recipes'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'  # Your actual template
    context_object_name = 'recipe'

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_form.html'  # Your actual template
    success_url = reverse_lazy('recipe_list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_form.html'  # Your actual template
    success_url = reverse_lazy('recipe_list')

class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = 'recipe_confirm_delete.html'  # Your actual template
    success_url = reverse_lazy('recipe_list')

# INGREDIENT Views
class IngredientListView(ListView):
    model = Ingredient
    template_name = 'ingredient_list.html'  # Your actual template
    context_object_name = 'ingredients'

class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'ingredient_form.html'  # Your actual template
    success_url = reverse_lazy('ingredient_list')

class IngredientUpdateView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'ingredient_form.html'  # Your actual template
    success_url = reverse_lazy('ingredient_list')

class IngredientDeleteView(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = 'ingredient_confirm_delete.html'  # Your actual template
    success_url = reverse_lazy('ingredient_list')

# INSTRUCTION Views (renamed from CookingInstruction)
class InstructionListView(ListView):
    model = Instruction
    template_name = 'cooking_instruction_list.html'  # Keep your existing template name
    context_object_name = 'instructions'

class InstructionCreateView(LoginRequiredMixin, CreateView):
    model = Instruction
    form_class = InstructionForm
    template_name = 'cooking_instruction_form.html'  # Keep your existing template name
    success_url = reverse_lazy('cooking_instruction_list')

class InstructionUpdateView(LoginRequiredMixin, UpdateView):
    model = Instruction
    form_class = InstructionForm
    template_name = 'cooking_instruction_form.html'  # Keep your existing template name
    success_url = reverse_lazy('cooking_instruction_list')

class InstructionDeleteView(LoginRequiredMixin, DeleteView):
    model = Instruction
    template_name = 'cooking_instruction_confirm_delete.html'  # Keep your existing template name
    success_url = reverse_lazy('cooking_instruction_list')

# SEARCH Function
def recipe_search(request):
    query = request.GET.get('q')
    
    if query:
        recipes = Recipe.objects.filter(
            Q(ingredients__name__icontains=query)
        ).distinct()
    else:
        recipes = Recipe.objects.all()
    
    return render(request, 'recipe_list.html', {'recipes': recipes})