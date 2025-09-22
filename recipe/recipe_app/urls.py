from django.urls import path
from .views import (
    RecipeListView, RecipeDetailView, RecipeCreateView, 
    RecipeUpdateView, RecipeDeleteView,
    IngredientListView, IngredientCreateView, IngredientUpdateView, IngredientDeleteView,
    InstructionListView, InstructionCreateView, InstructionUpdateView, InstructionDeleteView,  # Changed names
    recipe_search
)

urlpatterns = [
    # Recipe URLs
    path('', RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/new/', RecipeCreateView.as_view(), name='recipe_create'),
    path('recipe/<int:pk>/edit/', RecipeUpdateView.as_view(), name='recipe_update'),
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe_delete'),
    
    # Ingredient URLs
    path('ingredients/', IngredientListView.as_view(), name='ingredient_list'),
    path('ingredient/new/', IngredientCreateView.as_view(), name='ingredient_create'),
    path('ingredient/<int:pk>/edit/', IngredientUpdateView.as_view(), name='ingredient_update'),
    path('ingredient/<int:pk>/delete/', IngredientDeleteView.as_view(), name='ingredient_delete'),
    
    # Instruction URLs (renamed from CookingInstruction)
    path('instructions/', InstructionListView.as_view(), name='cooking_instruction_list'),  # Keep URL name same
    path('instruction/new/', InstructionCreateView.as_view(), name='cooking_instruction_create'),  # Keep URL name same
    path('instruction/<int:pk>/edit/', InstructionUpdateView.as_view(), name='cooking_instruction_update'),  # Keep URL name same
    path('instruction/<int:pk>/delete/', InstructionDeleteView.as_view(), name='cooking_instruction_delete'),  # Keep URL name same
    
    # Search
    path('search/', recipe_search, name='recipe_search'),
]