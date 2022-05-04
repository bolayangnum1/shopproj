from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import Product, Recommendations, Category, Ordering
from .serializer import ProductSerializer, RecommendationsSerializer, CategorySerializer, OrderingSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter


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
        import requests
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()

        tg_message = {
            "text": f"имя: ФИО: {serializer.data['full_name']}\n Номер телефона: {serializer.data['phone_number']}\n Область: {serializer.data['region']}\n Адрес: {serializer.data['address']}\n Цена: {serializer.data['price']}\n Корзина: {serializer.data['basket']}",
            "chat_id": "679974348" #if is group -100
        }
        url = "https://api.telegram.org/bot5346235377:AAGg1mWc4FPRxGn1GFcnOBcj75MMLlrAJlA/sendMessage"
        response = requests.post(url, json=tg_message)
        print(response.text)
        return super().create(request)


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

