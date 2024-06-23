from rest_framework import serializers
from .models import Payment, Review, Waiter, Establishment


class PaymentSerializer(serializers.ModelSerializer):
    qr_url = serializers.URLField(read_only=True)
    checkout_url = serializers.URLField(read_only=True)

    class Meta:
        model = Payment
        fields = [
            'id',
            'amount',
            'status',
            'description',
            'qr_url',
            'checkout_url',
            'created_at',
            'committed_at',
        ]



class WaiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waiter
        fields = ['id', 'name', 'age']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'waiter', 'stars', 'comment', 'created_at']


class EstablishmentSerializer(serializers.ModelSerializer):
    qr_code_url = serializers.URLField(source='qr_code_url', read_only=True)

    class Meta:
        model = Establishment
        fields = [
            'id',
            'owner_name',
            'phone_number',
            'address',
            'qr_code_url',
        ]
