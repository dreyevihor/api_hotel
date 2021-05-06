from rest_framework import permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin

from hotel_admin.models import Room
from api_hotel.booking.serializers.rooms import RoomsSerializer


class RoomsView(ListModelMixin, GenericViewSet):
    model = Room
    queryset = model.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = RoomsSerializer
