from django.contrib import admin
from .models import Recipe, Ingredient, Instruction

# Unregister if already registered
admin.site.register(Ingredient)
admin.site.register(Instruction)
admin.site.register(Recipe)

