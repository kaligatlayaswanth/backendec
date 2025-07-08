from rest_framework import serializers
from .models import Category, Product, SuccessStory, RecommendedProduct, CarouselImage

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Category.objects.all(),
        write_only=True,
        source='categories'
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'image', 'brand', 'categories', 'category_ids', 'created_at', 'updated_at']

class SuccessStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SuccessStory
        fields = ['id', 'title', 'description', 'image_1', 'image_2', 'image_3', 'image_4', 'image_5', 'created_at', 'updated_at']

class RecommendedProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True
    )
    class Meta:
        model = RecommendedProduct
        fields = ['id', 'product', 'product_id']

class CarouselImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselImage
        fields = ['id', 'image_1', 'image_2', 'image_3']