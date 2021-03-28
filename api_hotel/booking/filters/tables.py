from datetime import timedelta
from django_filters import FilterSet, IsoDateTimeFilter
from django.db.models import Q


class TableFilter(FilterSet):
    free_at = IsoDateTimeFilter(field_name='free_at', method='filter_free_at')

    def filter_free_at(self, queryset, name, value):
        before_booking_hour_q = Q(tablebooking__destination_time__gte=value - timedelta(hours=1)) & \
                                Q(tablebooking__destination_time__lte=value + timedelta(hours=1))
        return queryset.exclude(before_booking_hour_q)