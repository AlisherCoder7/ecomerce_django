from rest_framework import serializers
from django.db import models
from django_drf.models import Product,Review,Category,ProductViewHistory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category  # Bu yerda model atributi to'g'ri ko'rsatilgan
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    avg_rating = serializers.FloatField(read_only=True, required=False)


    class Meta:
        model = Product
        fields = ['id','name','description','avg_rating','price','stock']


class ProductViewHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductViewHistory
        fields = '__all__'