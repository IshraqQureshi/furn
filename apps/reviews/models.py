from django.db import models
from apps.products.models import Product

# Create your models here.
class Review(models.Model):
    author = models.CharField(max_length=256)
    review = models.TextField()

    def __str__(self):
        return self.author
