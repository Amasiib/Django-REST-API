from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book

# Serializer للـ Book
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

# Serializer للتسجيل
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user
