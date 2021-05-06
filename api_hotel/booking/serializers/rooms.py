from rest_framework import serializers
from hotel_admin.models import Room


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("id", "capacity")
