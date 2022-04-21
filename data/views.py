from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, Recommendations, Category, Ordering
from .serializer import ProductSerializer, RecommendationsSerializer, CategorySerializer, OrderingSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    filter_fields = ['name', 'price']
    search_fields = ['name', 'price']
    ordering_fields = ['price', 'name', 'category']


class RecommendationsViewSet(viewsets.ModelViewSet):
    queryset = Recommendations.objects.all()
    serializer_class = RecommendationsSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    filter_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    filter_fields = ['title']
    search_fields = ['title']
    ordering_fields = ['title']


class OrderingViewSet(viewsets.ModelViewSet):
    queryset = Ordering.objects.all()
    serializer_class = OrderingSerializer

