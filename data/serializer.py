from django.contrib.sites import requests
from rest_framework import serializers
from .models import Product, TheSize, Recommendations, Category, Ordering, Color, Review


class TheSizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = TheSize
        fields = '__all__'


class OrderingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ordering
        fields = ['full_name', 'id', 'phone_number', 'region', 'price', 'basket']


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = '__all__'


class RecommendationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recommendations
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('creview', 'userview', 'id', 'review', 'created_date', 'rating')


class ProductSerializer(serializers.ModelSerializer):
    product_detail = ColorSerializer(many=True)
    prod_detail = TheSizeSerializer(many=True)
    recommendations_detail = RecommendationsSerializer(many=True)
    category = CategorySerializer()

    def create(self, validated_data):
        product = Product.objects.create(
            name=validated_data['name'],
            img=validated_data['img'],
            price=validated_data['price'],
            description=validated_data['description'],
            are_available=validated_data['are_available'],
            amount=validated_data['amount'],
        )
        product.save()
        data = {
            "text": f"Имя - {validated_data['name']},\n\
    poter - {validated_data['img']},\n\
    movers - {validated_data['price']},\n\
    dispersal - {validated_data['description']},\n\
    trash = {validated_data['are_available']},\n\
    Описание - {validated_data['amount']}",
            "chat_id": "795677145"
        }
        r = requests.post('https://api.telegram.org/bot5237491474:AAGKWsOrNVh91jPf21o5pJJ1m0VGCtEoJoM/sendMessage',
                          json=data)
        print(r.text)
        return product

    class Meta:
        model = Product
        fields = '__all__'
