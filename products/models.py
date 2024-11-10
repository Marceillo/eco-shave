from django.db import models
from star_ratings.models import Rating
from django.contrib.contenttypes.fields import GenericRelation


class Category(models.Model):
    """
    for the differant categories
    such as Razors,shaving,
    brushes,soaps ect. 
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254,
    null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.friendly_name or self.name

class Product(models.Model):
    """
    For the product details and category
    and shows if the product is active or 
    discontinued.
    """
    category = models.ForeignKey(Category, null=True,
    blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8,
    decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024,
    null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    rating = GenericRelation(Rating)

    def __str__(self):
        
        return f"{self.name} ({self.sku})"

# from django docs
class PreviewImage(models.Model):
    """
    To store multiple images for one product
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='preview_images/')