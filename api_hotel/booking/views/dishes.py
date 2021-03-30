from rest_framework import permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin

from hotel_admin.models import Dish, Order
from api_hotel.booking.serializers.dishes import DishSerializer, OrderSerializer


class DishView(ListModelMixin, GenericViewSet):
    model = Dish
    queryset = model.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = DishSerializer


class OrderView(CreateModelMixin, ListModelMixin, DestroyModelMixin, GenericViewSet):
    model = Order
    queryset = model.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = OrderSerializer

    def get_queryset(self, *args, **kwargs):
        return self.model.objects.filter(user=self.request.user)
