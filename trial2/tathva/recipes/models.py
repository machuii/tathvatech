from django.db import models
from django.urls import reverse


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    slugs = models.SlugField(null=True, unique=True)


    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={"slug": self.slugs})

    

    