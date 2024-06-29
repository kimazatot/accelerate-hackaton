from rest_framework import serializers
from .models import Establishment, Tip


class EstablishmentSerializer(serializers.ModelSerializer):
    get_absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Establishment
        fields = ['id', 'name', 'owner_name', 'owner_phone', 'address', 'qr_code', 'get_absolute_url']

    def get_get_absolute_url(self, obj):
        return obj.get_absolute_url()


class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
        fields = ['id', 'establishment', 'amount', 'created_at']
