from datetime import timedelta

from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import serializers

from hotel_admin.models import TableBooking, Table

User = get_user_model()


class BookTableSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    table = serializers.PrimaryKeyRelatedField(queryset=Table.objects.all())

    def validate(self, data):
        destination_time = data["destination_time"]
        before_booking_hour_q = Q(destination_time__gte=destination_time-timedelta(hours=1)) &\
                                Q(destination_time__lte=destination_time+timedelta(hours=1))
        booked = TableBooking.objects.filter(before_booking_hour_q, table=data["table"]).exists()
        if booked:
            raise serializers.ValidationError({"destination_time": "Already booked."})
        return data

    class Meta:
        model = TableBooking
        fields = ("user", "table", "destination_time")


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ("id", "capacity")
