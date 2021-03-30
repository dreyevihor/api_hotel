from rest_framework import serializers
from hotel_admin.models import RoomService, Room


class RoomServiceSerializer(serializers.ModelSerializer):
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)

    class Meta:
        model = RoomService
        fields = ("id", "room", "destination_time")
