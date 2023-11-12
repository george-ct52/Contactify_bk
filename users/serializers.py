from rest_framework import serializers
from django.contrib.auth.hashers import make_password  # Import make_password
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email", "password"]
        extra_kwargs = {
            "password": {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        hashed_password = make_password(password)  # Hash the password

        instance = self.Meta.model(**validated_data, password=hashed_password)
        instance.save()
        return instance

