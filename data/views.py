from django.core.mail import send_mail
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import Product, Recommendations, Category, Ordering, Review
from .serializer import ProductSerializer, RecommendationsSerializer, CategorySerializer, OrderingSerializer, ReviewSerializer
from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response


class PaginationProduct(PageNumberPagination):
    page_size = 20
    max_page_size = 1000


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    filter_fields = ['name', 'price']
    search_fields = ['name', 'price']
    ordering_fields = ['price', 'name', 'category']
    pagination_class = PaginationProduct

    def create(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            price = serializer.validated_data.get('price')
            description = serializer.validated_data.get('description')
            are_available = serializer.validated_data.get('are_available')
            amount = serializer.validated_data.get('amount')
            img = serializer.validated_data.get('img')

            send_mail('adanovbolot312@gmail.com', from_email='adanovbolot312@gmail.com',
                      message=f"{name} {description} {price} {are_available} {amount} {img}",
                      recipient_list=['adanovbolot312@gmail.com'])
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
