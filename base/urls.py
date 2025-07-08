from django.urls import path
from .views import (
    ProductListCreateAPIView, ProductDetailAPIView,
    SuccessStoryListCreateAPIView, SuccessStoryDetailAPIView,
    RecommendedProductListCreateAPIView, RecommendedProductDetailAPIView,
    CarouselImageListCreateAPIView,
    CategoryListCreateAPIView, CategoryDetailAPIView
)

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('success-stories/', SuccessStoryListCreateAPIView.as_view(), name='successstory-list-create'),
    path('success-stories/<int:pk>/', SuccessStoryDetailAPIView.as_view(), name='successstory-detail'),
    path('recommended-products/', RecommendedProductListCreateAPIView.as_view(), name='recommendedproduct-list-create'),
    path('recommended-products/<int:pk>/', RecommendedProductDetailAPIView.as_view(), name='recommendedproduct-detail'),
    path('carousel-images/', CarouselImageListCreateAPIView.as_view(), name='carouselimage-list-create'),
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
]