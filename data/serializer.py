from rest_framework import serializers
from .models import Product, TheSize, Recommendations, Category, Ordering, Color, Discount


class TheSizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = TheSize
        fields = '__all__'

#start
class OrderingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ordering
        fields = ['full_name', 'id', 'phone_number', 'region', 'price', 'basket']


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = '__all__'


class DiscountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discount
        fields = '__all__'


class RecommendationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recommendations
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    product_detail = ColorSerializer(many=True)
    prod_detail = TheSizeSerializer(many=True)
    discount_detail = DiscountSerializer(many=True)
    recommendations_detail = RecommendationsSerializer(many=True)
    category_detail = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
