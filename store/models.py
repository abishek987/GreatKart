from django.urls import reverse
from django.db import models
from ckeditor.fields import RichTextField
from categorie.models import Categorie

# Create your models here.

class Product(models.Model):
    product_name            = models.CharField(max_length=200, unique=True)
    slug                    = models.SlugField(max_length=200, unique=True)
    product_information     = RichTextField()
    price                   = models.IntegerField()
    images                  = models.CharField(max_length=2000,)
    stock                   = models.IntegerField()
    is_available            = models.BooleanField(default=True)
    categorie               = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    created_date            = models.DateTimeField(auto_now_add=True)
    modified_date           = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    def get_url(self):
        return reverse('product_detail', args = [self.categorie.slug , self.slug])