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
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'image', 'brand', 'categories', 'category_ids', 'created_at', 'updated_at']

class SuccessStorySerializer(serializers.ModelSerializer):
    image_1 = serializers.SerializerMethodField()
    image_2 = serializers.SerializerMethodField()
    image_3 = serializers.SerializerMethodField()
    image_4 = serializers.SerializerMethodField()
    image_5 = serializers.SerializerMethodField()

    def get_image_1(self, obj):
        return obj.image_1.url if obj.image_1 else None

    def get_image_2(self, obj):
        return obj.image_2.url if obj.image_2 else None

    def get_image_3(self, obj):
        return obj.image_3.url if obj.image_3 else None

    def get_image_4(self, obj):
        return obj.image_4.url if obj.image_4 else None

    def get_image_5(self, obj):
        return obj.image_5.url if obj.image_5 else None

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
    image_1 = serializers.SerializerMethodField()
    image_2 = serializers.SerializerMethodField()
    image_3 = serializers.SerializerMethodField()

    def get_image_1(self, obj):
        return obj.image_1.url if obj.image_1 else None

    def get_image_2(self, obj):
        return obj.image_2.url if obj.image_2 else None

    def get_image_3(self, obj):
        return obj.image_3.url if obj.image_3 else None

    class Meta:
        model = CarouselImage
        fields = ['id', 'image_1', 'image_2', 'image_3']