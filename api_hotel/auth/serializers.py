from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True, max_length=150)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            email=validated_data['email'],
        )

        return user

    class Meta:
        model = UserModel
        fields = ( "id", "username", "password", "first_name", "email")
