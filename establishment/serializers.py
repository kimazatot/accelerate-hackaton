from rest_framework import serializers
from .models import Establishment


class EstablishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Establishment
        fields = ('id', 'owner_name', 'phone_number', 'address')
