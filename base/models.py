from django.db import models
import os
from django.conf import settings
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    brand = models.CharField(max_length=100)
    image = CloudinaryField('image', folder='products/')
    categories = models.ManyToManyField(Category, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk:
            old = Product.objects.filter(pk=self.pk).first()
            if old and old.image and old.image != self.image:
                old_path = old.image.path
                if os.path.isfile(old_path):
                    os.remove(old_path)
        super().save(*args, **kwargs)

class SuccessStory(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_1 = CloudinaryField('image', folder='success_stories/')
    image_2 = CloudinaryField('image', folder='success_stories/', blank=True, null=True)
    image_3 = CloudinaryField('image', folder='success_stories/', blank=True, null=True)
    image_4 = CloudinaryField('image', folder='success_stories/', blank=True, null=True)
    image_5 = CloudinaryField('image', folder='success_stories/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk:
            old = SuccessStory.objects.filter(pk=self.pk).first()
            for field in ["image_1", "image_2", "image_3", "image_4", "image_5"]:
                old_img = getattr(old, field)
                new_img = getattr(self, field)
                if old_img and old_img != new_img:
                    old_path = old_img.path
                    if os.path.isfile(old_path):
                        os.remove(old_path)
        super().save(*args, **kwargs)

class RecommendedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='recommended')

    def __str__(self):
        return self.product.name

class CarouselImage(models.Model):
    image_1 = CloudinaryField('image', folder='carousel/')
    image_2 = CloudinaryField('image', folder='carousel/')
    image_3 = CloudinaryField('image', folder='carousel/')
    

    def __str__(self):
        return f"Carousel Image {self.id}"

    def save(self, *args, **kwargs):
        if self.pk:
            old = CarouselImage.objects.filter(pk=self.pk).first()
            for field in ["image_1", "image_2", "image_3"]:
                old_img = getattr(old, field)
                new_img = getattr(self, field)
                if old_img and old_img != new_img:
                    old_path = old_img.path
                    if os.path.isfile(old_path):
                        os.remove(old_path)
        super().save(*args, **kwargs)