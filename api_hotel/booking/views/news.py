from rest_framework import permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin

from hotel_admin.models import News
from api_hotel.booking.serializers.news import NewsSerializer


class NewsView(ListModelMixin, GenericViewSet):
    model = News
    queryset = model.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = NewsSerializer
