from rest_framework import serializers
from .models import Payment, Review, Waiter, RegistrationRequest, QRCode


class RegistrationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationRequest
        fields = ('id', 'establishment_name', 'contact_email', 'status', 'created_at')
        read_only_fields = ('id', 'status', 'created_at')


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
        fields = ['id', 'name', 'age', 'photo']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'waiter', 'stars', 'comment', 'created_at']


class QRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRCode
        fields = ['id', 'data', 'qr_code_image']