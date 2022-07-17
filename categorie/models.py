from django.urls import reverse
from django.db import models

class Categorie(models.Model):
    category_name = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=5000,unique=True)
    
    def get_url(self):
        return reverse('product_by_category', args=[self.slug])
    class Meta:
        verbose_name = ("Categorie")
        verbose_name_plural = ("Categorie")

    def __str__(self):
        return self.category_name
