from rest_framework import permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin

from hotel_admin.models import RoomService, Table
from api_hotel.booking.serializers.services import RoomServiceSerializer


class RoomServiceView(CreateModelMixin, ListModelMixin, DestroyModelMixin, GenericViewSet):
    model = RoomService
    queryset = model.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = RoomServiceSerializer

    def get_queryset(self, *args, **kwargs):
        return self.model.objects.filter(user=self.request.user)
