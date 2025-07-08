from django.contrib import admin
from .models import Category, Product, SuccessStory, RecommendedProduct, CarouselImage

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(SuccessStory)
admin.site.register(RecommendedProduct)
admin.site.register(CarouselImage)
