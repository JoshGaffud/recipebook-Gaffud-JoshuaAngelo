from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('ledger:ingredient-detail', args=[str(self.id)])

    def __str__(self):
        return self.ingredient_name
    

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args=[str(self.id)])

    def __str__(self):
        return self.recipe_name
    

class RecipeIngredient(models.Model):
    recipe_quantity = models.CharField(max_length=100)
    recipe_ingredient = models.ForeignKey(
        Ingredient, on_delete = models.CASCADE, related_name='recipe'
        )
    recipe_recipe = models.ForeignKey(
        Recipe, on_delete = models.CASCADE, related_name='ingredients'
        )

    def __str__(self):
        return f"{self.recipe_quantity} of {self.recipe_ingredient.ingredient_name}"
# Create your models here.
