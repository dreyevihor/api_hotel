from rest_framework import permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth import get_user_model

from .serializers import UserSerializer


class CreateUserView(CreateModelMixin, GenericViewSet):

    model = get_user_model()
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
