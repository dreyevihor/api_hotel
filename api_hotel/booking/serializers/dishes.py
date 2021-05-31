from rest_framework import serializers
from hotel_admin.models import Dish, DishOrder, Order, Room
from django.contrib.auth import get_user_model
import logging

User = get_user_model()
logger = logging.getLogger(__name__)


class DishSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
            max_length=None, use_url=True
        )

    class Meta:
        model = Dish
        fields = ("id", "title", "weight", "description", "image", "price")


class DishOrderSerializer(serializers.ModelSerializer):
    dish = DishSerializer(read_only=True)
    dish_id = serializers.PrimaryKeyRelatedField(queryset=Dish.objects.all(), write_only=True)

    class Meta:
        model = DishOrder
        fields = ("id", "dish", "count", "dish_id")


class OrderSerializer(serializers.ModelSerializer):
    dishes = DishOrderSerializer(many=True, source="dishorder_set")
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        dishes = validated_data.pop("dishorder_set", [])
        instance = super(OrderSerializer, self).create(validated_data)
        dish_order_objs = [DishOrder(dish=d["dish_id"], count=d["count"], order=instance) for d in dishes]
        DishOrder.objects.bulk_create(dish_order_objs)
        instance.refresh_from_db()
        return instance

    class Meta:
        model = Order
        fields = ("id", "created", "destination_time", "room", "dishes", )
