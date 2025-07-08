from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, SuccessStory, RecommendedProduct, CarouselImage
from .serializers import CategorySerializer, ProductSerializer, SuccessStorySerializer, RecommendedProductSerializer, CarouselImageSerializer


class ProductListCreateAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return None

    def get(self, request, pk):
        product = self.get_object(pk)
        if not product:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        if not product:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        if not product:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SuccessStoryListCreateAPIView(APIView):
    def get(self, request):
        stories = SuccessStory.objects.all()
        serializer = SuccessStorySerializer(stories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SuccessStorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SuccessStoryDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return SuccessStory.objects.get(pk=pk)
        except SuccessStory.DoesNotExist:
            return None

    def get(self, request, pk):
        story = self.get_object(pk)
        if not story:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = SuccessStorySerializer(story)
        return Response(serializer.data)

    def put(self, request, pk):
        story = self.get_object(pk)
        if not story:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = SuccessStorySerializer(story, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        story = self.get_object(pk)
        if not story:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        story.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RecommendedProductListCreateAPIView(APIView):
    def get(self, request):
        recs = RecommendedProduct.objects.all()
        serializer = RecommendedProductSerializer(recs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecommendedProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecommendedProductDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return RecommendedProduct.objects.get(pk=pk)
        except RecommendedProduct.DoesNotExist:
            return None

    def get(self, request, pk):
        rec = self.get_object(pk)
        if not rec:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = RecommendedProductSerializer(rec)
        return Response(serializer.data)

    def put(self, request, pk):
        rec = self.get_object(pk)
        if not rec:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = RecommendedProductSerializer(rec, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        rec = self.get_object(pk)
        if not rec:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        rec.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CarouselImageListCreateAPIView(APIView):
    def get(self, request):
        carousels = CarouselImage.objects.all()
        serializer = CarouselImageSerializer(carousels, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CarouselImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryListCreateAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return None

    def get(self, request, pk):
        category = self.get_object(pk)
        if not category:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_object(pk)
        if not category:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_object(pk)
        if not category:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

