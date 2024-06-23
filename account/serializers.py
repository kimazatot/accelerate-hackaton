from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Establishment

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(min_length=8, write_only=True)
    name = serializers.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('email', 'password', 'password_confirm', 'name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь с таким email уже существует.')
        return email

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('Пароли не совпадают.')
        return attrs

    def create(self, validated_data):
        name = validated_data.pop('name', '')
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            last_name=validated_data.get('last_name', '')
        )
        user.name = name
        user.save()
        return user


class EstablishmentSerializer(serializers.ModelSerializer):
    owner_email = serializers.EmailField(source='owner.email', read_only=True)

    class Meta:
        model = Establishment
        fields = ('id', 'owner', 'owner_email', 'name', 'address', 'pending_approval', 'created_at')
        read_only_fields = ('id', 'owner', 'pending_approval', 'created_at')
