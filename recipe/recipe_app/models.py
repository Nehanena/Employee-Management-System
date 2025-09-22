from django.db import models
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        if self.quantity:
            return f"{self.name} - {self.quantity}"
        return self.name

class Instruction(models.Model):
    step_number = models.IntegerField()
    description = models.TextField()
    
    def __str__(self):
        return f"Step {self.step_number}"

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='recipes/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)  # SIMPLE relationship
    instructions = models.ManyToManyField(Instruction)  # SIMPLE relationship
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title