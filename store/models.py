from django.db import models
from datetime import datetime

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name="Kategoriya"
        verbose_name_plural="Kategoriyalar"

    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/")
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    class Meta:
        verbose_name="Kichik kategoriya"
        verbose_name_plural="Kichik kategoriyalar"

    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = "mahsulot"
        verbose_name_plural = "mahsulotlar"

    name = models.CharField(max_length=255)
    price = models.FloatField()
    slug = models.CharField(max_length=255)
    stock = models.IntegerField()
    description = models.TextField()
    rating = models.FloatField()
    image = models.ImageField(upload_to="media/uploadphotos/")
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    def get_rating_precent(self):
        return 100 * (self.rating / 5)

    
    def is_new_product(self):
        time_delta = datetime.now() - self.created.replace(tzinfo=None)
        return time_delta.days < 4
    
    
class ProductColor(models.Model):
    name = models.CharField(max_length=50)
    

class ProductSize(models.Model):
    name = models.CharField(max_length=20)
    
    
class ProductImage(models.Model):
    image = models.ImageField(upload_to="media/uploadmorephotos")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
