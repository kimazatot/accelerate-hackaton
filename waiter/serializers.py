from rest_framework import serializers
from .models import Waiter, Review


class WaiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waiter
        fields = ['id', 'name', 'age', 'photo', 'establishment']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'waiter', 'stars', 'comment', 'created_at']
