from rest_framework import permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin

from hotel_admin.models import TableBooking, Table
from api_hotel.booking.serializers.tables import BookTableSerializer, TableSerializer
from api_hotel.booking.filters.tables import TableFilter


class BookTableView(CreateModelMixin, ListModelMixin, GenericViewSet):
    model = TableBooking
    queryset = model.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BookTableSerializer

    def get_queryset(self, *args, **kwargs):
        return self.model.objects.filter(user=self.request.user)


class TableView(ListModelMixin, GenericViewSet):
    model = Table
    queryset = model.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    filter_class = TableFilter
    serializer_class = TableSerializer

